import json
from math import cos, asin, sqrt

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)

def get_seats(json_content):
    all_seats = []
    for bar_count in range(len(json_content['features'])):
        all_seats.append(json_content['features'][bar_count]['properties']['Attributes']['SeatsCount'])
    return all_seats

def print_bars(bar_attributes):
    print('Название: ', bar_attributes['Name'])
    print('Округ: ', bar_attributes['AdmArea'])
    print('Район: ', bar_attributes['District'])
    print('Адрес: ', bar_attributes['Address'])
    print('Количество мест: ', bar_attributes['SeatsCount'])
    print('Телефон: ', bar_attributes['PublicPhone'][0]['PublicPhone'])
    print('**************************************************************')
    
def get_biggest_bar(json_content):
    max_seats = (max(get_seats(json_content)))
    print('************************** Biggest bar ***********************')
    for bar_count in range(len(json_content['features'])):
        if json_content['features'][bar_count]['properties']['Attributes']['SeatsCount'] == max_seats: 
            bar_attributes = json_content['features'][bar_count]['properties']['Attributes']
            print_bars(bar_attributes)

def get_smallest_bar(json_content):
    min_seats = (min(get_seats(json_content)))
    print('************************ Smallest bar ************************')
    for bar_count in range(len(json_content['features'])):
        if json_content['features'][bar_count]['properties']['Attributes']['SeatsCount'] == min_seats: 
            bar_attributes = json_content['features'][bar_count]['properties']['Attributes']
            print_bars(bar_attributes)

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def get_closest_bar(json_content, latitude, longitude):
    all_coordinates = []
    for bar_count in range(len(json_content['features'])):
        coordinate = {
            'lat': json_content['features'][bar_count]['geometry']['coordinates'][0],
            'lon': json_content['features'][bar_count]['geometry']['coordinates'][1],
        }
        all_coordinates.append(coordinate)
    
    human_coordinates = {'lat': float(latitude), 'lon': float(longitude)}
    closest_bar = min(all_coordinates, key=lambda p: distance(human_coordinates['lat'], human_coordinates['lon'], p['lat'], p['lon']))
  
    print('************************** Closest bar ***********************')
    for bar_count in range(len(json_content['features'])):
        bar_coordinate = json_content['features'][bar_count]['geometry']['coordinates']
        if  bar_coordinate[0] == closest_bar['lat'] and bar_coordinate[1] == closest_bar['lon'] : 
            bar_attributes = json_content['features'][bar_count]['properties']['Attributes']
            print_bars(bar_attributes)

if __name__ == '__main__':
    json_content = load_data(r'd:\PythonScript\Devman\bars.json')
    big_bars = get_biggest_bar(json_content)
    smallest_bars = get_smallest_bar(json_content)
    latitude = input('Введите координаты latitude: ')
    longitude = input('Введите координаты longitude: ')
    get_closest_bar(json_content, latitude, longitude)    


