from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data
user_id = "john_doe_17091999"
email = "john@xyz.com"
roll_number = "ABCD123"

# Helper function to process data
def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if not highest_lowercase_alphabet or item > highest_lowercase_alphabet[0]:
                    highest_lowercase_alphabet = [item]

    return numbers, alphabets, highest_lowercase_alphabet

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data')
        
        if not data or not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        numbers, alphabets, highest_lowercase_alphabet = process_data(data)

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
