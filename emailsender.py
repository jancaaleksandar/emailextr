import smtplib
import csv

def send_email(input_file, sender_email, sender_password, email_subject, email_body):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        with open(input_file, newline='') as file:
            email_reader = csv.reader(file)
            for row in email_reader:
                receiver_email = row[0]
                server.sendmail(sender_email, receiver_email, f'Subject: {email_subject}\n\n{email_body}')

# Example usage
input_file = 'emails.csv'
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'  # Be cautious with your password
email_subject = 'Your Email Subject'
email_body = 'Your email body.'

send_email(input_file, sender_email, sender_password, email_subject, email_body)
