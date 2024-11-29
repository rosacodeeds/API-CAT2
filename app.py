from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (for simplicity)
products = []

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Invalid data"}), 400

    product = {
        "id": len(products) + 1,
        "name": data['name'],
        "description": data.get('description', ''),
        "price": data['price']
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
