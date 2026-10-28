from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Temperature Converter API",
        "menu": {
            "1": "Convert Celsius to Fahrenheit -> Route: /convert/c-to-f"
        }
    })

@app.route('/convert/c-to-f', methods=['GET'])
def c_to_f():
    try:
        celsius = float(request.args.get('celsius', 0))
        fahrenheit = (celsius * 9/5) + 32
        return jsonify({"celsius": celsius, "fahrenheit": fahrenheit})
    except ValueError:
        return jsonify({"error": "Invalid input value"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
