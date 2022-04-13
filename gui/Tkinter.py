import tkinter as tk
from gui.Table import Table
from gui.Window import Window


class Tkinter:
    TITLE = "Деканат"
    WIDTH = 500
    HEIGHT = 500
    BACKGROUND = "#E7E8EC"

    MAIN_TABLE_HEADS = ['group_name', 'discipline_name', 'attestation_type_name', 'mentor_name',
                        'statement_attestation_date']
    PERCENTAGE_TABLE_HEADS = ['group_name', 'success']

    def __init__(self):
        self.table = None
        self.ws = self.get_ws()
        self.frame = self.get_frame()

    def get_ws(self):
        ws = tk.Tk()
        ws.title(self.TITLE)
        # ws.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        ws['bg'] = self.BACKGROUND
        return ws

    def get_frame(self):
        frame = tk.Frame(self.ws, relief=tk.RAISED, borderwidth=1)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame

    def set_table(self, heads, content):
        self.table = Table(self.frame, heads, content)

    def set_add_button(self, command):
        tk.Button(self.ws, text="Добавить", command=command).pack(side=tk.LEFT, padx=5, pady=5)

    def set_percentage_button(self, heads, content):
        tk.Button(self.ws, text="Качество обучения по группам",
                  command=lambda: Window(self.ws, heads, content, "Качество обучения по группам")).pack(side=tk.RIGHT,
                                                                                                        padx=5, pady=5)

    def set_stay_button(self, command):
        tk.Button(self.ws, text="Список неуспевающих", command=command).pack(side=tk.RIGHT)

    def start(self):
        self.table.start(expand=tk.YES, fill=tk.BOTH)
        self.ws.mainloop()
