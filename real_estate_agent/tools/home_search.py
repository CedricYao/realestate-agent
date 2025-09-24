
from typing import List, Dict, Any

def search_homes(zip_code: str, max_price: int) -> List[Dict[str, Any]]:
    """
    Searches for homes in a given zip code up to a maximum price.

    Args:
        zip_code: The zip code to search in.
        max_price: The maximum price of the properties.

    Returns:
        A list of properties matching the criteria.
    """
    print(f"Searching for homes in {zip_code} up to ${max_price}...")

    # For now, this function returns a hard-coded list of properties
    # to simulate a real estate API call.
    mock_properties = [
        {
            "address": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip_code": zip_code,
            "price": 750000,
            "bedrooms": 3,
            "bathrooms": 2,
            "sqft": 1500,
        },
        {
            "address": "456 Oak Ave",
            "city": "Anytown",
            "state": "CA",
            "zip_code": zip_code,
            "price": 950000,
            "bedrooms": 4,
            "bathrooms": 3,
            "sqft": 2200,
        },
    ]

    # Filter properties by max_price
    return [p for p in mock_properties if p["price"] <= max_price]
