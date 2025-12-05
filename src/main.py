# TODO HEADER 
import argparse
import tkinter as tk 

from GUI.main_gui import MainGui

def setup_opts(): 
    parser = argparse.ArgumentParser(description="MD Based Notetaking Application")
    parser.add_argument('-d', '--debug', dest= "DEBUG", action="store_true",  
                        help="Use for debugging.. duh")

    return parser.parse_args() 


if __name__ == "__main__":
    args = setup_opts()

    root = tk.Tk()  
    app  = MainGui(root, args.DEBUG)
    root.mainloop() 