from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence


class DailyMenu(BaseFundamental):
    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.daily_menu_info = DailyMenuInformation(data['daily_menu'], self.r)
        self.code = data['code']
        self.status = data['status']
        self.message = data['message']


class DailyMenuInformation(Sequence):
    def __len__(self):
        return len(self.dishes)

    def __getitem__(self, index):
        return self.dishes[index]

    def __init__(self, daily_menu, request):
        self.r = request
        self.dishes = []
        self.process_dishes(daily_menu['dishes'])
        self.daily_menu_id = daily_menu['daily_menu_id']
        self.name = daily_menu['name']
        self.start_date = daily_menu['start_date']
        self.end_date = daily_menu['end_date']

    def process_dishes(self, dishes):
        for dish in dishes:
            self.dishes.append(Dish(dish, self.r))


class Dish:
    def __init__(self, dish, request):
        self.r = request
        self.dish_id = dish['dish_id']
        self.name = dish['name']
        self.price = dish['price']
