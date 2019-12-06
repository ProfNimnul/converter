import dbf, datetime
import easygui
from abc import  ABC, abstractmethod


class Statement(ABC):

    @abstractmethod
    def parse(self):
        pass


    def getDbfName(self)->str:
        fname = fileopenbox("Выберите файл", default="*.dbf")

        filename, file_extension = p.splitext(fname)

        while len(fname) == 0:
            if file_extension.upper() != '.DBF':
                msgbox('Это не  DBF- файл', ok_button="ОК", title="Перевірте тип файла!")
                fname = ''
                # exit ( )
        return fname

    def  createEtalonDbf(self):
        outfilename = {"PivdennyStatement":"111.dbf", "MarfinStatement":"222.dbf"}[self.__class__.__name__ == "PivdennyStatement"]

        fielddescription =  "ls C(10); nomerplat C(20); sum N(9,2); data_opl D; comment C(255)"
        table =  dbf.Table("d:\\vypiski.dbf", fielddescription, codepage='cp866')
        table.open(mode=dbf.READ_WRITE)
        return table

    def writeCortege(self, cortege:str, table:dbf.Table):
        table.append(cortege)
        return None

    def closeEtalonDfb(self, table:dbf.Table):
        table.close()
        return None



class PivdennyStatement(Statement):

    def parse(self):
        pass

class MarfinStatement(Statement):

    def parse(self):
        pass



if __name__ == '__main__':


    converter = EtalonDBF()

    filename = converter.getDbfName()

    table = converter.createEtalonDbf()
    for _ in range(10):
        info = ("test_ls", "test_nomerplat", 10.5, datetime.datetime.date(datetime.datetime.now()), "test_comment")
        converter.writeCortege(info,table)

    converter.closeEtalonDfb(table)


