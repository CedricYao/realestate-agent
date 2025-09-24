from adk.tools import tool

@tool
def search_homes(zip_code: str, max_price: int) -> list:
    """Searches for homes in a given zip code up to a maximum price."""

    print(f"Searching for homes in {zip_code} up to ${max_price}...")

    # Mock response
    mock_properties = [
        {
            "address": "123 Main St, Anytown, USA",
            "price": 1200000,
            "bedrooms": 3,
            "bathrooms": 2,
            "sqft": 1800,
        },
        {
            "address": "456 Oak Ave, Anytown, USA",
            "price": 1500000,
            "bedrooms": 4,
            "bathrooms": 3,
            "sqft": 2400,
        },
    ]

    return [p for p in mock_properties if p["price"] <= max_price]
