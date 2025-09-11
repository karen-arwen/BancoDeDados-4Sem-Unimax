import tkinter as tk
from tkinter import ttk

def apply_theme(root: tk.Tk | tk.Toplevel):
    style = ttk.Style(root)
    # Tente "clam" para visuais limpos e consistentes:
    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))
    style.configure("Subtle.TLabel", foreground="#666")
    style.configure("TButton", padding=6)
    style.configure("Card.TFrame", relief="ridge", borderwidth=1)

def make_grid_responsive(widget: tk.Widget, rows: int, cols: int):
    for r in range(rows):
        widget.grid_rowconfigure(r, weight=1 if r == rows - 1 else 0)
    for c in range(cols):
        widget.grid_columnconfigure(c, weight=1)
