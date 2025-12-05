import html
import tkinter as tk 
from markdown import markdown
from tkhtmlview import HTMLLabel
from .MarkdownHandlers import REGISTER_EXTENSIONS
from .Styles import TextSpace
from .TkComponentBase import TkComponentBase


class NoteOutput(TkComponentBase): 
    def __init__(self, frame, editor, debug = False):
        self.editor  = editor 
        self.frame   = frame
        self.debug   = debug
        self.popup   = None 

        # Init and style label element
        self.display = HTMLLabel(
            self.frame, 
            html = self.___styleTextAsHtml___( 
                    "Text entered in the editor will appear here"
                ),
            background = TextSpace.BG_COLOR
        )


        # Update with user input
        self.editor.bind("<KeyRelease>", self.update_display)
        

    def register(self):
        self.display.grid(row=0, column=1, sticky="nsew")        


    def ___markdownWithExtensions___(self, text):
        return markdown(text=text, extensions=REGISTER_EXTENSIONS)


    def ___styleTextAsHtml___(self, text : str): 
        html_submission = f"<div style='color:{TextSpace.TEXT_COLOR}; background-color:{TextSpace.BG_COLOR}'>\n{ 
            self.___markdownWithExtensions___(text=text)
        }</div>"

        if self.debug:
            html_submission = f"<pre style='color:{TextSpace.TEXT_COLOR}; background-color:{TextSpace.BG_COLOR}'>{html.escape(html_submission)}</pre>"
            
        return html_submission


    def update_display(self, event = None):
        text = self.editor.get("1.0", tk.END)
        self.display.set_html( self.___styleTextAsHtml___(text=text) )