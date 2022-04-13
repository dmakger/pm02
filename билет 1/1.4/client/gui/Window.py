import tkinter as tk
from gui.Table import Table


class Window:

    def __init__(self, ws, heads, content=None, label="Window"):
        self.ws = tk.Toplevel(ws)
        tk.Label(self.ws, text=label).pack()
        self.table = self.get_table(heads, content)
        self.table.start(expand=tk.YES, fill=tk.BOTH)
        self.ws.mainloop()

    def get_table(self, heads, content):
        return Table(self.ws, heads, content)
