from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Callback API is running!"

@app.route('/pre-call', methods=['POST'])
def pre_call():
    data = request.json

    # Get the 'call_details' field and parse the JSON string
    call_details_raw = data.get('call_details')
    if not call_details_raw:
        return jsonify({"error": "call_details is required"}), 400

    try:
        call_details = json.loads(call_details_raw)
    except Exception as e:
        return jsonify({"error": "Invalid call_details JSON"}), 400

    # Extract the phone number from call_to
    phone = call_details.get('call_to', '').lstrip('+')

    if not phone:
        return jsonify({"error": "Phone number not found in call_details"}), 400

    # Match number and return name
    if phone == "966502104776":
        return jsonify({"caller_name": "Ahmed"})
    elif phone == "966580323262":
        return jsonify({"caller_name": "Sara"})
    else:
        return jsonify({"error": "Caller not found"}), 404


if __name__ == '__main__':
    app.run()
