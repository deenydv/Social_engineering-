import smtplib
from email.mime.text import MIMEText

def send_fake_job_email():
    msg = MIMEText("Congratulations! You've been selected for an interview. Download the attached file and fill out your details.")
    msg["Subject"] = "Job Interview Invitation"
    msg["From"] = "recruitment@example.com"
    msg["To"] = "victim@example.com"

    server = smtplib.SMTP("smtp.example.com", 587)
    server.starttls()
    server.login("attacker@example.com", "password")
    server.sendmail("recruitment@example.com", "victim@example.com", msg.as_string())
    server.quit()

print("[INFO] Sending fake job phishing email...")
send_fake_job_email(
