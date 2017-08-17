from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence


class Collections(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.collections)

    def __getitem__(self, index):
        return self.collections[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.collections = []
        self.process_collections(data['collections'])
        self.has_more = data['has_more']
        self.share_url = data['share_url']
        self.display_text = data['display_text']
        self.has_total = data['has_total']

    def process_collections(self, collections):
        for collection in collections:
            self.collections.append(Collection(collection['collection'], self.r))


class Collection:
    def __init__(self, collection, request):
        self.r = request
        self.collection_id = collection['collection_id']
        self.res_count = collection['res_count']
        self.image_url = collection['image_url']
        self.url = collection['url']
        self.title = collection['title']
        self.description = collection['description']
        self.share_url = collection['share_url']
