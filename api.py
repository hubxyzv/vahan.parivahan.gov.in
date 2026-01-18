from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

# JSON settings
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Authorized Keys
ALLOWED_KEYS = ["1adcd", "2efgh", "3ijkl", "Happy", "4mnop", "darasingh"]

# API Endpoints
API_1 = "https://new-pre-vehicle-api.vercel.app/mobile"
API_2 = "https://x-premium-vehicle.vercel.app/mobile"

def validate():
    key = request.args.get("key", "")
    reg = request.args.get("registration", "")

    if key not in ALLOWED_KEYS:
        return None, jsonify({"status": "error", "message": "access key wrong"}), 401
    if not reg:
        return None, jsonify({"status": "error", "message": "registration number required"}), 400
    
    return reg, None, None

@app.route("/mobile", methods=["GET"])
def mobile():
    reg, err, code = validate()
    if err:
        return err, code

    key_used = request.args.get("key")
    params = {"key": key_used, "registration": reg}
    
    # Retry Logic Settings
    max_retries = 3
    retry_delay = 2  # 2 seconds ka gap har retry ke beech mein

    for attempt in range(max_retries):
        try:
            # Step 1: Check API 2 (Full Details)
            response2 = requests.get(API_2, params=params, timeout=10)
            if response2.status_code == 200:
                data2 = response2.json()
                if data2 and len(data2) > 0:
                    return jsonify(data2), 200

            # Step 2: Fallback to API 1 (Only Mobile)
            response1 = requests.get(API_1, params=params, timeout=10)
            if response1.status_code == 200:
                data1 = response1.json()
                m_num = data1.get("mobileNo") or data1.get("mobile_no") or data1.get("mobile")
                if m_num:
                    return jsonify({"mobile_no": m_num}), 200
            
            # Agar dono API se data nahi mila, toh loop agle attempt par jayega
            time.sleep(retry_delay)

        except Exception:
            # Connection error aane par bhi retry karega
            time.sleep(retry_delay)
            continue

    # Saare attempts khatam hone ke baad agar data nahi mila
    return jsonify({
        "status": "error",
        "message": "no data found try another number"
    }), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

# JSON settings
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Authorized Keys
ALLOWED_KEYS = ["1adcd", "2efgh", "3ijkl", "Happy", "4mnop", "darasingh"]

# API Endpoints
API_1 = "https://new-pre-vehicle-api.vercel.app/mobile"
API_2 = "https://x-premium-vehicle.vercel.app/mobile"

def validate():
    key = request.args.get("key", "")
    reg = request.args.get("registration", "")

    if key not in ALLOWED_KEYS:
        return None, jsonify({"status": "error", "message": "access key wrong"}), 401
    if not reg:
        return None, jsonify({"status": "error", "message": "registration number required"}), 400
    
    return reg, None, None

@app.route("/mobile", methods=["GET"])
def mobile():
    reg, err, code = validate()
    if err:
        return err, code

    key_used = request.args.get("key")
    params = {"key": key_used, "registration": reg}
    
    # Retry Logic Settings
    max_retries = 3
    retry_delay = 2  # 2 seconds ka gap har retry ke beech mein

    for attempt in range(max_retries):
        try:
            # Step 1: Check API 2 (Full Details)
            response2 = requests.get(API_2, params=params, timeout=10)
            if response2.status_code == 200:
                data2 = response2.json()
                if data2 and len(data2) > 0:
                    return jsonify(data2), 200

            # Step 2: Fallback to API 1 (Only Mobile)
            response1 = requests.get(API_1, params=params, timeout=10)
            if response1.status_code == 200:
                data1 = response1.json()
                m_num = data1.get("mobileNo") or data1.get("mobile_no") or data1.get("mobile")
                if m_num:
                    return jsonify({"mobile_no": m_num}), 200
            
            # Agar dono API se data nahi mila, toh loop agle attempt par jayega
            time.sleep(retry_delay)

        except Exception:
            # Connection error aane par bhi retry karega
            time.sleep(retry_delay)
            continue

    # Saare attempts khatam hone ke baad agar data nahi mila
    return jsonify({
        "status": "error",
        "message": "no data found try another number"
    }), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
