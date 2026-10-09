from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

now = datetime.now()
print(now)

my_time = datetime.now()# + timedelta(hours=8)
print(my_time)

# command
def snooze():
    messagebox.showinfo = ("Information", "Alarm snoozed")
def stop():
    messagebox.showinfo = ("Information", "Alarm stopped")    
    
# Set up the main application window
root = tk.Tk()
root.geometry("300x200")

# Button to trigger the pop-up
button1 = tk.Button(root, text = "Snooze",command = snooze)
button2 = tk.Button(root, text = "Stop", command = stop)

root.mainloop()

if now == my_time:
    button1.pack(pady = 20)
    button2.pack(pady = 40)

########################    
# import tkinter as tk
# from tkinter import messagebox
# 
# def show_popup():
#     # Syntax: showinfo("Window Title", "Your message goes here")
#     messagebox.showinfo("Information", "This is a standard Tkinter pop-up!")
# 
# # Set up the main application window
# root = tk.Tk()
# root.geometry("300x200")
# 
# # Button to trigger the pop-up
# btn = tk.Button(root, text="Click Me", command=show_popup)
# btn.pack(pady=10)
# 
# root.mainloop()

    
