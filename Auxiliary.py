import datetime
from easygui import *
import os


class Auxiliary:



    def getSourceStatementName(self):
        fname = fileopenbox("Выберите файл")
        if fname==None:
            exit(0)
        _, file_extension = os.path.splitext(fname)
        path =  os.path.dirname(fname).upper()
        file_extension = file_extension.upper()

        #   while len(fname) == 0:
        #       if file_extension.upper() != '.DBF':
        #           msgbox('Это не  DBF- файл', ok_button="ОК", title="Перевірте тип файла!")
        #           fname = ''
        # exit ( )
        return path, fname, file_extension

    # многократно заменяет подстроку на указанную строку
    def fullReplace(self, s: str, source: str, pattern: str):
        while s.find(source) != -1:
            s = s.replace(source, pattern)
        return s
