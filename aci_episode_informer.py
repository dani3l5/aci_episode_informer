import praw
import time
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Edit reddit info here
reddit = praw.Reddit(client_id = 'YOUR_CLIENT_ID',
                     client_secret = 'YOUR_CLIENT_SECRET',
                     username = 'YOUR_USERNAME',
                     password = 'YOUR_PASSWORD',
                     user_agent = 'CAN_BE_LITERALLY_ANYTHING_JUST_PROVIDE_ONE')

subreddit = reddit.subreddit('aircrashinvestigation')

new_episode = False
running_time = 0

try:
    while True:
        new_post = subreddit.new(limit=1)
        for submission in new_post:
			#Edit Episode Number Here
            if 'EPISODE_NUMBER' in submission.title:
                new_episode = True
        if new_episode:
            break
        time.sleep(10)
        running_time += 10
        os.system('clear')
        print(str(running_time) + "s")
except KeyboardInterrupt:
    exit(1)

#For 'host', choose the smtp addresses of your email provider (you may need to check online)
#For, 'port', it's usually 587 (not a string), but sometimes email providers use a different port, so please do check online
s = smtplib.SMTP(host="IF YOU USE: Outlook: 'smtp-mail.outlook.com', Gmail: 'smtp.gmail.com', Yahoo: 'plus.smtp.mail.yahoo.com'",
				 port=587)
s.starttls()
s.login('YOUR_EMAIL_ADDRESS', 'YOUR_EMAIL_PASSWORD')

msg = MIMEMultipart()

message = "EMAIL_MESSAGE_HERE"

msg["From"] = 'YOUR_EMAIL_ADDRESS'
msg["To"] = 'YOUR_EMAIL_ADDRESS'
msg["Subject"] = 'EMAIL_TITLE'

msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)

print("Post found and email sent!")
