import tkinter as tk
from tkinter import ttk


def canvas_demo(parent):
    frame = ttk.Frame(parent, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Canvas Drawing", font=("TkDefaultFont", 14, "bold")).pack(pady=(0, 12))

    ttk.Label(frame, text="A Canvas is a blank area where we can draw shapes.").pack(anchor="w")

    canvas = tk.Canvas(frame, width=650, height=380, bg="white")
    canvas.pack(expand=True, fill="both", pady=8)

    # line: two points, (x1, y1) and (x2, y2)
    canvas.create_line(20, 20, 200, 100, width=3, arrow="last")

    # rectangle: top-left corner, then bottom-right corner
    canvas.create_rectangle(230, 20, 380, 120, fill="#bbddee")

    # oval: drawn inside the box that touches its edges
    canvas.create_oval(410, 20, 530, 120, fill="#ffccdd")

    # polygon: a shape made from any number of points
    canvas.create_polygon(20, 160, 130, 250, 20, 340, fill="#ffffcc")

    # arc: a slice of an oval
    canvas.create_arc(540, 160, 650, 280, start=0, extent=90, style="pieslice", fill="#ccffcc")

    # text: writes words on the canvas
    canvas.create_text(280, 200, text="Hello from the Canvas!",
                       font=("TkDefaultFont", 16, "bold"))

    # a dashed line
    canvas.create_line(230, 300, 600, 300, dash=(5, 5), width=2)

    return frame