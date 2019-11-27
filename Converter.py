
import easygui
from abc import ABCMeta, abstractmethod
class Converter(ABCMeta):

    def __init__(self):
        self.filename = easygui.fileopenbox("Выберите файл","Открыть файл...")

        pass

    def writeDbf(self):
        pass

    @abstractmethod
    def parseSource(self):
        pass

