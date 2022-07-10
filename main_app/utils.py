from main_app.db import db
import local_settings


def find_restaurants(data):
    cuisine_list = {
        local_settings.CUISINE_LIST[int(data.get('cuisine_choice_list1'))-1],
        local_settings.CUISINE_LIST[int(data.get('cuisine_choice_list2'))-1]
    }
    query_city = {"ranking_geo": {'$regex': local_settings.AVAILABLE_CITIES_LIST[int(data.get('user_city'))-1]},
                  "rating": {'$gte': local_settings.RESTAURANT_RATING_LIST[int(data.get('restaurant_rating'))-1]},
                  'cuisine_list': {'$in': list(cuisine_list)},
                  }
    if int(data.get('price_category')) == 0:
        result = list(db[local_settings.MONGO_DB_COLLECTION].find(query_city))
    else:
        query_city["price_category"] = {'$eq': int(data.get('price_category'))}
        print(query_city)
        result = list(db[local_settings.MONGO_DB_COLLECTION].find(query_city))
    return result





