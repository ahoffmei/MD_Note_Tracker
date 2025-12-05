import tkinter as tk 
from .TkComponentBase import TkComponentBase

class EditorBox(TkComponentBase):
    def __init__(self, frame):
        self.textarea = tk.Text(
            frame, 
            wrap = "word",
            bg   =  "#1e1e1e",
            fg   =  "#d4d4d4",
            insertbackground = "white"
            )


    def register(self):
       self.textarea.grid(row=0, column=0, sticky="nsew")


    def disableEditor(self):
        self.textarea.grid_forget() 
    
    
    def getTextArea(self):
        return self.textarea

