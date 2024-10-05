import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to fetch data from Google Spreadsheet
def get_spreadsheet_data(sheet_url):
    # Define the scope for accessing Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Provide the path to your credentials JSON file
    creds = ServiceAccountCredentials.from_json_keyfile_name('/content/credentials.json', scope)
    client = gspread.authorize(creds)

    # Open the Google spreadsheet by URL
    spreadsheet = client.open_by_url(sheet_url)
    sheet = spreadsheet.sheet1

    # Get all values from the sheet
    data = sheet.get_all_records()
    return data

# Function to send customized email with attachment
def send_custom_email_with_attachment(recipient_email, recipient_name, attachment_file):
    # Email content with the customized name
    subject = "Exploring Opportunities for a DevOps/Software Development Role"

    body = f"""
Dear {recipient_name},

I hope this email finds you well. My name is Tanush Banchhod, a recent graduate with a BTech in Computer Engineering, and I have gained hands-on experience as a DevOps intern at Hackveda. I am now actively seeking a role where I can leverage my skills in DevOps, CI/CD pipeline development, and software deployment.

During my internship, I developed a strong foundation in Jenkins, Git/GitHub, Python, and cloud technologies. Additionally, I have completed projects such as creating a stock market dashboard using Python, YFinance, and Alpha Vantage, as well as developing a job recommendation system utilizing NumPy, SVM, and cosine similarity.

I am confident that my blend of technical skills and passion for efficient deployment practices would make me a valuable addition to your team. I would greatly appreciate the opportunity to discuss how I can contribute to your organization's success.

Could we schedule a brief call to explore any current or future openings that align with my background?

Thank you for your time, and I look forward to your response.

Best regards,
Tanush Banchhod
  """

    # Set up the email
    sender_email = "[Your Email]"  # Replace with your email
    sender_password = "[App password]"      # Replace with your email password
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the resume file
    attachment_name = os.path.basename(attachment_file)
    with open(attachment_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {attachment_name}')
    msg.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.close()
        print(f"Email with resume sent to {recipient_name} at {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_name} at {recipient_email}: {str(e)}")

# Main function to fetch data and send emails
def main():
    # Google Spreadsheet URL
    sheet_url = '[Spreadsheet Link editable or view only depending upon your use]'

    # Fetch data from the spreadsheet
    data = get_spreadsheet_data(sheet_url)

    # Path to your resume (ensure it's in the same directory or provide full path)
    resume_file = "/content/TanushBanchhod.pdf"  # Replace with your actual resume file path

    # Loop through each record and send emails with attachment
    for record in data:
        recipient_email = record['Email Id']
        recipient_name = record['Name']
        send_custom_email_with_attachment(recipient_email, recipient_name, resume_file)

if __name__ == "__main__":
    main()