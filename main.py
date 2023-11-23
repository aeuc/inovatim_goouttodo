import requests

def get_location_and_name(search_query, api_key):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': search_query,
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    results = response.json().get('results', [])
    if results:
        first_result = results[0]
        name = first_result['name']
        location = first_result['geometry']['location']
        return name, location
    else:
        return None, None

def calculate_midpoint(locations):
    if not locations:
        return None
    total_lat = sum(location['lat'] for location in locations)
    total_lng = sum(location['lng'] for location in locations)
    return {'lat': total_lat / len(locations), 'lng': total_lng / len(locations)}

# Google Places API anahtarınızı buraya girin
api_key = "AIzaSyCD_ji6Vc_BS9Z8yytfQxKEZltWYKdCPCE"

# Arama sorgularınızı burada belirtin
search_queries = ["Urla Restoran", "Urla Eczane", "Urla Kırtasiye"]

# Her arama sorgusu için konumları ve isimleri alın
locations = []
names = []
for query in search_queries:
    name, location = get_location_and_name(query, api_key)
    if location:
        locations.append(location)
        names.append(name)

# Bulunan yerlerin isimlerini ve ortalama konumu yazdırın
print("Bulunan Yerler:")
for name in names:
    print(name)

midpoint = calculate_midpoint(locations)
print("\nOrta Nokta Koordinatları:", midpoint)
