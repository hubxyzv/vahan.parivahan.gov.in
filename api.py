from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# JSON Settings
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

ALLOWED_KEYS = ["1adcd", "2efgh", "3ijkl", "Happy", "4mnop", "darasingh"]
API_1 = "https://new-pre-vehicle-api.vercel.app/mobile"
API_2 = "https://x-premium-vehicle.vercel.app/mobile"

@app.route("/mobile", methods=["GET"])
def mobile():
    key = request.args.get("key", "")
    reg = request.args.get("registration", "")

    # Basic Validation
    if key not in ALLOWED_KEYS:
        return jsonify({"status": "error", "message": "access key wrong"}), 401
    if not reg:
        return jsonify({"status": "error", "message": "registration number required"}), 400

    params = {"key": key, "registration": reg}

    try:
        # Step 1: Pehle API 2 (Full JSON) try karein
        # Timeout 7 seconds rakha hai taki Vercel khud terminate na kare
        r2 = requests.get(API_2, params=params, timeout=7)
        if r2.status_code == 200:
            data2 = r2.json()
            # Check karein agar data empty toh nahi hai
            if data2 and len(str(data2)) > 10: 
                return jsonify(data2), 200

        # Step 2: Fallback to API 1 (Only Mobile)
        r1 = requests.get(API_1, params=params, timeout=7)
        if r1.status_code == 200:
            data1 = r1.json()
            m_num = data1.get("mobileNo") or data1.get("mobile_no") or data1.get("mobile")
            if m_num:
                return jsonify({"mobile_no": m_num}), 200

    except Exception as e:
        # Log error for internal debugging (optional)
        print(f"Error: {e}")

    # Agar kahin se data nahi mila
    return jsonify({
        "message": "no data found try another number",
        "status": "error"
    }), 404

# Vercel requirements
app.debug = True
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# JSON Settings
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

ALLOWED_KEYS = ["1adcd", "2efgh", "3ijkl", "Happy", "4mnop", "darasingh"]
API_1 = "https://new-pre-vehicle-api.vercel.app/mobile"
API_2 = "https://x-premium-vehicle.vercel.app/mobile"

@app.route("/mobile", methods=["GET"])
def mobile():
    key = request.args.get("key", "")
    reg = request.args.get("registration", "")

    # Basic Validation
    if key not in ALLOWED_KEYS:
        return jsonify({"status": "error", "message": "access key wrong"}), 401
    if not reg:
        return jsonify({"status": "error", "message": "registration number required"}), 400

    params = {"key": key, "registration": reg}

    try:
        # Step 1: Pehle API 2 (Full JSON) try karein
        # Timeout 7 seconds rakha hai taki Vercel khud terminate na kare
        r2 = requests.get(API_2, params=params, timeout=7)
        if r2.status_code == 200:
            data2 = r2.json()
            # Check karein agar data empty toh nahi hai
            if data2 and len(str(data2)) > 10: 
                return jsonify(data2), 200

        # Step 2: Fallback to API 1 (Only Mobile)
        r1 = requests.get(API_1, params=params, timeout=7)
        if r1.status_code == 200:
            data1 = r1.json()
            m_num = data1.get("mobileNo") or data1.get("mobile_no") or data1.get("mobile")
            if m_num:
                return jsonify({"mobile_no": m_num}), 200

    except Exception as e:
        # Log error for internal debugging (optional)
        print(f"Error: {e}")

    # Agar kahin se data nahi mila
    return jsonify({
        "message": "no data found try another number",
        "status": "error"
    }), 404

# Vercel requirements
app.debug = True
