# Zomato SDK

Installation
============

Using ``pip``:



	pip install zomato-sdk

This is an unofficial SDK for [Zomato](https://developers.zomato.com/api).

Usage is as simple as it gets:

    from zomato import Zomato
    z = Zomato("YOUR-API-KEY")
    
Now there are three objects presented namely, `common`, `location` and `restaurant` as listed at [Developers](https://developers.zomato.com/documentation)

    common = z.common
    location = z.location
    restaurant = z.restaurant
    
Now Each object has different methods as listed in documentation section of Zomato API, namely

- Common
    - get_categories
    - get_cities
    - get_collections
    - get_cuisines
    - get_establishments
    - get_geocode
- Location
    - get_location_details
    - get_locations
- Restaurant
    - get_daily_menu
    - get_restaurant
    - get_reviews
    - search
    
All of them takes parameters as listed in Documentation section of Zomato API : https://developers.zomato.com/documentation (except the user-key which is initialized as headers)

The best thing about it is that everything is modular, and connected to each other, letting you do things like:
    
    $city = z.common.get_cities()[0]
    $city.get_collections()

Tests are written to give an idea on how the API works, do check them to get a clear understanding on how to use the sdk.

Documentation about each class explicitly will be released by this week.
