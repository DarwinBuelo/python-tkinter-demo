import tkinter as tk
from tkinter import ttk


def widgets_demo(parent):
    # A frame is a container that groups other widgets together
    frame = ttk.Frame(parent, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Common Widgets",
              font=("TkDefaultFont", 14, "bold")).pack(pady=(0, 12))

    # --- Label: shows text ------------------------------------------------
    ttk.Label(frame, text="This is a Label. Labels only show text.").pack(pady=4)

    # --- Entry: a text box where the user can type ------------------------
    ttk.Label(frame, text="Entry (click and type):").pack(anchor="w", pady=(8, 2))
    entry = ttk.Entry(frame)
    entry.pack(fill="x")

    # --- Button: runs a function when clicked -----------------------------
    ttk.Label(frame, text="Button (click it):").pack(anchor="w", pady=(8, 2))
    clicked = tk.StringVar(value="The button has not been clicked yet.")

    def on_click():
        clicked.set("The button WAS clicked!")

    ttk.Button(frame, text="Click me", command=on_click).pack()
    ttk.Label(frame, textvariable=clicked).pack(pady=4)

    # --- Checkbutton: a box you can tick on or off ------------------------
    ttk.Label(frame, text="Checkbutton (tick it on or off):").pack(anchor="w", pady=(8, 2))
    checked = tk.BooleanVar(value=True)
    ttk.Checkbutton(frame, text="I like Tkinter", variable=checked).pack(anchor="w")

    # --- Radiobutton: pick one option from a group ------------------------
    ttk.Label(frame, text="Radiobutton (pick one option):").pack(anchor="w", pady=(8, 2))
    size = tk.StringVar(value="Small")
    ttk.Radiobutton(frame, text="Small", value="Small", variable=size).pack(anchor="w")
    ttk.Radiobutton(frame, text="Medium", value="Medium", variable=size).pack(anchor="w")
    ttk.Radiobutton(frame, text="Large", value="Large", variable=size).pack(anchor="w")

    # --- Combobox: a drop-down list --------------------------------------
    ttk.Label(frame, text="Combobox (choose from a list):").pack(anchor="w", pady=(8, 2))
    ttk.Combobox(frame, values=["Red", "Green", "Blue"]).pack(fill="x")

    # --- Scale: a draggable slider ----------------------------------------
    ttk.Label(frame, text="Scale (drag the slider):").pack(anchor="w", pady=(8, 2))
    ttk.Scale(frame, from_=0, to=100).pack(fill="x")

    # --- Progressbar: shows how far a task has come -----------------------
    ttk.Label(frame, text="Progressbar (shows progress):").pack(anchor="w", pady=(8, 2))
    ttk.Progressbar(frame, maximum=100, value=40).pack(fill="x")

    # --- Listbox: a scrollable list of items ------------------------------
    ttk.Label(frame, text="Listbox (a list of items):").pack(anchor="w", pady=(8, 2))
    listbox = tk.Listbox(frame, height=4)
    for item in ("apple", "banana", "cherry", "date"):
        listbox.insert("end", item)
    listbox.pack(fill="x")

    return frame