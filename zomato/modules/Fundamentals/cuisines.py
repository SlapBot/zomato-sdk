from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence


class Cuisines(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.cuisines)

    def __getitem__(self, index):
        return self.cuisines[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.cuisines = []
        self.process_cuisines(data['cuisines'])

    def process_cuisines(self, cuisines):
        for cuisine in cuisines:
            self.cuisines.append(Cuisine(cuisine['cuisine'], self.r))


class Cuisine:
    def __init__(self, cuisine, request):
        self.r = request
        self.cuisine_id = cuisine['cuisine_id']
        self.cuisine_name = cuisine['cuisine_name']
