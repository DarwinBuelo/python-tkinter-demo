import tkinter as tk

root = tk.Tk()
root.title("Hello World")
root.geometry("300x200")

# Allow the window to be resized or maximized
root.resizable(True, True)

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()

root.mainloop()