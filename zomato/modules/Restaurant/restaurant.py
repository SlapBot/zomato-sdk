from zomato.modules.base_module import BaseModule
from zomato.modules.Fundamentals.daily_menu import DailyMenu
from zomato.modules.Fundamentals.restaurant_info import RestaurantInfo
from zomato.modules.Fundamentals.reviews import Reviews
from zomato.modules.Fundamentals.search import Search


class Restaurant(BaseModule):
    def __init__(self, API_KEY="", requester=None):
        super().__init__(API_KEY, requester)

    def get_daily_menu(self, res_id, raw=False):
        data, headers = self.r.request('daily_menu', payload=locals())
        if raw:
            return data
        return DailyMenu(data, headers, self.r)

    def get_restaurant(self, res_id, raw=False):
        data, headers = self.r.request('restaurant', payload=locals())
        if raw:
            return data
        return RestaurantInfo(data, headers, self.r)

    def get_reviews(self, res_id, start=None, count=None, raw=False):
        data, headers = self.r.request('reviews', payload=locals())
        if raw:
            return data
        return Reviews(data, headers, self.r)

    def search(self, raw=False, **kwargs):
        data, headers = self.r.request('search', payload=locals()['kwargs'])
        if raw:
            return data
        return Search(data, headers, self.r)
