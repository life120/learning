from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for, session
import os
import datetime
import json

app = Flask(__name__)

app.secret_key = 'your_secret_key'
# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Mock user credentials (for demonstration)
USER_CREDENTIALS = {
    'admin': 'password123'  # username: password
}

def get_date_folder_name():
    """Generate a folder name based on the current date."""
    return datetime.datetime.now().strftime('%Y_%m_%d')


def get_current_datetime():
    """Get the current date and time in YYYY_MM_DDTHH:MM:SS format."""
    return datetime.datetime.now().strftime('%Y_%m_%dT%H:%M:%S')


@app.route('/')
def index():
    """Redirect to login or the main UI."""
    if 'username' in session:
        return redirect(url_for('upload_ui'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render the login page and handle login logic."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['username'] = username
            return redirect(url_for('upload_ui'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout the user and clear the session."""
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/upload_ui')
def upload_ui():
    """Serve the file upload UI."""
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def api_upload():
    """Handle file uploads via API."""
    if 'file' not in request.files or 'region' not in request.form:
        return jsonify({"error": "File and region are required"}), 400

    file = request.files['file']
    region = request.form['region']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Create or use the existing folder for today's date
    date_folder = get_date_folder_name()
    region_folder = os.path.join(app.config['UPLOAD_FOLDER'], region)
    upload_folder = os.path.join(region_folder, date_folder)
    os.makedirs(upload_folder, exist_ok=True)

    # Delete any existing file in the folder except the metadata.json file
    for existing_file in os.listdir(upload_folder):
        existing_file_path = os.path.join(upload_folder, existing_file)
        if os.path.isfile(existing_file_path) and existing_file != "metadata.json":
            os.remove(existing_file_path)

    # Save the new uploaded file
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Collect metadata
    metadata = {
        "name": file.filename,
        "region": region,
        "uploadDateTime": get_current_datetime(),
        "size": f"{os.path.getsize(file_path) / 1024:.2f} KB",  # Convert to kilobytes
    }

    # Save or update metadata in the JSON file
    metadata_file_path = os.path.join(upload_folder, "metadata.json")
    if os.path.exists(metadata_file_path):
        # Update existing metadata
        with open(metadata_file_path, 'r') as metadata_file:
            existing_metadata = json.load(metadata_file)

        # Update or replace metadata for this file
        existing_metadata["lastModified"] = metadata["uploadDateTime"]
        metadata.pop("uploadDateTime")
        existing_metadata.update(metadata)
    else:
        existing_metadata = metadata

    # Save the updated metadata
    with open(metadata_file_path, 'w') as metadata_file:
        json.dump(existing_metadata, metadata_file)

    return jsonify({"message": f"File uploaded successfully under '{region}' region.", "metadata": existing_metadata})


@app.route('/api/files', methods=['GET'])
def api_list_files():
    """List all uploaded files with metadata."""
    files_with_metadata = []
    for region in os.listdir(app.config['UPLOAD_FOLDER']):
        region_folder = os.path.join(app.config['UPLOAD_FOLDER'], region)
        if os.path.isdir(region_folder):
            for date_folder in os.listdir(region_folder):
                upload_folder = os.path.join(region_folder, date_folder)
                if os.path.isdir(upload_folder):
                    metadata_file_path = os.path.join(upload_folder, "metadata.json")
                    if os.path.exists(metadata_file_path):
                        with open(metadata_file_path, 'r') as metadata_file:
                            metadata = json.load(metadata_file)
                            if 'lastModified' not in metadata:
                                metadata['lastModified'] = 'NA'
                            files_with_metadata.append(metadata)
    print(files_with_metadata)
    return jsonify(files_with_metadata)


@app.route('/api/delete', methods=['POST'])
def api_delete_file():
    """Delete an upload folder and its contents."""
    data = request.json
    date_folder = data.get("dateFolder")
    region = data.get("region")

    if not date_folder or not region:
        return jsonify({"error": "Date folder and region are required"}), 400

    # Find and delete the folder
    region_folder = os.path.join(app.config['UPLOAD_FOLDER'], region)
    upload_folder = os.path.join(region_folder, date_folder)
    if os.path.exists(upload_folder) and os.path.isdir(upload_folder):
        for root, dirs, files in os.walk(upload_folder, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(upload_folder)
        return jsonify({"message": "Upload folder deleted successfully."})
    else:
        return jsonify({"error": "Folder not found."}), 404


@app.route('/uploads/<region>/<folder>/<filename>')
def serve_file(region, folder, filename):
    """Serve uploaded files."""
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], region, folder), filename)


if __name__ == '__main__':
    app.run(debug=True)
