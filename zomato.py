from base import Base
from core.modules.Common.common import Common
from core.modules.Location.location import Location
from core.modules.Restaurant.restaurant import Restaurant


class Zomato(Base):
    def __init__(self, API_KEY):
        super().__init__(API_KEY)
        self.common = Common(requester=self.requester)
        self.location = Location(requester=self.requester)
        self.restaurant = Restaurant(requester=self.requester)
