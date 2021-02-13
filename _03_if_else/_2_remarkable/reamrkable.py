from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw ()
Name = simpledialog.askstring(title="", prompt="what is your name")

if Name.lower() == "ellie":
    print("something remarkleble about you is.... you are allergic to most nuts")
elif Name.lower() == "caris":
    print("something remarkable about you is.....you can draw")
elif Name.lower() == "christopher":
    print('something remarkable about you is..... you breathe')
elif Name.lower() == "daniel":
    print("you can code")
else:
    print("I dont know you")