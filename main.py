import tkinter as tk
from tkinter import ttk

from demos.widgets import widgets_demo
from demos.layout import layout_demo
from demos.events import events_demo
from demos.canvas import canvas_demo

# Create the main window
root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("800x600")

# Allow the window to be resized or maximized
root.resizable(True, True)
root.minsize(600, 400)

# A notebook shows one tab at a time
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Each demo is one page (tab) in the notebook
notebook.add(widgets_demo(notebook), text="Widgets")
notebook.add(layout_demo(notebook), text="Layout")
notebook.add(events_demo(notebook), text="Events")
notebook.add(canvas_demo(notebook), text="Canvas")

# Start the program (this must always come last)
root.mainloop()