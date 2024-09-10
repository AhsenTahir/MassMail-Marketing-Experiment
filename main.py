import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import starting_roll_number , ending_roll_number

# Email account credentials (sender's email and password)
sender_email = "your_email@gmail.com"
password = "your_password"

# SMTP server setup (for Gmail, you can change this if using another email service)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email content
subject = "Check this out! You don't want to miss it!"
body = """
Hey there,

You won't believe what I found! Click on the link below to find out more.

[]

Best regards,
ClickBait Team
"""

# Email function
def send_email(receiver_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, password)  # Login to the email account
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        print(f"Email sent to {receiver_email}")
        server.quit()
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {str(e)}")

# Function to send emails to a range of students
def send_bulk_emails(start_roll, end_roll):
    # Extract the prefix (e.g., 'k2306') and the starting number (e.g., 06) from the roll number
    prefix = start_roll[:-3]  # Assuming the last three digits are the roll number
    start_number = int(start_roll[-3:])
    end_number = int(end_roll[-3:])

    for i in range(start_number, end_number + 1):
        # Generate the email address
        student_email = f"{prefix}{str(i).zfill(3)}@nu.edu.pk"
        send_email(student_email)
        time.sleep(10)  # Delay for 10 seconds to avoid sending too many emails at once

if __name__ == "__main__":
    # Define the starting and ending roll numbers
    start_roll = starting_roll_number
    end_roll = ending_roll_number
    
    # Call the function to start sending emails
    send_bulk_emails(start_roll, end_roll)
