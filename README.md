# Tkinter Demo

A small collection of programs for learning **Tkinter**, Python's built-in
graphical user interface (GUI) toolkit.

No third-party packages are needed — everything uses the Python standard library.

## Requirements

- Python 3.6 or newer
- `tkinter` (built into Python; see [requirements.txt](requirements.txt)
  if it is missing on your system)

## Programs

| File              | What it shows                                                        |
| ----------------- | -------------------------------------------------------------------- |
| `app.py`          | The most basic GUI: a window, a label, and a Quit button.            |
| `main.py`         | A tabbed (Notebook) app with four pages: widgets, layout, events,    |
|                   | and canvas drawing.                                                  |
| `all_widgets.py`  | A one-page, scrollable tour of every major widget (buttons, text,    |
|                   | lists, tables, charts, dialogs, and more), each with a comment.      |

### The demo pages inside `main.py`

- **Widgets** (`demos/widgets.py`) — Label, Entry, Button, Checkbutton,
  Radiobutton, Combobox, Scale, Progressbar, Listbox.
- **Layout** (`demos/layout.py`) — the three layout managers:
  `pack`, `grid`, and `place`.
- **Events** (`demos/events.py`) — how `bind()` wires mouse and keyboard
  events to handler functions.
- **Canvas** (`demos/canvas.py`) — drawing shapes: line, rectangle, oval,
  polygon, arc, text.

## Running

Run any program from the project folder:

```bash
python3 app.py
python3 main.py
python3 all_widgets.py
```

## Tips for using this as a teaching tool

- Read the files top to bottom — all of them are written to be read in order.
- `all_widgets.py` is the fullest tour: each widget has a one-line comment
  explaining what it does, and the whole page scrolls.
- Try removing lines and re-running: seeing what breaks (or goes away) is
  the fastest way to learn what each line does.