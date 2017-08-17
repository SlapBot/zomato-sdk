from zomato.modules.Fundamentals.base_fundamental import BaseFundamental


class Geocode(BaseFundamental):
    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.data = data
