from zomato.requester import Requester


class BaseModule:
    def __init__(self, API_KEY, requester):
        if API_KEY:
            self.r = Requester(API_KEY=API_KEY)
        else:
            self.r = requester
