import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, email, message):
    # Compose email message
    subject = "New Form Submission"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    # Create the MIMEText and MIMEMultipart objects
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain'))

    # Set email headers
    msg['From'] = email  # Use the provided email as the sender
    msg['Subject'] = subject

    # Determine recipient email dynamically based on the provided email
    recipient_email = determine_recipient_email(email)

    # Connect to the SMTP server (replace 'smtp.gmail.com' and 587 with your SMTP server details)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('gaurubro@gmail.com', '9986844986')  # Replace with your email and password
        server.sendmail(email, recipient_email, msg.as_string())

def determine_recipient_email(sender_email):
    # Customize this logic based on your application's requirements
    # For example, you can have predefined mappings or use specific conditions
    # In this example, we simply use the sender's email as the recipient's email
    return sender_email

# Example usage
send_email("John Doe", "john@example.com", "This is a test message")
