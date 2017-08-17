from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence


class Categories(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.categories)

    def __getitem__(self, index):
        return self.categories[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.categories = []
        self.process_categories(data['categories'])

    def process_categories(self, categories):
        for category in categories:
            self.categories.append(Category(category['categories'], self.r))


class Category:
    def __init__(self, category, request):
        self.id = category['id']
        self.name = category['name']
        self.r = request
