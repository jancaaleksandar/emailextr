import json
import csv

def extract_info(input_file, output_file):
    with open(input_file, 'r') as file:
        information = json.load(file)

    name_email = []

    for info in information:
        name = info.get('title')

        # Check if name is found
        if name:
            contact_details = info.get('contactDetails', {})
            emails = contact_details.get('emails', [])

            # Write only if there is at least one email
            if emails:
                for email in emails:
                    name_email.append([name, email])

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])  # Writing the header
        writer.writerows(name_email)

input_file = 'info.json'
output_file = 'emails.csv'
extract_info(input_file, output_file)
