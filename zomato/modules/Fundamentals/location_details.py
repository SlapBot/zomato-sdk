from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence
from zomato.modules.Fundamentals.location_suggestion import LocationSuggestion
from zomato.modules.Fundamentals.daily_menu import DailyMenu
from zomato.modules.Fundamentals.reviews import Reviews


class LocationDetails(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.best_rated_restaurant)

    def __getitem__(self, index):
        return self.best_rated_restaurant[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.best_rated_restaurant = []
        self.popularity = data['popularity']
        self.nightlife_index = data['nightlife_index']
        self.nearby_res = data['nearby_res']
        self.top_cuisines = data['top_cuisines']
        self.popularity_res = data['popularity_res']
        self.nightlife_res = data['nightlife_res']
        self.subzone = data['subzone']
        self.subzone_id = data['subzone_id']
        self.city = data['city']
        self.location = LocationSuggestion(data['location'], self.r)
        self.num_restaurant = data['num_restaurant']
        self.process_best_rated_restaurant(data['best_rated_restaurant'])

    def process_best_rated_restaurant(self, best_rated_restaurant):
        for restaurant in best_rated_restaurant:
            self.best_rated_restaurant.append(BestRatedRestaurant(restaurant['restaurant'], self.r))


class UserRating:
    def __init__(self, rating, request):
        self.r = request
        self.aggregate_rating = rating['aggregate_rating']
        self.rating_text = rating['rating_text']
        self.rating_color = rating['rating_color']
        self.votes = rating['votes']


class Location:
    def __init__(self, location, request):
        self.r = request
        self.address = location['address']
        self.locality = location['locality']
        self.city = location['city']
        self.city_id = location['city_id']
        self.latitude = location['latitude']
        self.longitude = location['longitude']
        self.zipcode = location['zipcode']
        self.country_id = location['country_id']
        self.locality_verbose = location['locality_verbose']


class BestRatedRestaurant:
    def __init__(self, restaurant, request):
        self.r = request
        self.apikey = restaurant['apikey']
        self.id = restaurant['id']
        self.name = restaurant['name']
        self.url = restaurant['url']
        self.location = Location(restaurant['location'], self.r)
        self.switch_to_order_menu = restaurant['switch_to_order_menu']
        self.cuisines = restaurant['cuisines']
        self.average_cost_for_two = restaurant['average_cost_for_two']
        self.price_range = restaurant['price_range']
        self.currency = restaurant['currency']
        self.offers = restaurant['offers']
        self.thumb = restaurant['thumb']
        self.user_rating = UserRating(restaurant['user_rating'], self.r)
        self.photos_url = restaurant['photos_url']
        self.menu_url = restaurant['menu_url']
        self.featured_image = restaurant['featured_image']
        self.has_online_delivery = restaurant['has_online_delivery']
        self.is_delivering_now = restaurant['is_delivering_now']
        self.deeplink = restaurant['deeplink']
        self.has_table_booking = restaurant['has_table_booking']
        self.events_url = restaurant['events_url']
        self.r = request

    def get_daily_menu(self):
        data, headers = self.r.request('daily_menu', payload={'res_id': self.id})
        return DailyMenu(data, headers, self.r)

    def get_reviews(self):
        data, headers = self.r.request('reviews', payload={'res_id': self.id})
        return Reviews(data, headers, self.r)
