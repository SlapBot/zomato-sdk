import unittest


class TestZomato(unittest.TestCase):
    @staticmethod
    def do_init():
        from zomato.zomato import Zomato
        z = Zomato(API_KEY="e74778cd3728858df3578092ecea02cf")
        return z

    def test_get_all_categoies(self):
        z = self.do_init()
        category = z.common.get_categories()[0]
        self.assertEqual(category.id, 1)
        self.assertEqual(category.name, 'Delivery')

    def test_get_cities(self):
        z = self.do_init()
        city = z.common.get_cities("kanpur")[0]
        self.assertEqual(city.id, 23)
        self.assertEqual(city.country_id, 1)
        self.assertEqual(city.name, 'Kanpur')
        self.assertEqual(city.country_name, 'India')

    def test_get_collections(self):
        z = self.do_init()
        collection = z.common.get_collections(5)[0]
        self.assertIsNotNone(collection)

    def test_get_establishments(self):
        z = self.do_init()
        collection = z.common.get_establishments(5)[0]
        self.assertIsNotNone(collection)

    def test_get_cuisines(self):
        z = self.do_init()
        collection = z.common.get_cuisines(5)[0]
        self.assertIsNotNone(collection)

    def test_get_locations(self):
        z = self.do_init()
        collection = z.location.get_locations("kanpur")
        self.assertAlmostEqual(collection.status, "success")

    def test_get_location_details(self):
        z = self.do_init()
        collection = z.location.get_location_details(3, "city")[0]
        self.assertIsNotNone(collection)

    def test_get_restaurant(self):
        z = self.do_init()
        collection = z.restaurant.get_restaurant(18392725)
        self.assertIsNotNone(collection)

    def test_get_reviews(self):
        z = self.do_init()
        collection = z.restaurant.get_reviews(18392725)
        self.assertIsNotNone(collection)

    def test_search(self):
        z = self.do_init()
        collection = z.restaurant.search(q="kanpur")
        self.assertIsNotNone(collection)

if __name__ == "__main__":
    unittest.main()

