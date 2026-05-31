import tkinter as tk
from tkinter import ttk
from time import strftime
#Update Clock Function
def update_clock():
    current_time = strftime("%I:%M:%S %p")
    current_date = strftime("%d %B %Y")
    current_day = strftime("%A")
    time_label.configure(text=current_time)
    date_label.configure(text=current_date)
    day_label.configure(text=current_day)
    root.after(1000, update_clock)
#Main Window
root = tk.Tk()
root.title(" Digital Clock ")
root.geometry("700x400")
root.minsize(600, 350)
#Heading Labels
heading = ttk.Label(root, text="Digital Clock ",font=("Arial", 24,"bold"))
heading.pack(pady=20)
time_label = ttk.Label(root, font=("Arial", 48,"bold"))
time_label.pack(pady=10)
date_label = ttk.Label(root, font=("Arial", 20))
date_label.pack(pady=10)
day_label = ttk.Label(root, font=("Arial", 22))
day_label.pack()
exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)
status=ttk.Label(root,text="Running...",relief="sunken",anchor="w")
status.pack(side="bottom",fill="x")
update_clock()
root.mainloop()
