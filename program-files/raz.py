from tkinter.ttk import Combobox
from tkinter import *
import os
from distutils.core import setup
import py2exe


def get_selected(param):
    """
    Function make connection between combobox values and programs
    Input: combobox parameter
    """
    icombo = combo.current() + 1
    #print('index ', icombo)
    if icombo == 1:
        os.system('python part_1_otl_1.py')
    elif icombo == 2:
        os.system('python part_2_otl_1.py')

    else:
        os.system('python part_3_otl_1.py')


window = Tk()
window.geometry('400x250')
combo = Combobox(values=["Действия с числами в разных СС ", "Алгебра логики",
                         "Формулы комбинаторики"], width=30)
combo.bind('<<ComboboxSelected>>', get_selected)
combo.place(x=10, y=10)
mainloop()
