import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents_gallery.real_estate_agent.tools.home_search import search_homes

def test_search_homes_within_budget():
    """Tests that the search_homes function returns properties within the price range."""
    properties = search_homes(zip_code="90210", max_price=800000)
    assert len(properties) == 1
    assert properties[0]["address"] == "123 Main St"

def test_search_homes_high_budget():
    """Tests that the search_homes function returns all mock properties for a high budget."""
    properties = search_homes(zip_code="90210", max_price=1000000)
    assert len(properties) == 2

def test_search_homes_low_budget():
    """Tests that the search_homes function returns no properties if budget is too low."""
    properties = search_homes(zip_code="90210", max_price=100000)
    assert len(properties) == 0