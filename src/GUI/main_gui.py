import os
import re 
import sys
import pathlib
import tkinter as tk 

from tkinter import filedialog

# Import GUI dependencies 
from .TextComponents.EditorBox import EditorBox
from .TextComponents.TextFrame import TextFrame, ViewBtn
from .TextComponents.RenderedText import NoteOutput
from .StartWindow.CustomFileNav import CustomFileDialog

src_path = str(pathlib.Path(re.search(r".*md_note_tracker\\src", os.path.abspath(__file__)).group()))
if src_path not in sys.path:
    sys.path.append(src_path)

from env_config import DEFALT_SAVE_DIR

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
        
        # Topbar options -- TODO put this all in a grid mayb
        self.view_btn    = ViewBtn(root=root, editor=self.editor_box)

        test = CustomFileDialog(root, DEFALT_SAVE_DIR)

    def renderDocNav(self):
        """
        @brief  Handles rendering of document navigation
        """
        pass 


    def renderEditor(self): 
        """
        @brief  Handles rendering of editor elements
        """
        # Register in ideal order
        # Topbar render 
        self.view_btn.register()
        self.text_frame.register()
        
        # Render notes section
        self.editor_box.register()
        self.note_output.register()