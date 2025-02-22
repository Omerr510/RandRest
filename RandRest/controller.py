from model import RestaurantModel
from view import RestaurantView

class RestaurantController:
    def __init__(self, root):
        self.model = RestaurantModel()
        self.view = RestaurantView(root, self)

    def get_random_restaurants(self):
        """Gets random restaurants based on user selection."""
        count = int(self.view.combo_var.get())  # Get selected number
        random_restaurants = self.model.get_random_restaurants(count)
        self.view.update_list(random_restaurants)
