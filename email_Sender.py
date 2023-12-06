from email.message import EmailMessage
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


context = ssl.create_default_context() 
def send_otp_email(email,verification_code):
    devhire_email = "devhirecontact@gmail.com"
    devhire_email_password = "fazxvkyfnonkvnsj"
    mail_content = MIMEMultipart("alternative")
    mail_content['Subject'] = 'Project-Heimer One Time Verification'
    mail_content['From'] = devhire_email
    mail_content['To'] = email
    text = f"Your Verification Code For Project-Heimer Is : {verification_code}"
    # HTML content for email template
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Verification Email</title>
        </head>
        <body>
            <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
                <div style="margin:50px auto;width:80%;padding:20px 0">
                    <div style="color:white; text-align:center; background: -webkit-linear-gradient(0deg,#39b1b2 ,#000000 100%);">
                        <p style="font-size:15px;color: white;">Hello,</p>
                        <p>Welcome To Project-Heimer. Use this code to complete your accounts verification process.</p>
                        <p>Remember, Never share this code with anyone.</p>
                        <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{verification_code}</h2>
                        <p style="font-size:15px;">Regards,<br />Team Project-Heimer</p>
                    </div>
                    <hr style="border:none;border-top:5px solid #eee" />
                    <div style="float:left;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
                        <p>Contact Us</p>
                        <p><a href="mailto:k213218@nu.edu.pk">k213218@nu.edu.pk</a>.</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
        
    """
    part1 = MIMEText(text ,'plain')
    part2 = MIMEText(html,'html')
    mail_content.attach(part1)
    mail_content.attach(part2)
    
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
        server.login(devhire_email,devhire_email_password)
        server.send_message(mail_content)