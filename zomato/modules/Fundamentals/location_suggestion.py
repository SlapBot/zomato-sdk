# from core.modules.Fundamentals.location_details import LocationDetails
from zomato.modules.Fundamentals.collections import Collections
from zomato.modules.Fundamentals.cuisines import Cuisines
from zomato.modules.Fundamentals.establishments import Establishments


class LocationSuggestion:
    def __init__(self, location_suggestion, request):
        self.r = request
        self.entity_type = location_suggestion['entity_type']
        self.entity_id = location_suggestion['entity_id']
        self.title = location_suggestion['title']
        self.latitude = location_suggestion['latitude']
        self.longitude = location_suggestion['longitude']
        self.city_id = location_suggestion['city_id']
        self.city_name = location_suggestion['city_name']
        self.country_id = location_suggestion['country_id']
        self.country_name = location_suggestion['country_name']

    def get_collections(self):
        data, headers = self.r.request('collections', payload={'city_id': self.city_id})
        return Collections(data, headers, self.r)

    def get_cuisines(self):
        data, headers = self.r.request('cuisines', payload={'city_id': self.city_id})
        return Cuisines(data, headers, self.r)

    def get_establishments(self):
        data, headers = self.r.request('establishments', payload={'city_id': self.city_id})
        return Establishments(data, headers, self.r)
    #
    # def get_location_details(self):
    #     data, headers = self.r.request('location_details', payload={
    #         'entity_id': self.entity_id,
    #         'entity_type': self.entity_type
    #     })
    #     return LocationDetails(data, headers, self.r)
