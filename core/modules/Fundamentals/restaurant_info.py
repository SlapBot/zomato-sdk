from core.modules.Fundamentals.base_fundamental import BaseFundamental
from core.modules.Fundamentals.location_details import BestRatedRestaurant


class RestaurantInfo(BaseFundamental):
    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.restaurant = BestRatedRestaurant(data, self.r)
