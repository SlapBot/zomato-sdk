from zomato.core.modules.fundamentals.base_fundamental import BaseFundamental


class Categories(BaseFundamental):
	def __init__(self, data, headers, request)
		super().__init__(self, data, headers, request)
		self.categories_list = self.process_categories(self.data['categories'])

class CategoriesList:
	def __init__(self, categories_list):

	def process_categories(categories_list):
		categories = []
		for category in categories_list:
			categories.append()