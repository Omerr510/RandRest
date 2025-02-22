import tkinter as tk
from tkinter import ttk, Listbox, Button, Canvas
from bidi.algorithm import get_display
from PIL import Image, ImageTk

class RestaurantView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("רשימת מסעדות")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.bg_color = "#ffffff"
        self.button_color = "#3f51b5"
        self.text_color = "#333333"

        # Rounded Rectangle Background
        self.canvas = Canvas(root, width=380, height=380, bg="#f0f0f0", highlightthickness=0)
        self.create_round_rectangle(10, 10, 390, 390, radius=20, fill=self.bg_color)
        self.canvas.pack(pady=10)

        # Frame inside the Canvas for content
        self.content_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.content_frame.place(x=20, y=20)

        # Styled Combobox Container
        self.combo_container = tk.Frame(self.content_frame, bg=self.bg_color)
        self.combo_container.pack(pady=5)

        # Rounded Rectangle for Combobox
        self.combo_canvas = Canvas(self.combo_container, width=200, height=30, bg=self.bg_color, highlightthickness=0)
        self.create_round_rectangle_combobox(0, 0, 200, 30, radius=15, fill=self.bg_color, canvas=self.combo_canvas)
        self.combo_canvas.pack(side="left")

        # Create Custom Style
        style = ttk.Style()
        style.layout("Rounded.TCombobox", [
            ('Combobox.downarrow', {'sticky': 'e', 'children': [
                ('Rounded.Combobox.downarrow.button', {'sticky': 'nswe'})
            ]}),
            ('Combobox.padding', {'sticky': 'nswe', 'children': [
                ('Combobox.textarea', {'sticky': 'nswe'})
            ]})
        ])

        # Combobox inside the Rounded Rectangle with Custom Style
        self.combo_var = tk.StringVar()
        self.combo_box = ttk.Combobox(self.combo_container, textvariable=self.combo_var, state="readonly", font=("Arial", 12), width=15, style="Rounded.TCombobox")
        self.combo_box["values"] = (1, 2, 3, 4, 5)
        self.combo_box.current(0)
        self.combo_box.place(relx=0.5, rely=0.5, anchor=tk.CENTER, x=0)  # Centered and shifted left

        # Button to get restaurants
        self.get_button = Button(self.content_frame, text="הצג מסעדות אקראיות", command=self.controller.get_random_restaurants, bg=self.button_color, fg="white", bd=0, padx=10, pady=5)
        self.get_button.pack(pady=10)

        # Listbox (no scrollbar)
        self.listbox = Listbox(self.content_frame, font=("Arial", 14), width=30, justify="right", bg=self.bg_color, fg=self.text_color, bd=0, highlightthickness=0)
        self.listbox.pack(side="left", fill="both", expand=True)


    def update_list(self, restaurants):
        self.listbox.delete(0, tk.END)
        for rest in restaurants:
            self.listbox.insert(tk.END, get_display(rest))

    def create_round_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        points = [x1 + radius, y1,
                  x2 - radius, y1,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1, y2 - radius,
                  x1, y1 + radius]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def create_round_rectangle_combobox(self, x1, y1, x2, y2, radius, fill, canvas):
        points = [x1 + radius, y1,
                  x2 - radius, y1,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1, y2 - radius,
                  x1, y1 + radius]
        return canvas.create_polygon(points, fill=fill, smooth=True)