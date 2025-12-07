import tkinter as tk
import os

class CustomFileDialog(tk.Toplevel):
    def __init__(self, root, start_dir):
        self.root = root 
        self.current_dir = start_dir
        self.selected_file = None

        self.dir_label = tk.Label(self.root, text=self.current_dir)
        self.dir_label.pack(fill="x")

        self.file_list = tk.Listbox(self.root)
        self.file_list.pack(fill="both", expand=True)
        self.file_list.bind("<Double-1>", self.on_double_click)

        # TODO: Do something with these buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(fill="x")
        tk.Button(self.btn_frame, text="Up", command=self.go_up).pack(side="left")
        tk.Button(self.btn_frame, text="Select", command=self.select_file).pack(side="right")

        self.___populate___()


    def ___populate___(self):
        self.file_list.delete(0, tk.END)
        try:
            for item in os.listdir(self.current_dir):
                self.file_list.insert(tk.END, item)
        except PermissionError:
            pass # Should probably do something 


    def go_up(self):
        self.current_dir = os.path.dirname(self.current_dir)
        self.dir_label.config(text=self.current_dir)
        self.___populate___()


    def on_double_click(self, event = None):
        selection = self.file_list.get(self.file_list.curselection())
        path = os.path.join(self.current_dir, selection)
        if os.path.isdir(path):
            self.current_dir = path
            self.dir_label.config(text=self.current_dir)
            self.___populate___()
        else:
            self.selected_file = path
            self.destroy() # TODO: idk if destorying is correct 


    def select_file(self):
        selection          = self.file_list.get(self.file_list.curselection())
        self.selected_file = os.path.join(self.current_dir, selection)
        
        self.destroy() # TODO: idk if destroying is correct 

