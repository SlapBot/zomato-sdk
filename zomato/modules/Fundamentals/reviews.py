from zomato.modules.Fundamentals.base_fundamental import BaseFundamental
from collections.abc import Sequence


class Reviews(BaseFundamental, Sequence):
    def __len__(self):
        return len(self.user_reviews)

    def __getitem__(self, index):
        return self.user_reviews[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.user_reviews = []
        self.process_user_reviews(data['user_reviews'])
        self.reviews_count = data['reviews_count']
        self.reviews_start = data['reviews_start']
        self.reviews_shown = data['reviews_shown']
        self.respond_to_reviews_via_zomato_dashboard = data['Respond to reviews via Zomato Dashboard']

    def process_user_reviews(self, reviews):
        for review in reviews:
            self.user_reviews.append(Review(review['review'], self.r))


class Review:
    def __init__(self, review, request):
        self.r = request
        self.rating = review['rating']
        self.review_text = review['review_text']
        self.id = review['id']
        self.rating_color = review['rating_color']
        self.review_time_friendly = review['review_time_friendly']
        self.rating_text = review['rating_text']
        self.timestamp = review['timestamp']
        self.likes = review['likes']
        self.comments_count = review['comments_count']
        self.user = User(review['user'], self.r)


class User:
    def __init__(self, user, request):
        self.r = request
        self.name = user['name']
        self.foodie_level = user['foodie_level']
        self.foodie_level_num = user['foodie_level_num']
        self.foodie_color = user['foodie_color']
        self.profile_url = user['profile_url']
        self.profile_image = user['profile_image']
        self.profile_deeplink = user['profile_deeplink']
