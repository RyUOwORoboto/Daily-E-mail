# import smtplib
# import schedule
# import time
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from datetime import datetime

# # Email details
# SMTP_SERVER = 'smtp.your-email-provider.com'
# SMTP_PORT = 587
# SENDER_EMAIL = 'your-email@example.com'
# SENDER_PASSWORD = 'your-email-password'
# RECIPIENT_EMAIL = 'recipient-email@example.com'
# SUBJECT = 'Daily Report'

# # Function to create the email content
# def create_email_content():
#     now = datetime.now()
#     current_time = now.strftime("%Y-%m-%d %H:%M:%S")
#     body = f"Hello,\n\nThis is your daily report for {current_time}.\n\nBest regards,\nYour Automated System"

#     # Attach any files if necessary
#     filename = "path/to/your/report.pdf"  # Example file attachment
#     attachment = open(filename, "rb")

#     msg = MIMEMultipart()
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = RECIPIENT_EMAIL
#     msg['Subject'] = SUBJECT

#     msg.attach(MIMEText(body, 'plain'))

#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(attachment.read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', f'attachment; filename={filename}')

#     msg.attach(part)
#     attachment.close()

#     return msg.as_string()

# # Function to send the email
# def send_email():
#     try:
#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()
#         server.login(SENDER_EMAIL, SENDER_PASSWORD)

#         email_content = create_email_content()
#         server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, email_content)
#         server.quit()
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")

# # Schedule the task
# schedule.every().day.at("09:00").do(send_email)  # Schedule for 9 AM every day

# # Main loop to keep the script running and checking for the scheduled task
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Check every minute
