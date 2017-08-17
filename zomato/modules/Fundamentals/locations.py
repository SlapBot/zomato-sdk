from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence
from zomato.modules.Fundamentals.location_suggestion import LocationSuggestion


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
