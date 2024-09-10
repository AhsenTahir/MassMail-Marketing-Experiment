import smtplib
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import starting_roll_number, ending_roll_number

# Email account credentials (sender's email and password)
sender_email = "mhm@gmail.com"
password = "skibidi"

# SMTP server setup (for Gmail, you can change this if using another email service)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email content
subject = "Discover Microsoft Learn Resources – A New Way to Boost Your Skills"
greetings = ["Hi there,", "Hello,", "Greetings,", "Hey,", "Salutations,"]

# Function to create a unique email body
def create_email_body():
    greeting = random.choice(greetings)  # Randomly select a greeting
    body = f"""{greeting}

We've built a tool to make it easier for you to find Microsoft Learn resources, including learning paths, modules, and documentation. Whether you're improving your tech skills or exploring new topics, this platform can help.

Use this website:

-Access free, official resources from Microsoft Learn.
-Explore learning paths and documentation on topics like Azure, AI, DevOps, and more.
-Benefit from an all-in-one search for quick and easy access to the material you need.
-You can check it out here: Visit the Website(https://microsoft-earn.vercel.app/)

By using this site, you're also supporting my journey to become a Microsoft Learn Student Ambassador, and I truly appreciate your help!

Thank you for your support, and feel free to reach out if you have any questions or feedback.

Best regards,
Microsoft Learn Student Ambassador
"""
    return body

# Email function
def send_email(receiver_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add body to the email
    body = create_email_body()  # Get the unique email body
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
        time.sleep(random.randint(1,3))  # Delay for 10 seconds to avoid sending too many emails at once
        if(i==50):
            time.sleep(random.randint(40, 80))

if __name__ == "__main__":
    # Define the starting and ending roll numbers
    start_roll = starting_roll_number
    end_roll = ending_roll_number
    
    # Call the function to start sending emails
    send_bulk_emails(start_roll, end_roll)
