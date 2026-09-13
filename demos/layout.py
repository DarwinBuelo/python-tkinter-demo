from tkinter import ttk


def layout_demo(parent):
    frame = ttk.Frame(parent, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Layout Managers",
              font=("TkDefaultFont", 14, "bold")).pack(pady=(0, 12))

    # --- pack: stack widgets using a side (left, right, top, bottom) ------
    ttk.Label(frame, text="pack with side='left' puts widgets in a row:").pack(anchor="w", pady=(8, 2))
    row = ttk.Frame(frame)
    row.pack(fill="x")
    for i in range(3):
        ttk.Label(row, text=f"one {i}", width=10).pack(side="left", padx=4)

    # --- grid: place widgets in rows and columns --------------------------
    ttk.Label(frame, text="grid uses a row number and a column number:").pack(anchor="w", pady=(8, 2))
    table = ttk.Frame(frame)
    table.pack()
    for r in range(2):
        for c in range(2):
            ttk.Button(table, text=f"{r},{c}").grid(row=r, column=c, padx=4, pady=4)

    # --- place: put a widget at an exact position --------------------------
    ttk.Label(frame, text="place gives a widget an exact position:").pack(anchor="w", pady=(8, 2))
    box = ttk.Frame(frame, width=250, height=70)
    box.pack()
    ttk.Label(box, text="top-left", background="#ffffcc").place(x=5, y=5)
    ttk.Label(box, text="bottom-right", background="#ccffff").place(relx=1, rely=1, anchor="se")

    return frame