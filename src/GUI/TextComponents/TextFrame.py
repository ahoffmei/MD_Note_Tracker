import tkinter as tk 
from enum import Enum
from .EditorBox import EditorBox
from .RenderedText import NoteOutput
from .TkComponentBase import TkComponentBase

class TextFrame(TkComponentBase):
    def __init__(self, root):
        self.root  = root 
        self.frame = tk.Frame(self.root)

    def register(self):
        self.frame.pack(fill="both", expand=True)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def getFrame(self):
        return self.frame
    


class ViewBtn(TkComponentBase):
    VIEW_TXT = ["Toggle Edit Mode", "Toggle Preview Mode"]

    def __init__(self, root, editor : EditorBox, start_in_edit_state : bool = True):
        """
        @brief  Controls Views modes (Editor mode vs Preview Mode). Yes this doubles as a controller. 
        """
        self.editor     = editor
        self.edit_mode  = start_in_edit_state
        self.view_btn   = tk.Button(
            root, 
            text = self.VIEW_TXT[self.edit_mode], 
            command=self.___toggleNewState___
        )


    def register(self):
        self.view_btn.pack(side="top", padx=5, pady=5)


    def ___toggleNewState___(self):
        if self.edit_mode:
            # In edit mode, so enter preview mode by disabling editor
            self.editor.disableEditor() 
        else:  
            # In preview mode, so enter edit mode by enabling editor
            self.editor.register()

        self.edit_mode = not self.edit_mode
        self.view_btn.config(text = self.VIEW_TXT[self.edit_mode])
    