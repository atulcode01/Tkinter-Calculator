from tkinter import *

#creating on click function 
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(event_var.get()))
            event_var.set(result)
        except Exception as e:
            event_var.set("Error")
    elif text == "C":
        event_var.set("")
    else:
        event_var.set(event_var.get() + text)


# creating window
window = Tk()
window.geometry("360x480")
window.title("Atul's Calculator")
window.resizable(width = False, height = False)
window.configure(bg = "#0d0d0d")

#entry wigid for user input 
event_var = StringVar()
event = Entry(window, textvariable=event_var, font="Arial", bd=2, insertwidth=4, width=14, borderwidth=10, relief="ridge" )
event.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

#buttons creation 
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Adding buttons to the window
for (text, row, col) in buttons:
    button = Button(window, text=text, font="Arial 15 bold", bg="#636e72", fg="white", height=2, width=5)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)

#run the window 
window.mainloop()