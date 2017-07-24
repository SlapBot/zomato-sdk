from core.modules.base_module import BaseModule


class Restaurant(BaseModule):
    def __init__(self, API_KEY="", requester=None):
        super().__init__(API_KEY, requester)
