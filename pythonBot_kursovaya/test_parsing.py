import requests
import config

s_city_1 ="Орел"
s_city_2 = "Вашингтон"
s_city_3 = "Эмпайр"

api_parameters_1 = {'APPID': config.API_KEY, 'q': s_city_1, 'units': 'metric'}
api_parameters_2 = {'APPID': config.API_KEY, 'q': s_city_2, 'units': 'metric'}
api_parameters_3 = {'APPID': config.API_KEY, 'q': s_city_3, 'units': 'metric'}

def test_one():
    assert requests.get(config.API_LINK, params=api_parameters_1)
def test_two():
    assert requests.get(config.API_LINK, params=api_parameters_2)
def test_three():
    assert requests.get(config.API_LINK, params=api_parameters_3)