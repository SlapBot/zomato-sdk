from zomato.modules.base_module import BaseModule
from zomato.modules.Fundamentals.categories import Categories
from zomato.modules.Fundamentals.cities import Cities
from zomato.modules.Fundamentals.collections import Collections
from zomato.modules.Fundamentals.cuisines import Cuisines
from zomato.modules.Fundamentals.establishments import Establishments
from zomato.modules.Fundamentals.geocode import Geocode


class Common(BaseModule):
    def __init__(self, API_KEY="", requester=None):
        super().__init__(API_KEY, requester)

    def get_categories(self, raw=False):
        data, headers = self.r.request('categories')
        if raw:
            return data
        return Categories(data, headers, self.r)

    def get_cities(self, q="", lat=None, lon=None, city_ids=None, count=None, raw=False):
        if city_ids is None:
            city_ids = []
        data, headers = self.r.request('cities', payload=locals())
        if raw:
            return data
        return Cities(data, headers, self.r)

    def get_collections(self, city_id=None, lat=None, lon=None, count=None, raw=False):
        data, headers = self.r.request('collections', payload=locals())
        if raw:
            return data
        return Collections(data, headers, self.r)

    def get_cuisines(self, city_id=None, lat=None, lon=None, raw=False):
        data, headers = self.r.request('cuisines', payload=locals())
        if raw:
            return data
        return Cuisines(data, headers, self.r)

    def get_establishments(self, city_id=None, lat=None, lon=None, raw=False):
        data, headers = self.r.request('establishments', payload=locals())
        if raw:
            return data
        return Establishments(data, headers, self.r)

    def get_geocode(self, lat, lon, raw=None):
        data, headers = self.r.request('geocode', payload=locals())
        if raw:
            return data
        return Geocode(data, headers, self.r)
