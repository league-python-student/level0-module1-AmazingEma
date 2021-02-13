from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
bday = simpledialog.askinteger(title="", prompt="what is your B-DAY in mmdd format")

if bday == 212:
    print("happy bday")

else:
    print('have a very merry UNbirthday')
