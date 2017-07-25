from core.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence
from core.modules.Fundamentals.location_details import LocationDetails
from core.modules.Fundamentals.collections import Collections
from core.modules.Fundamentals.cuisines import Cuisines
from core.modules.Fundamentals.establishments import Establishments


class Locations(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.location_suggestions)

    def __getitem__(self, index):
        return self.location_suggestions[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.location_suggestions = []
        self.process_location_suggestions(data['location_suggestions'])
        self.status = data['status']
        self.has_more = data['has_more']
        self.has_total = data['has_total']

    def process_location_suggestions(self, location_suggestions):
        for location_suggestion in location_suggestions:
            self.location_suggestions.append(LocationSuggestion(location_suggestion, self.r))


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

    def get_location_details(self):
        data, headers = self.r.request('location_details', payload={
            'entity_id': self.entity_id,
            'entity_type': self.entity_type
        })
        return LocationDetails(data, headers, self.r)
