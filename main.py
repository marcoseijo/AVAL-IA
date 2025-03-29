import tkinter as tk
from gui import show_loading_screen, show_demo_screen

if __name__ == "__main__":
    root = tk.Tk()
    root.title("AVAL-IA Demo")
    show_loading_screen(root, lambda: show_demo_screen(root))
    root.mainloop()