
import unittest
from real_estate_agent.tools.home_search import search_homes

class TestHomeSearch(unittest.TestCase):

    def test_search_homes_within_budget(self):
        """Tests that the search_homes function returns properties within the price range."""
        properties = search_homes(zip_code="90210", max_price=800000)
        self.assertEqual(len(properties), 1)
        self.assertEqual(properties[0]["address"], "123 Main St")

    def test_search_homes_high_budget(self):
        """Tests that the search_homes function returns all mock properties for a high budget."""
        properties = search_homes(zip_code="90210", max_price=1000000)
        self.assertEqual(len(properties), 2)

    def test_search_homes_low_budget(self):
        """Tests that the search_homes function returns no properties if budget is too low."""
        properties = search_homes(zip_code="90210", max_price=100000)
        self.assertEqual(len(properties), 0)

if __name__ == '__main__':
    unittest.main()
