#!/usr/bin/python
def check_my_city(city_name):
    if city_name == "PANTIN-":
        return({"stations_nb": 1,
                "zip_code": ['93500'],
                "city": 'pantin'})
    elif city_name == "BAGNOLET":
        return({"stations_nb": 1,
                "zip_code": ['93170'],
                "city": 'bagnolet'})
    elif city_name == "PARIS-":
        return({"stations_nb": 3,
                "zip_code": ['75001', '75008', '75010'],
                "city": 'paris'})
    else:
        return("Sorry! No station for your city has been found!")
