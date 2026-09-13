"""
all_widgets.py
================

A one-page tour of every major Tkinter / ttk widget.

Run it with:  python3 all_widgets.py

There is one labeled frame (ttk.LabelFrame) per widget group, so you can
read the file top to bottom and see each widget explained next to its code.
"""

import tkinter as tk
from tkinter import colorchooser, filedialog, font as tkfont, messagebox, simpledialog, scrolledtext, ttk

root = tk.Tk()
root.title("All Tkinter Widgets")
root.geometry("760x900")

# Allow the window to be resized or maximized
root.resizable(True, True)
root.minsize(600, 400)

ttk.Label(root, text="Every major widget, one by one",
          font=("TkDefaultFont", 14, "bold")).pack(pady=10)

# --- Scrollable page -------------------------------------------------------
# The whole page is too tall to fit in one window, so we draw it on a
# Canvas that has a scrollbar. The "body" frame is the page itself; it is
# placed inside the canvas and can be scrolled up and down.
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

scroll_canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=scroll_canvas.yview)
scroll_canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
scroll_canvas.pack(side="left", fill="both", expand=True)

body = ttk.Frame(scroll_canvas)
body_window = scroll_canvas.create_window((0, 0), window=body, anchor="nw")


def on_body_resize(event):
    # Tell the canvas how tall the page is, so it knows how far to scroll.
    scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))


def on_canvas_resize(event):
    # Keep the page as wide as the window when it is resized.
    scroll_canvas.itemconfig(body_window, width=event.width)


body.bind("<Configure>", on_body_resize)
scroll_canvas.bind("<Configure>", on_canvas_resize)


def scroll_up(event):
    scroll_canvas.yview_scroll(-1, "units")


def scroll_down(event):
    scroll_canvas.yview_scroll(1, "units")


scroll_canvas.bind_all("<Button-4>", scroll_up)                          # mouse wheel up (Linux)
scroll_canvas.bind_all("<Button-5>", scroll_down)                        # mouse wheel down (Linux)
root.bind_all("<MouseWheel>",
              lambda e: scroll_canvas.yview_scroll(int(-e.delta / 120), "units"))  # Windows / Mac


# (1) Label & Message: show text -------------------------------------------
f = ttk.LabelFrame(body, text="(1) Label & Message")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="A Label just shows text.").pack(padx=10, pady=4)
tk.Label(f, text="A blue, bold, bigger Label.",
         fg="blue", font=("Helvetica", 12, "bold")).pack(padx=10, pady=4)
tk.Label(f, text="Labels can wrap long text over several lines if you "
                 "set wraplength, like this sentence right here.",
         wraplength=450, justify="left").pack(padx=10, pady=4)
tk.Message(f, text="A Message is like a Label, but it always wraps "
                   "its text and takes a width in characters. "
                   "Good for paragraphs.", width=55).pack(padx=10, pady=4)


# (2) Button: runs a function when clicked ---------------------------------
def button_clicked():
    messagebox.showinfo("Button", "You clicked a Button!")

f = ttk.LabelFrame(body, text="(2) Button")
f.pack(fill="x", padx=10, pady=5)
tk.Button(f, text="tk.Button", command=button_clicked).pack(padx=10, pady=4)
ttk.Button(f, text="ttk.Button (modern look)", command=button_clicked).pack(padx=10, pady=4)
ttk.Button(f, text="Disabled button", state="disabled").pack(padx=10, pady=4)


# (3) Entry, Spinbox, Combobox, OptionMenu: text input ---------------------
f = ttk.LabelFrame(body, text="(3) Entry, Spinbox, Combobox, OptionMenu")
f.pack(fill="x", padx=10, pady=5)

tk.Label(f, text="Entry: a one-line text box.").pack(anchor="w", padx=10, pady=(6, 2))
entry = tk.Entry(f)
entry.insert(0, "some text already here")
entry.pack(fill="x", padx=10)

tk.Label(f, text="Entry with show='*' hides typing (passwords).").pack(anchor="w", padx=10, pady=(6, 2))
tk.Entry(f, show="*").pack(fill="x", padx=10)

tk.Label(f, text="Spinbox: click the arrows to change a number.").pack(anchor="w", padx=10, pady=(6, 2))
tk.Spinbox(f, from_=0, to=10).pack(fill="x", padx=10)

tk.Label(f, text="Combobox: pick one item from a drop-down list.").pack(anchor="w", padx=10, pady=(6, 2))
ttk.Combobox(f, values=["Python", "Java", "Go", "Rust"]).pack(fill="x", padx=10)

tk.Label(f, text="OptionMenu: a small menu button that holds one choice.").pack(anchor="w", padx=10, pady=(6, 2))
language = tk.StringVar(value="Python")
tk.OptionMenu(f, language, "Python", "Java", "Go", "Rust").pack(fill="x", padx=10, pady=(0, 6))


# (4) Text & ScrolledText: multi-line text ---------------------------------
f = ttk.LabelFrame(body, text="(4) Text & ScrolledText")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="ScrolledText: a multi-line editor with a scrollbar built in.").pack(anchor="w", padx=10, pady=(6, 2))
st = scrolledtext.ScrolledText(f, height=4)
st.insert("1.0", "Line one\nLine two\n")
st.pack(fill="x", padx=10, pady=(0, 6))


# (5) Checkbutton & Radiobutton: choices -----------------------------------
f = ttk.LabelFrame(body, text="(5) Checkbutton & Radiobutton")
f.pack(fill="x", padx=10, pady=5)
likes = tk.BooleanVar(value=True)
tk.Checkbutton(f, text="Checkbutton: an on/off tick box.", variable=likes).pack(anchor="w", padx=10, pady=2)
tk.Checkbutton(f, text="Another Checkbutton, unticked.").pack(anchor="w", padx=10, pady=2)
tk.Label(f, text="Radiobuttons in a group: exactly one is chosen.").pack(anchor="w", padx=10, pady=(6, 2))
size = tk.StringVar(value="Small")
for option in ("Small", "Medium", "Large"):
    tk.Radiobutton(f, text=option, value=option, variable=size).pack(anchor="w", padx=10)


# (6) Listbox & Scrollbar --------------------------------------------------
f = ttk.LabelFrame(body, text="(6) Listbox")
f.pack(fill="x", padx=10, pady=5)
list_row = ttk.Frame(f)
list_row.pack(fill="both", expand=True, padx=10, pady=6)
listbox = tk.Listbox(list_row, height=4)
for position, item in enumerate(["Alpha", "Beta", "Gamma", "Delta"], 1):
    listbox.insert("end", f"{position}. {item}")
listbox.pack(side="left", fill="both", expand=True)
scroll = ttk.Scrollbar(list_row, orient="vertical", command=listbox.yview)
scroll.pack(side="right", fill="y")
listbox.configure(yscrollcommand=scroll.set)


# (7) Scale slider & Progressbar -------------------------------------------
f = ttk.LabelFrame(body, text="(7) Scale & Progressbar")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="Scale: drag the slider between 0 and 100.").pack(anchor="w", padx=10, pady=(6, 2))
tk.Scale(f, from_=0, to=100, orient="horizontal").pack(fill="x", padx=10)
tk.Label(f, text="Progressbar: shows how much of a task is done.").pack(anchor="w", padx=10, pady=(6, 2))
ttk.Progressbar(f, maximum=100, value=40).pack(fill="x", padx=10)
tk.Label(f, text="An animated progressbar is for 'something is happening'.").pack(anchor="w", padx=10, pady=(6, 2))
busy = ttk.Progressbar(f, mode="indeterminate")
busy.pack(fill="x", padx=10, pady=(0, 6))
busy.start(15)


# (8) Canvas: draw shapes --------------------------------------------------
f = ttk.LabelFrame(body, text="(8) Canvas")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="A Canvas is a blank area where we can draw shapes.").pack(anchor="w", padx=10, pady=(6, 2))
shapes = tk.Canvas(f, width=660, height=200, bg="white")
shapes.pack(fill="x", padx=10, pady=(0, 6))
shapes.create_line(20, 20, 150, 90, width=3, arrow="last")
shapes.create_rectangle(170, 20, 270, 110, fill="#bbddee")
shapes.create_oval(290, 20, 380, 110, fill="#ffccdd")
shapes.create_polygon(400, 110, 460, 30, 520, 110, fill="#ffffcc")
shapes.create_text(570, 70, text="Canvas!", font=("TkDefaultFont", 12, "bold"))


# (9) Frame, LabelFrame & Separator: containers ----------------------------
f = ttk.LabelFrame(body, text="(9) Frame, LabelFrame & Separator")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="Frames are containers that group widgets. "
                 "This whole page is a group of LabelFrames like this one.").pack(anchor="w", padx=10, pady=4)
inner = ttk.Frame(f, relief="groove", borderwidth=2)
inner.pack(fill="x", padx=10, pady=6)
for letter in ("A", "B", "C"):
    ttk.Label(inner, text=letter).pack(side="left", padx=8, pady=4)
tk.Label(f, text="A Separator is a simple line used to divide space.").pack(anchor="w", padx=10, pady=(6, 2))
ttk.Separator(f, orient="horizontal").pack(fill="x", padx=10, pady=(0, 6))


# (10) Treeview: data in a table -------------------------------------------
f = ttk.LabelFrame(body, text="(10) Treeview")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="Treeview shows data in a table with named columns.").pack(anchor="w", padx=10, pady=(6, 2))
tree_row = ttk.Frame(f)
tree_row.pack(fill="both", expand=True, padx=10, pady=(0, 6))
tree = ttk.Treeview(tree_row, columns=("name", "age", "city"), show="headings")
tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("city", text="City")
for person in (("Ada", 36, "London"), ("Grace", 45, "Virginia"), ("Alan", 41, "Manchester")):
    tree.insert("", "end", values=person)
tree.pack(side="left", fill="both", expand=True)
tree_scroll = ttk.Scrollbar(tree_row, orient="vertical", command=tree.yview)
tree_scroll.pack(side="right", fill="y")
tree.configure(yscrollcommand=tree_scroll.set)


# (11) Toplevel: a second window -------------------------------------------
def open_toplevel():
    top = tk.Toplevel(root)
    top.title("Toplevel")
    top.geometry("280x120")
    tk.Label(top, text="I am a separate window.").pack(pady=15)
    ttk.Button(top, text="Close", command=top.destroy).pack()

f = ttk.LabelFrame(body, text="(11) Toplevel")
f.pack(fill="x", padx=10, pady=5)
ttk.Button(f, text="Open a second window", command=open_toplevel).pack(padx=10, pady=6)


# (12) Menu bar ------------------------------------------------------------
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: messagebox.showinfo("Menu", "New chosen"))
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)


# (13) Built-in dialogs ----------------------------------------------------
f = ttk.LabelFrame(body, text="(13) Dialogs")
f.pack(fill="x", padx=10, pady=5)


def ask_question():
    answer = messagebox.askyesno("Question", "Do you like Tkinter?")
    messagebox.showinfo("Answer", f"Your answer was: {answer}")


def pick_file():
    name = filedialog.askopenfilename(title="Pick a file")
    if name:
        messagebox.showinfo("File", f"You chose:\n{name}")


def pick_folder():
    folder = filedialog.askdirectory(title="Pick a folder")
    if folder:
        messagebox.showinfo("Folder", f"You chose:\n{folder}")


def save_file():
    name = filedialog.asksaveasfilename(title="Save as", defaultextension=".txt")
    if name:
        messagebox.showinfo("Save", f"You would save to:\n{name}")


def pick_color():
    rgb, hexcode = colorchooser.askcolor(title="Pick a colour")
    if hexcode:
        messagebox.showinfo("Colour", f"RGB: {rgb}\nHex: {hexcode}")


def pick_font():
    try:
        chosen = tkfont.askfont(parent=root, title="Pick a font")
    except tk.TclError:
        messagebox.showerror("Font", "The font dialog is not supported here.")
        return
    if chosen:
        messagebox.showinfo("Font", f"Font chosen:\n{chosen}")


def ask_text():
    value = simpledialog.askstring("Input", "Enter some text:")
    if value is not None:
        messagebox.showinfo("Input", f"You entered:\n{value}")


buttons = [
    ("Messagebox (info)", lambda: messagebox.showinfo("Info", "Hello!")),
    ("Messagebox (yes/no)", ask_question),
    ("Open file dialog", pick_file),
    ("Choose a folder", pick_folder),
    ("Save file dialog", save_file),
    ("Colour chooser", pick_color),
    ("Font chooser", pick_font),
    ("Ask for text", ask_text),
]
for label, command in buttons:
    ttk.Button(f, text=label, command=command).pack(fill="x", padx=10, pady=2)


# (14) PanedWindow & Notebook: more containers ------------------------------
f = ttk.LabelFrame(body, text="(14) PanedWindow & Notebook")
f.pack(fill="x", padx=10, pady=5)
tk.Label(f, text="PanedWindow: two panes separated by a draggable divider.").pack(anchor="w", padx=10, pady=(6, 2))
paned = ttk.Panedwindow(f, orient="horizontal")
left_pane = ttk.Frame(paned, padding=20)
right_pane = ttk.Frame(paned, padding=20)
paned.add(left_pane)
paned.add(right_pane)
ttk.Label(left_pane, text="Left pane").pack()
ttk.Label(right_pane, text="Right pane").pack()
paned.pack(fill="x", padx=10)

tk.Label(f, text="Notebook: several pages, one tab at a time.").pack(anchor="w", padx=10, pady=(6, 2))
notebook = ttk.Notebook(f)
notebook.add(ttk.Frame(notebook), text="Tab 1")
notebook.add(ttk.Frame(notebook), text="Tab 2")
notebook.pack(fill="x", padx=10, pady=(0, 6))


# (15) Status bar at the bottom ---------------------------------------------
ttk.Label(root, text="Status: ready", relief="sunken", padding=(8, 4)).pack(side="bottom", fill="x")

root.mainloop()