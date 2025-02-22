import tkinter as tk
from controller import RestaurantController

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantController(root)
    root.mainloop()
