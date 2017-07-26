class EndpointManager:
    def __init__(self):
        self.base_url = "https://developers.zomato.com/api/v2.1"
        self.endpoints = self.get_endpoints()

    def get_endpoints(self):
        endpoints = {
            'categories': self.base_url + '/categories',
            'cities': self.base_url + '/cities',
            'collections': self.base_url + '/collections',
            'cuisines': self.base_url + '/cuisines',
            'establishments': self.base_url + '/establishments',
            'geocode': self.base_url + '/geocode',
            'location_details': self.base_url + '/location_details',
            'locations': self.base_url + '/locations',
            'daily_menu': self.base_url + '/daily_menu',
            'restaurant': self.base_url + '/restaurant',
            'reviews': self.base_url + '/reviews',
            'search': self.base_url + '/search'
        }
        return endpoints

    def get_endpoint(self, name):
        return self.endpoints[name]
