from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from io import StringIO
from email_body import create_email_body

app = Flask(__name__)

# Function to read recipients from CSV file
def read_recipients_from_csv(file):
    recipients = []
    file.seek(0)  # Make sure we're at the start of the file
    csv_reader = csv.DictReader(StringIO(file.read().decode('utf-8')))
    for row in csv_reader:
        recipients.append({"name": row['name'], "email": row['email']})
    return recipients

# Function to send email
def send_email(sender_email, sender_password, recipient, subject, body_template):
    smtp_server = 'smtp.mail.yahoo.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient['email']
    msg['Subject'] = subject

    # Replace the placeholder with the recipient's name
    body = body_template.replace("[NAME]", recipient['name'])

    # Attach HTML body
    msg.attach(MIMEText(body, 'html'))

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, recipient['email'], text)
    server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    sender_email = request.form['sender_email']
    sender_password = request.form['sender_password']
    subject = request.form['subject']
    body_template = create_email_body()

    # Path to CSV file
    csv_file = request.files['file']
    
    # Read recipients from CSV file
    recipients = read_recipients_from_csv(csv_file)
    
    # Send email to each recipient
    for recipient in recipients:
        send_email(sender_email, sender_password, recipient, subject, body_template)
    
    # Pass success message to template
    return render_template('index.html', success_message='Emails successfully sent!')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
