import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents_gallery.real_estate_agent.tools.home_search import search_homes

mock_properties = [
    {"address": "123 Main St", "price": 750000},
    {"address": "456 Oak Ave", "price": 950000},
]

def mock_call_listings(zipcode, max_price, min_beds=3):
    return [p for p in mock_properties if p["price"] <= max_price]

@patch('agents_gallery.real_estate_agent.tools.home_search.call_listings', side_effect=mock_call_listings)
def test_search_homes_within_budget(mock_call_listings_function):
    """Tests that the search_homes function returns properties within the price range."""
    properties = search_homes(zip_code="90210", max_price=800000)
    assert len(properties) == 1
    assert properties[0]["address"] == "123 Main St"

@patch('agents_gallery.real_estate_agent.tools.home_search.call_listings', side_effect=mock_call_listings)
def test_search_homes_high_budget(mock_call_listings_function):
    """Tests that the search_homes function returns all mock properties for a high budget."""
    properties = search_homes(zip_code="90210", max_price=1000000)
    assert len(properties) == 2

@patch('agents_gallery.real_estate_agent.tools.home_search.call_listings', side_effect=mock_call_listings)
def test_search_homes_low_budget(mock_call_listings_function):
    """Tests that the search_homes function returns no properties if budget is too low."""
    properties = search_homes(zip_code="90210", max_price=100000)
    assert len(properties) == 0
