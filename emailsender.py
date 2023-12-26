import smtplib
import csv

def send_email(input_file, sender_email, sender_password, email_subject, email_template):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        with open(input_file, newline='', encoding='utf-8') as file:
            email_reader = csv.reader(file)
            for row in email_reader:
                receiver_email, name = row
                personalized_email_body = email_template.replace("[name]", name)
                full_email = f"Subject: {email_subject}\n\n{personalized_email_body}"
                server.sendmail(sender_email, receiver_email, full_email.encode('utf-8'))

# Email Template
email_template = """
Αγαπητέ, [name]

Καλησπέρα ονομαζόμαστε SoftSight, και είμαστε ειδικοί στη δημιουργία και βελτίωση ιστοσελίδων. Μετά από μία ενδελεχή ανάλυση της ιστοσελίδας σας, παρατηρήσαμε κάποιες ευκαιρίες για βελτίωση που μπορούν να αυξήσουν την εμπειρία των πελατών σας και να ενισχύσουν την εταιρική σας εικόνα.

[...rest of the message...]

Με εκτίμηση,
SoftSight
"""

# Example usage
input_file = 'emails.csv'
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'  # Replace with your actual password
email_subject = 'Your Email Subject'

send_email(input_file, sender_email, sender_password, email_subject, email_template)
