from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw ()
password = simpledialog.askstring(title="", prompt="set a password")

message = simpledialog.askstring(title="", prompt="what is your secret?")

print("next user")

Name = simpledialog.askstring(title="", prompt="write the password to see what the secret is")

if Name.lower() == password:
    print(message)
else:
    print("INTRUDER!!!")