import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from pathlib import Path
from email_body import create_email_body



# Function to send email
def send_email(sender_email, sender_password, recipients, subject, template_body):
    smtp_server = 'smtp.mail.yahoo.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    for recipient in recipients:

        name = recipient['name']
        email = recipient['email']
        
        # Replace placeholder with the recipient's name
        body = template_body.replace("[NAME]", name)
        
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        
        # Attach HTML body
        msg.attach(MIMEText(body, 'html'))

        # # Attach images
        # for file_name in os.listdir(folder_path):
        #     if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        #         image_path = os.path.join(folder_path, file_name)
        #         image_cid = file_name.split('.')[0]
        #         with open(image_path, 'rb') as img_file:
        #             img_data = img_file.read()
        #         img = MIMEImage(img_data, name=file_name)
        #         img.add_header('Content-ID', f'<{image_cid}>')
        #         msg.attach(img)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, email, text)

    server.quit()

if __name__ == "__main__":
    # folder_to_attach = "/home/caleb/Code/Email_List/agency_photos"
    
    sender_email = "schilling.caleb@yahoo.com"
    sender_password = "mxqtxjgpxblbfmii"


    # List of recipients with names and emails
    recipients = [
        {"name": "Caleb", "email": "cschilli98@gmail.com"},
        {"name": "Alecia", "email": "simpson.alecia@gmail.com"},
        {"name": "Account", "email": "account_logins@yahoo.com"}

       
    ]

    subject = "Don’t Miss Out on This Marketable Family for Your Campaigns!"
    
    # Create email body
    body = create_email_body()
    
    # Send the emails with inline images
    send_email(sender_email, sender_password, recipients, subject, body)
