How to create a next.js app?
Ensure that [[NPM]] is installed to the latest version
1. Check that npm is installed in your computer
	1. $npm -v
	2. $node -v
How to update node or npm?
Ensure that [[Chocolatey]] is installed and upgraded to the latest version.

npx create-next-app@latest
cd into the folder
$npm run dev

Data Fetching in NextJS

Static Site Generation: Data is always cached by default. 
Incremental Static Re-generation: Data will be re-cached every 1 hour (Your timing)
Server-side Rendering: No caching, fetches every time!
