from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence
from zomato.modules.Fundamentals.location_details import BestRatedRestaurant


class Search(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.restaurants)

    def __getitem__(self, index):
        return self.restaurants[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.restaurants = []
        self.process_restaurants(data['restaurants'])
        self.results_found = data['results_found']
        self.results_start = data['results_start']
        self.results_shown = data['results_shown']

    def process_restaurants(self, restaurants):
        for restaurant in restaurants:
            self.restaurants.append(BestRatedRestaurant(restaurant['restaurant'], self.r))
