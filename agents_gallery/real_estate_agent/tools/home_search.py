import requests
import os
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()
has_data_api_key = os.getenv("HAS_DATA_API_KEY")


def search_homes(zip_code: str, max_price: int, min_beds: int=3) -> List[Dict[str, Any]]:
    """
    Searches for homes in a given zip code up to a maximum price.

    Args:
        zip_code: The zip code to search in.
        max_price: The maximum price of the properties.
        min_beds: The minimum number of bedrooms.

    Returns:
        A list of properties matching the criteria. Be sure to include images, price, address, and a link to the listing.
    """

    return call_listings(zip_code, max_price, min_beds)


def call_listings(zipcode:str, max_price:int, min_beds:int=3) -> List[Dict[str, Any]]:
    """
    Calls the Zillow API to get listings for sale in Superior, CO
    with a minimum of 3 beds and a maximum price of $600,000.
    """
    url = "https://api.hasdata.com/scrape/zillow/listing"
    
    # The API key is sensitive and should not be hardcoded.
    # For this example, it is included, but in a real application,
    # it should be loaded from an environment variable or a secure vault.
    headers = {
        "Content-Type": "application/json",
        "x-api-key": has_data_api_key
    }
    
    params = {
        "keyword": zipcode,
        "type": "forSale",
        "beds.min": min_beds,
        "price.max": max_price
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()