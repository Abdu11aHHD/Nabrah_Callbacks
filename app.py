from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Callback API is running!"

@app.route('/pre-call', methods=['POST'])
def pre_call():
    print("📞 Call received at /pre-call endpoint")

    data = request.json
    print("📦 Raw incoming data:", data)

    # Extract user_number directly
    phone = data.get('user_number', '').lstrip('+')

    if not phone:
        print("❌ Error: 'user_number' field is missing")
        return jsonify({"error": "'user_number' is required"}), 400

    print("📞 Extracted phone number:", phone)

    # Match number
    if phone == "966502104776":
        print("✅ Caller matched: Ahmed")
        return jsonify({"caller_name": "Ahmed"})
    elif phone == "966566128561":
        print("✅ Caller matched: sarah")
        return jsonify({"caller_name": "sarah"})
    else:
        print("❌ Caller not found for number:", phone)
        return jsonify({"error": "Caller not found"}), 404


if __name__ == '__main__':
    app.run()
