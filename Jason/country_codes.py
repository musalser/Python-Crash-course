from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for country_code in COUNTRIES.keys():
        if COUNTRIES[country_code] == country_name:
            return country_code
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))