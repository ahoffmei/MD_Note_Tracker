import tkinter

from abc import abstractmethod

class TkComponentBase:
    @abstractmethod
    def register(self):
        pass 