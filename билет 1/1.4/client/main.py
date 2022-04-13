import config
from database.Datasource import Datasource
from gui.Tkinter import Tkinter


def main():
    datasource = Datasource(config.host, config.user, config.password, config.db_name)

    gui = Tkinter()
    gui.set_table(gui.MAIN_TABLE_HEADS, datasource.get_statement_view())

    gui.set_add_button(None)
    gui.set_percentage_button(gui.PERCENTAGE_TABLE_HEADS, datasource.get_education_quality_view())
    gui.set_stay_button(None)

    gui.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

