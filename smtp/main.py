import smtplib 
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


subject = "Daily Quote:"
my_email = "dennisopokuamponsah86@gmail.com"
password = "hlcztzarsqjkbxge"

recipient_emails = ["dennisopokuamponsah86@gmail.com","adusarkodieirene31@gmail.com", "anyirageorgeatsu@yahoo.com"]

now = dt.datetime.now()
weekday = now.weekday()

if weekday in range(7):
    # Read the quotes from the quote.txt
    with open("smtp/quote.txt", "r", encoding="utf-8") as daily_quote:
        all_quotes = daily_quote.readlines()
        quote = random.choice(all_quotes)
        
        #Load the html templates from the file
    try:
        with open("smtp/daily_quote.html", "r", encoding="utf-8") as file:
            template = file.read()
            
        # Replace the placeholders with actual quote
            html_message = template.replace("{{quote}}", quote)
            
    except Exception as e:
        print(f"Error loading the HTML template: {e}")
        html_message = quote
    try:
        # Create a multipart message
        with smtplib.SMTP( "smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            #message = f"Subject:{subject}\n\n{quote}".encode("utf-8")
            
            for recipient_email in recipient_emails:
                message = MIMEMultipart()
                message["from"] = my_email
                message['To'] = recipient_email
                message["subject"] = subject

            #Create an HTML version of the email
                html_body = MIMEText(html_message, "html", "utf-8")
                message.attach(html_body)
        
            # Send the email to the specified recipient
                connection.sendmail(
                from_addr=my_email, 
                to_addrs=recipient_email, 
                msg=message.as_string()
            )
                
    except Exception as e:
            print(f"An error occurred while sending the email: {e}")

    else:
        print("Email sent successfully!")