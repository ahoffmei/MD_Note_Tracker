import tkinter as tk 
import os, sys
# Import GUI dependencies 
from .TextComponents.EditorBox import EditorBox
from .TextComponents.TextFrame import TextFrame, ViewBtn
from .TextComponents.RenderedText import NoteOutput


class MainGui:
    def __init__(self, root : tk.Tk, debug = False):
        self.root  = root 
        self.debug = debug
        self.root.title("Hello World")
        self.root.configure(bg = "black")

        label = tk.Label(root, text="ello")
        label.pack(padx=20, pady=20)

        # Manage components

        # Editor/Preview Space
        self.text_frame  = TextFrame(root=root) 
        self.editor_box  = EditorBox(self.text_frame.getFrame())
        self.note_output = NoteOutput(self.text_frame.getFrame(), self.editor_box.getTextArea(), self.debug)
        
        # Topbar options -- TODO put this all in a grid
        self.view_btn    = ViewBtn(root=root, editor=self.editor_box)

        # Register in ideal order
        # Topbar render 
        self.view_btn.register()
        self.text_frame.register()
        self.editor_box.register()
        self.note_output.register()