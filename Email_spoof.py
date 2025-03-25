import smtplib

def send_email():
    server = smtplib.SMTP("smtp.example.com", 587)
    server.starttls()
    server.login("attacker@example.com", "password")

    subject = "Urgent: Security Update Required"
    body = "Your account has been compromised. Click here to secure it: http://fake-site.com"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("spoofed@example.com", "victim@example.com", msg)
    server.quit()

print("[INFO] Sending phishing email...")
send_email(
