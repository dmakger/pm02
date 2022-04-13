import tkinter as tk
from tkinter import ttk


class Table:

    def __init__(self, frame, heads, content):
        self.table = ttk.Treeview(frame, show='headings')
        self.table['columns'] = heads

        for header in heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center')

        for row in content:
            self.table.insert('', tk.END, values=row)

        scroll_pane = ttk.Scrollbar(frame, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)

    def start(self, expand=None, fill=None):
        self.table.pack(expand=expand, fill=fill)
