from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/pre-call', methods=['POST'])
def pre_call():
    print("📞 Call received at /pre-call endpoint")

    data = request.json
    print("📦 Raw incoming data:", data)

    # Get the 'call_details' field and parse the JSON string
    call_details_raw = data.get('call_details')
    if not call_details_raw:
        print("❌ Error: 'call_details' field is missing")
        return jsonify({"error": "call_details is required"}), 400

    try:
        call_details = json.loads(call_details_raw)
    except Exception as e:
        print("❌ Error parsing call_details:", e)
        return jsonify({"error": "Invalid call_details JSON"}), 400

    # Extract the phone number
    phone = call_details.get('call_to', '').lstrip('+')
    print("📞 Extracted phone number:", phone)

    if not phone:
        print("❌ No phone number found in call_details")
        return jsonify({"error": "Phone number not found in call_details"}), 400

    # Basic name matching
    if phone == "966502104776":
        print("✅ Caller matched: Ahmed")
        return jsonify({"caller_name": "Ahmed"})
    elif phone == "966566128561":
        print("✅ Caller matched: Sara")
        return jsonify({"caller_name": "Sara"})
    else:
        print("❌ Caller not found for number:", phone)
        return jsonify({"error": "Caller not found"}), 404


if __name__ == '__main__':
    app.run()
