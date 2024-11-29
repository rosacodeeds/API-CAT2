import requests

BASE_URL = "http://127.0.0.1:5000/products"

def add_product(name, description, price):
    response = requests.post(BASE_URL, json={
        "name": name,
        "description": description,
        "price": price
    })
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def get_products():
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")
    print(f"Products: {response.json()}")

if __name__ == "__main__":
    add_product("Sample Product", "This is a test product.", 19.99)
    add_product("Another Product", "This is another test.", 29.99)
    get_products()
