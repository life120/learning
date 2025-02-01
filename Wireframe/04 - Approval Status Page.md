### **Updated Breakdown of the Approval Status Page**  

The **Approval Status Page** allows users to track the progress of their access requests efficiently.

---

### **1. Sidebar Navigation**  
- **Portal Logo & Title:** Displays "Self-Service Portal."  
- **Navigation Menu:**  
  - Home  
  - Request Access  
  - **Approval Status (Current Page Highlighted)**  
  - Help/FAQs  
  - Admin Dashboard  

---

### **2. Header Section**  
- **Title:** "Approval Status"  
- **Brief Description:** Explains that users can filter and track their requests.  
- **User Profile Menu** (Top-right, includes settings, logout, and dark mode toggle)  
- **Notifications Icon** (Bell icon for updates and pending approvals)  

---

### **3. Search & Filter Panel**  
- **Search Bar:** Allows users to search by **URL, Request ID, or Requester Name**.  
- **Filters:**
  - **Status:** Pending, Approved, Cancelled, Rejected, All  
  - **Request Type:** Self, Colleague, Server  
  - **Date Selector:** Users can filter by request submission date.  
  - **Show Requests Dropdown:** Allows users to display **10 or 20 requests per page**.  

---

### **4. Request Status Table**  
- **Table with sortable columns:**  
  - **Request ID** (Unique identifier for the request)  
  - **Requested URL** (URL being requested)  
  - **Request Type** (Self, Colleague, or Server)  
  - **Submitted By** (Requester’s name)  
  - **Date** (Displayed in **DD/MM/YYYY** format)  
  - **Current Status** (Pending, Approved, Cancelled, Rejected)  
  - **Action Buttons:**  
    - **🔍 View Request Details**  
    - **❌ Cancel Request** (For pending requests only)  

- **Color Indicators for Statuses:**  
  - **Green:** Approved  
  - **Orange:** Pending  
  - **Red:** Rejected  
  - **Gray:** Cancelled  

---

### **5. Sample Requests Displayed in Table**
- **Pending Request:** User can cancel it.  
- **Approved Request:** No cancel button; user can view details.  
- **Cancelled Request:** Indicates that the user cancelled it.  
- **Rejected Request:** Shows request was denied by an approver.  

---

### **6. Download Options**  
- **Flushed to the right side below the table.**  
- **Buttons:**  
  - **Download CSV**  
  - **Download PDF**  

---

### **7. Pagination Control**  
- Displays **Page 1 of 1**, indicating that all requests fit within a single page.  

---

### **Dynamic Features**  
- **Real-time Updates:** If a request status changes, the table updates automatically.  
- **Mobile Responsiveness:** Layout adjusts based on screen size.  

---

This updated breakdown ensures a **structured, user-friendly, and functional** approval tracking experience, Boss. 🚀 Let me know if you need any refinements!

### **Breakdown of the Request Details Modal**  

When the user clicks **"View"** in the **Approval Status Page**, a **modal (popup window)** appears, displaying detailed information about the request.

---

### **1. Modal Background**
- **Full-Screen Overlay:** A semi-transparent background covers the main page when the modal is open.
- **Clicking outside the modal or the close button (`×`) will close it.**

---

### **2. Modal Header**
- **Title:** "Request Details"
- **Close Button (`×`)** positioned at the top-right.

---

### **3. Request Information Section**
- **Request ID:** Displays the unique identifier of the request.
- **Requested URL:** Shows the URL for which access was requested.
- **Submitted By:** Displays the requester’s name.
- **Date:** Displays the request submission date.
- **Status:** Shows the current approval status (Pending, Approved, Rejected, Cancelled).

---

### **4. Approval Workflow Section**
- **Shows the approval progress and pending stages:**
  - **Direct Manager Approval:** ✅ Approved (Already approved)
  - **Security Manager Approval:** ⏳ Pending (Waiting for approval)

- **Future enhancements can include more approval levels like:**
  - **Risk Consultant Approval**
  - **Director Approval**
  - **Timestamps of each approval stage**

---

### **5. Dynamic Behavior**
- **The modal dynamically updates content** when a user clicks on a request’s "View" button.
- **Displays real-time approval updates** depending on the status.

---

### **6. Styling & Layout**
- **Centered modal box** with a white background and a rounded border.
- **Consistent text alignment** and spacing for readability.
- **Color-coded status indicators** to show approval progress.

---

This ensures the **Request Details Modal** is **clean, informative, and user-friendly**, Boss. 🚀 Let me know if you need any further refinements!