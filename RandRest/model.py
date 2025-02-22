import json
import random
from bidi.algorithm import get_display

class RestaurantModel:
    def __init__(self, file_path="data/Input1.json"):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """Loads JSON data from file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file).get("list", [])
        except FileNotFoundError:
            return []

    def get_random_restaurants(self, count):
        """Returns 'count' random restaurant names."""
        restaurants = [get_display(rest["name"]) for rest in self.data] # removed arabic_reshaper
        return random.sample(restaurants, min(count, len(restaurants)))