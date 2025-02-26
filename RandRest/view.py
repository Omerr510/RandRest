import tkinter as tk
from tkinter import ttk, Listbox, Button, Canvas, filedialog
from bidi.algorithm import get_display
import random

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
        self.content_frame = tk.Frame(self.canvas, bg="")
        self.content_frame.place(x=20, y=20)

        # ComboBox
        self.combo_var = tk.StringVar()
        self.combo_box = ttk.Combobox(self.content_frame, textvariable=self.combo_var, state="readonly", font=("Arial", 12), width=15)
        self.combo_box["values"] = (1, 2, 3, 4, 5)
        self.combo_box.current(0)
        self.combo_box.pack(pady=5)

        # Button to get restaurants
        self.get_button = Button(self.content_frame, text="הצג מסעדות אקראיות",
                                command=lambda: [self.controller.get_random_restaurants(), self.start_confetti()],
                                bg=self.button_color, fg="white", bd=0, padx=10, pady=5)
        self.get_button.pack(pady=10)

        # Button to select JSON file
        self.select_file_button = Button(self.content_frame, text="JSON בחר קובץ",
                                       command=self.select_json_file, bg=self.button_color, fg="white", bd=0, padx=10, pady=5)
        self.select_file_button.pack(pady=5)

        # Listbox
        self.listbox = Listbox(self.content_frame, font=("Arial", 14), width=30, justify="right",
                                bg=self.bg_color, fg=self.text_color, bd=0, highlightthickness=0)
        self.listbox.pack(side="left", fill="both", expand=True)

        # Confetti Canvas
        self.confetti_canvas = Canvas(self.root, width=400, height=400, bg="white", highlightthickness=0)
        self.confetti_list = []
        self.animation_running = False

    def select_json_file(self):
        """Opens a file dialog to select a JSON file."""
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.controller.update_json_file(file_path)

    def update_list(self, restaurants):
        """ Updates the listbox with restaurant names """
        self.listbox.delete(0, tk.END)
        for rest in restaurants:
            self.listbox.insert(tk.END, get_display(rest))

    def start_confetti(self):
        if not self.animation_running: # Start animation only if not already running
            self.animation_running = True
            # Remove old confetti before generating new ones
            if hasattr(self, "confetti_pieces"):
                for piece, _ in self.confetti_pieces:
                    self.canvas.delete(piece)
            confetti_count = 30  # Number of confetti pieces

            # Store confetti pieces
            self.confetti_pieces = []

            for _ in range(confetti_count):
                x = random.randint(10, 390)
                y = random.randint(10, 200)
                size = random.randint(5, 10)
                color = random.choice([
                    "red", "blue", "green", "yellow", "purple", "orange",  
                    "pink", "cyan", "magenta", "lime", "teal", "gold",  
                    "violet", "indigo", "turquoise", "salmon", "maroon", "navy",  
                    "lavender", "coral", "khaki", "orchid", "plum", "peru"
                ])

                # Draw confetti directly onto self.canvas
                confetti_piece = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
                self.confetti_pieces.append((confetti_piece, random.randint(1, 3)))  # Store (id, speed)

            self.animate_confetti()

    def animate_confetti(self):
        if self.animation_running: # Continue only if animation should run
            for i, (piece, speed) in enumerate(self.confetti_pieces):
                self.canvas.move(piece, 0, speed)  # Move confetti downward
                x1, y1, x2, y2 = self.canvas.coords(piece)
                if y1 > 400:  # If confetti reaches the bottom, reset position
                    self.canvas.move(piece, 0, -400)

            self.root.after(50, self.animate_confetti)  # Repeat animation
        else:
            self.animation_running = False # Reset the flag

    def create_round_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        points = [x1 + radius, y1, x2 - radius, y1, x2, y1 + radius, x2, y2 - radius, x2 - radius, y2,
                  x1 + radius, y2, x1, y2 - radius, x1, y1 + radius]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)