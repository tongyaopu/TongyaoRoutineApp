import tkinter as tk

appName = "Tongyao morning routine"


def setRoutine(event):
    print("bring you to the set routine interface")

    window_setRoutine = tk.Tk()
    window_setRoutine.title(appName)
    window_setRoutine.geometry("300x200")

    mybutton = tk.Button(window_setRoutine, text="Setting tasks for today")
    mybutton.grid(column=1, row=1)
    mybutton.bind("<Button-1>", setRoutine)


# label1=tk.Label(text="?")
# label1.grid(column=1,row=1)

window_setRoutine = tk.Tk()
window_setRoutine.title(appName)
window_setRoutine.geometry("300x200")

mybutton = tk.Button(window_setRoutine, text="Setting tasks for today")
mybutton.grid(column=1, row=1)
mybutton.bind("<Button-1>", setRoutine)


window_setRoutine.mainloop()
