from abc import ABC, abstractmethod
import dbf
import Auxiliary
import datetime
import linecache
import os
from string import *


class Statement(ABC):

    @abstractmethod
    def __init__(self):
        self.bank = ""

    @abstractmethod
    def parse(self, fname):
        pass



    def createOutDbfName(self):
        # a =  datetime.datetime.today().strftime("_%m.%Y")
        date = datetime.datetime.now()
        m = str(date.month - 1)
        y = str(date.year)
        suffix = self.bank + "_" + m + "." + y

        # +"."+datetime.datetime.year(now)
        return suffix

    def createEtalonDbf(self, fname):
        fielddescription = "ls C(10); nomerplat C(20); sum N(9,2); data_opl D; comment C(255)"
        table = dbf.Table(fname, fielddescription, codepage='cp866')
        table.open(mode=dbf.READ_WRITE)
        return table

    def writeCortege(self, cortege: str, table: dbf.Table):
        table.append(cortege)
        return None

    def closeEtalonDfb(self, table: dbf.Table):
        table.close()
        return None


class PivdennyStatement(Statement):

    def __init__(self):
        self.bank = "АБПівденний"

    def parse(self,fname):
        pass




class MarfinStatement(Statement):

    def __init__(self):
        self.bank = "МТББанк"


    def parse(self,fname):
        aux=Auxiliary.Auxiliary()
        with open(fname, 'r') as f:
            nums = f.read()
            nums = aux.fullReplace(nums,";;",";")
            nums = aux.fullReplace(nums,"о/р ","о/р")

        print(nums)