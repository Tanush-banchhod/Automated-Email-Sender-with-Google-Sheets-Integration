# Automated Email Sender with Google Sheets Integration

This project automates the process of sending personalized emails to multiple recipients. The recipients' names and email addresses are fetched from a Google Spreadsheet, and each email is customized with the recipient's name. You can also attach files like resumes to the emails.

## Features

- Send personalized emails to multiple recipients
- Fetch names and email addresses from a Google Spreadsheet
- Attach files (e.g., resumes) to the emails
- Uses Gmail for sending emails

## Prerequisites

Before you run this script, ensure you have the following:

1. **Google Account** with access to Gmail and Google Sheets.
2. **Python 3.x** installed on your system.
3. A **Google Cloud Project** with the Google Sheets API enabled.
4. A **service account** and the `credentials.json` file.

## Step-by-Step Guide

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/automated-email-sender.git
cd automated-email-sender
``` 

### 2. Install Required Libraries

Run the following command to install all required Python packages:

```bash
pip install -r requirements.txt
```
The requirements.txt file includes the following packages:

- gspread for accessing Google Sheets.
- oauth2client for handling Google authentication.
- smtplib and email for sending emails via Gmail.

### 3. Set Up Google Cloud API Credentials
1. Go to the Google Cloud Console.
2. Create a new project or use an existing one.
3. Navigate to APIs & Services > Library, and enable the Google Sheets API.
4. Go to APIs & Services > Credentials, and click Create Credentials > Service Account.
5. After creating the service account, click Add Key > Create New Key and select JSON. This will download a credentials.json file.
6. Save this credentials.json file in the root directory of this project.
7. Open the Google Spreadsheet that contains your recipient data, and share it with the service account email (found in credentials.json).

   
###4. Enable Gmail App Password
To send emails using Gmail, you must use an App Password if Two-Factor Authentication (2FA) is enabled. Follow these steps:

1. Go to your Google Account.
2. Under Security, enable 2-Step Verification (if not already enabled).
3. Generate an App Password here.
4. Use this App Password in the Python script to authenticate sending emails.
   
###5. Customize the Script
1. Open the email_sender.py script.
2. Replace the placeholder Gmail credentials with your own Gmail address and App Password:
```bash
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
```
3. Update the Google Spreadsheet URL in the script to the one you are using.

### 6. Attach a Resume (Optional)
If you want to attach a file, such as a resume, place the file in the project directory and specify the filename in the script under the send_custom_email function.

### 7. Run the Script
To execute the script and send emails, run the following command:
```bash
python email_sender.py
```

###Example Spreadsheet Structure
Your Google Spreadsheet should contain two columns with the following headers:

Name: The name of the recipient (e.g., "Ayushi").
Email Id: The email address of the recipient (e.g., "ayushi@example.com").

| Name | Email |
|---|---|
| Ayushi | ayushi@example.com |
| Rahul | rahul@example.com |
| Sita | sita@example.com |


### 8. Troubleshooting
1. Authentication Error: Make sure that your service account has access to the Google Spreadsheet, and that the credentials.json file is in the correct directory.
2. App Password Issues: If your App Password is not working, ensure that Two-Factor Authentication (2FA) is enabled on your Google account.


---

### Files in the Repository:

- `email_sender.py`: The main Python script for sending customized emails.
- `requirements.txt`: List of Python dependencies for the project.
- `credentials.json`: Your Google Cloud API credentials file (not uploaded to GitHub for security reasons, but instructions are provided).
- `README.md`: Documentation for the project.

---

### How the README.md is Structured:

1. **Introduction**: Brief overview of the project and its features.
2. **Prerequisites**: Lists what the user needs before running the script (Python, Gmail account, Google API credentials).
3. **Step-by-Step Guide**: Easy-to-follow instructions for setting up the script and running it. This section covers everything from cloning the repo, installing libraries, setting up Google Cloud credentials, using Gmail App Passwords, and running the script.
4. **Spreadsheet Structure**: Simple example of how the Google Spreadsheet should be formatted.
5. **Troubleshooting**: Common issues and solutions.
6. **License**: Specifies the project license.

By following these instructions, even a beginner will be able to set up and execute the email-sending script without much trouble. Let me know if you need any adjustments or additional information!
