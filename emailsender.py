def sendEmail(input_file):
    with open(input_file, 'r') as file:
        emails = file.readlines()
   
    for email in emails:
        return email