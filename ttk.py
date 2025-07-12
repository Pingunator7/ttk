import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Meter
import tkinter as tk
from tkinter import ttk

def cambiar_tema(event):
    nuevo_tema = combo_tema.get()
    app.style.theme_use(nuevo_tema)


app = tb.Window(themename="flatly")
app.title("ttkbootstrap widget demo")
app.geometry("1000x650")
style = app.style


top_frame = ttk.Frame(app)
top_frame.pack(fill=X, pady=5, padx=10)

ttk.Label(top_frame, text="flatly", font=("Segoe UI", 20)).pack(side=LEFT)

combo_tema = ttk.Combobox(top_frame, values=style.theme_names(), width=20)
combo_tema.set("flatly")
combo_tema.pack(side=RIGHT)
combo_tema.bind("<<ComboboxSelected>>", cambiar_tema)


frame_botones = ttk.Frame(app)
frame_botones.pack(pady=5)

colores = ["primary", "secondary", "success", "info", "warning", "danger", "light", "dark"]
for color in colores:
    tb.Button(frame_botones, text=color, bootstyle=color).pack(side=LEFT, padx=2)


frame_check = ttk.Frame(app)
frame_check.pack(pady=5)


cb1 = tb.Checkbutton(frame_check, text="selected", bootstyle="primary", variable=tk.IntVar(value=1))
cb2 = tb.Checkbutton(frame_check, text="deselected", bootstyle="secondary", variable=tk.IntVar(value=0))
cb3 = tb.Checkbutton(frame_check, text="disabled", bootstyle="light", state=DISABLED)

cb1.pack(side=LEFT, padx=5)
cb2.pack(side=LEFT, padx=5)
cb3.pack(side=LEFT, padx=5)


rb_var = tk.IntVar(value=1)
for i, text in enumerate(["selected", "deselected", "disabled"]):
    state = DISABLED if text == "disabled" else NORMAL
    tb.Radiobutton(frame_check, text=text, bootstyle="info", variable=rb_var, value=i, state=state).pack(side=LEFT, padx=5)


frame_tabla = ttk.Frame(app)
frame_tabla.pack(pady=5)

tree = ttk.Treeview(frame_tabla, columns=("City", "Rank"), show="headings", height=5)
tree.heading("City", text="City")
tree.heading("Rank", text="Rank")
tree.column("City", width=300)
tree.column("Rank", width=50)

datos = [
    ("South Island, New Zealand", 1),
    ("Paris", 2),
    ("Bora Bora", 3),
    ("Maui", 4),
    ("Tahiti", 5)
]
for ciudad, rank in datos:
    tree.insert("", "end", values=(ciudad, rank))

tree.pack()


tabs = ttk.Notebook(app)
for i in range(1, 6):
    tab = ttk.Frame(tabs)
    ttk.Label(tab, text="You can put any widget you want here.").pack(padx=10, pady=10)
    tabs.add(tab, text=f"Tab {i}")
tabs.pack(fill=X, padx=10, pady=5)


main_frame = ttk.Frame(app)
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)


zen_text = """\
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Spares is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than "right" now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
frame_left = ttk.Frame(main_frame)
frame_left.pack(side=LEFT, fill=BOTH, expand=True)

txt = tk.Text(frame_left, height=18, wrap=WORD)
txt.insert("1.0", zen_text)
txt.config(state=DISABLED)
txt.pack(fill=BOTH, expand=True)


frame_right = ttk.Frame(main_frame)
frame_right.pack(side=RIGHT, fill=Y, padx=10)


ttk.Scale(frame_right, orient=HORIZONTAL, length=150).pack(pady=5)


tb.Floodgauge(frame_right, value=60, bootstyle="success").pack(pady=5)


Meter(frame_right, amountused=45, metersize=150, subtext="meter widget", bootstyle="info").pack(pady=5)

tb.Button(frame_right, text="solid button", bootstyle="secondary").pack(fill=X, pady=2)
tb.Menubutton(frame_right, text="solid menubutton", bootstyle="secondary").pack(fill=X, pady=2)
tb.Button(frame_right, text="solid toolbutton", bootstyle="success,toolbutton").pack(fill=X, pady=2)
tb.Button(frame_right, text="outline button", bootstyle="info-outline").pack(fill=X, pady=2)
tb.Menubutton(frame_right, text="outline menubutton", bootstyle="warning-outline").pack(fill=X, pady=2)
tb.Button(frame_right, text="outline toolbutton", bootstyle="info-outline,toolbutton").pack(fill=X, pady=2)

ttk.Label(frame_right, text="link button").pack(anchor=W, pady=2)
tb.Checkbutton(frame_right, text="rounded toggle", bootstyle="success,round-toggle").pack(anchor=W)
tb.Checkbutton(frame_right, text="squared toggle", bootstyle="info,square-toggle").pack(anchor=W)


ttk.Label(frame_right, text="Other input widgets").pack(anchor=W, pady=5)
tb.Entry(frame_right).pack(fill=X, pady=2)
ttk.Spinbox(frame_right, from_=0, to=100).pack(fill=X, pady=2)
tb.DateEntry(frame_right).pack(fill=X, pady=2)

app.mainloop()