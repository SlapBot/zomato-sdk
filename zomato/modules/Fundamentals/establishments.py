from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence


class Establishments(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.establishments)

    def __getitem__(self, index):
        return self.establishments[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.establishments = []
        self.process_establishments(data['establishments'])

    def process_establishments(self, establishments):
        for establishment in establishments:
            self.establishments.append(Establishment(establishment['establishment']))


class Establishment:
    def __init__(self, establishment):
        self.id = establishment['id']
        self.name = establishment['name']
