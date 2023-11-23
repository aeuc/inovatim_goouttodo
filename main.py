import requests
import openai

chatgpt_api_key = "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"
google_maps_api_key = "AIzaSyCD_ji6Vc_BS9Z8yytfQxKEZltWYKdCPCE"

def get_chatgpt_response(prompt, api_key):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

def get_location(search_query, google_maps_api_key):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': search_query,
        'key': google_maps_api_key
    }
    response = requests.get(base_url, params=params)
    results = response.json().get('results', [])
    if results:
        return results[0]['geometry']['location']
    else:
        return None

def calculate_midpoint(locations):
    if not locations:
        return None
    total_lat = sum(location['lat'] for location in locations)
    total_lng = sum(location['lng'] for location in locations)
    return {'lat': total_lat / len(locations), 'lng': total_lng / len(locations)}


# Kullanıcıdan gelen metin
user_input = "Bugün ödevim var ve mukavvam bitmiş, yenisini almam lazım. Biraz da acıktım dışarı çıktığımda iyice acıkacağım. Aynı zamanda ağrı kesicim bitmiş"

# ChatGPT ile ihtiyaçları çözümle
chatgpt_response = get_chatgpt_response(user_input, chatgpt_api_key)
print("ChatGPT Çıktısı:", chatgpt_response)

# Google Maps API ile yerleri bul
search_queries = chatgpt_response.split("\n")  # Her satırı ayrı bir sorgu olarak kabul edin
locations = []
for query in search_queries:
    location = get_location(query, google_maps_api_key)
    if location:
        locations.append(location)

# Ortalama konumu hesapla
midpoint = calculate_midpoint(locations)
print("Orta Nokta Koordinatları:", midpoint)

