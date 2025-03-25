import qrcode

phishing_url = "http://fake-login.com"
qr = qrcode.make(phishing_url)
qr.save("phishing_qr.png")

print("[INFO] QR code saved as 'phishing_qr.png'"
