from zomato.base import Base
from zomato.modules.Common.common import Common
from zomato.modules.Location.location import Location
from zomato.modules.Restaurant.restaurant import Restaurant


class Zomato(Base):
    def __init__(self, API_KEY):
        super().__init__(API_KEY)
        self.common = Common(requester=self.requester)
        self.location = Location(requester=self.requester)
        self.restaurant = Restaurant(requester=self.requester)
