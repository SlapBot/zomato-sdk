from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence
from zomato.modules.Fundamentals.collections import Collections
from zomato.modules.Fundamentals.cuisines import Cuisines
from zomato.modules.Fundamentals.establishments import Establishments


class Cities(BaseFundamental, Sequence):
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
        self.id = location_suggestion['id']
        self.name = location_suggestion['name']
        self.country_id = location_suggestion['country_id']
        self.country_name = location_suggestion['country_name']
        self.should_experiment_with = location_suggestion['should_experiment_with']
        self.discovery_enabled = location_suggestion['discovery_enabled']
        self.has_new_ad_format = location_suggestion['has_new_ad_format']
        self.is_state = location_suggestion['is_state']
        self.state_id = location_suggestion['state_id']
        self.state_name = location_suggestion['state_name']
        self.state_code = location_suggestion['state_code']

    def get_collections(self):
        data, headers = self.r.request('collections', payload={'city_id': self.id})
        return Collections(data, headers, self.r)

    def get_cuisines(self):
        data, headers = self.r.request('cuisines', payload={'city_id': self.id})
        return Cuisines(data, headers, self.r)

    def get_establishments(self):
        data, headers = self.r.request('establishments', payload={'city_id': self.id})
        return Establishments(data, headers, self.r)
