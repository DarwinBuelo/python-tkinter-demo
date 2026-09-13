import tkinter as tk
from tkinter import ttk


def events_demo(parent):
    frame = ttk.Frame(parent, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Events", font=("TkDefaultFont", 14, "bold")).pack(pady=(0, 12))

    message = tk.StringVar(value="Move the mouse over the box below.")
    ttk.Label(frame, textvariable=message, wraplength=450).pack(fill="x", pady=8)

    box = tk.Label(frame, text="INTERACTIVE BOX", bg="#ddeeff", width=40, height=8)
    box.pack(pady=8)

    # Each function below is an "event handler".
    # It runs when the matching event happens on the box.
    def on_enter(event):
        message.set("Mouse entered the box.")

    def on_leave(event):
        message.set("Mouse left the box.")

    def on_click(event):
        message.set(f"Mouse clicked at x={event.x}, y={event.y}.")

    def on_move(event):
        message.set(f"Mouse moved to x={event.x}, y={event.y}.")

    # bind() connects an event (a string in <...>) to a handler function
    box.bind("<Enter>", on_enter)
    box.bind("<Leave>", on_leave)
    box.bind("<Button-1>", on_click)
    box.bind("<Motion>", on_move)

    ttk.Label(frame, text="Some common events:").pack(anchor="w", pady=(12, 2))
    for event in ("<Button-1>   left mouse button pressed",
                  "<Motion>     mouse moved",
                  "<Enter>      mouse entered the widget",
                  "<Leave>      mouse left the widget",
                  "<KeyPress>   a key was pressed"):
        ttk.Label(frame, text=event).pack(anchor="w")

    # Keys can be captured too: type in this box and watch the message above.
    entry = ttk.Entry(frame)
    entry.pack(fill="x", pady=10)

    def on_key(event):
        key = event.char if event.char else event.keysym
        message.set(f"You pressed the key: {key}")

    entry.bind("<KeyPress>", on_key)

    return frame