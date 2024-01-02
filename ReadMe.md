# Scripting through Google Drive

This is a simple notebook demonstrating how to iterate through files in Google Drive.
Use of the Drive API requires the script/application to be associated with a GCP project with a client OAuth secret.

## Google Cloud
Start by logging in to GCP
### Create a project
- Click on the 'Select Project' dialog at the top of the GCP console.
- Click 'New Project', provide a project name, and click 'Create'. (Or select an existing project)
### Enable the drive API
- In the GCP console, select 'APIs & Services > Enable APIs and services'
- Click on '+ Enable APIs and Services'.
- Type 'drive' into the 'Search for APIs and Services' search box and hit 'Enter'.
- Click 'Google Drive API'.
- Click 'Enable'
### Create OAuth Consent Screen.
- In the GCP console, 'APIs & Services > OAuth Consent Screen'
- Select 'External' and click 'Create'
- Enter an app name (e.g. 'GDrive Scripts').
- For 'User support email', enter the email associated with your GCP account.
- For 'Developer contact information > Email addresses', you can use the same email.
- Click 'Save and Continue'
- Add the scope 'https://www.googleapis.com/auth/drive'. Click 'Save and Continue'.
- To be your own test user, add your email address to the list of test users. Click 'Save and Continue'.
### Create Application Credentials
- Go to 'APIs & Services > Credentials'
- Click '+ Create Credentials' and select 'OAuth client ID'.
- For 'Application type', select 'Desktop app'
- Assign a name (e.g. GDrive Scripts).
- Submit form.
- At the bottom of the 'OAuth client created' form, click 'Download JSON'.
- Rename the file 'client_secret.json' and move it to this directory.
## Running the Jupyter notebook
- Clone this project.
- Run VSCode on the cloned directory.
- Make sure that the 'Dev Containers' extension for VSCode is installed.
  - When you run VSCode on a project with a dev container, you should be prompted to 'Reopen in Container'.
  - Otherwise, launch the command pallette (Ctrl+Shift+P) and 'Rebuild Container'.
- Open the 'demo.ipynb' notebook and select the kernel in '/opt/conda/bin/python'.
- When you run the notebook, you will be prompted to authenticate through a web browser.
  - VSCode will launch a dialog, 'Do you want Code to open the external website?'. Click 'Open'.
  - Choose an account to continue to 'tasks'.
  - A dialog that says 'Google hasn't verified this app' will appear. Click 'Continue'.
  - 'GDrive Demo' wants access to your Google Account... Click 'Continue'.
