class BaseFundamental:
    def __init__(self, raw_data, headers, request):
        self.raw_data = raw_data
        self.headers = headers
        self.r = request
