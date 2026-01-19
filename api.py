from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# JSON formatting settings
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Allowed Access Keys (Added 'darasingh' here)
ALLOWED_KEYS = ["1adcd", "darasingh", "3ijkl", "Happy", "4mnop", "2efgh"]

# New API Endpoint
BASE_API = "https://earnindia.top/auth.php"

def validate():
    key = request.args.get("key", "")
    reg = request.args.get("registration", "")

    if key not in ALLOWED_KEYS:
        return None, jsonify({
            "status": "failed",
            "message": "access key wrong"
        }), 401

    if not reg:
        return None, jsonify({
            "status": "failed",
            "message": "registration number required"
        }), 400

    return reg, None, None

@app.route("/mobile", methods=["GET"])
def mobile():
    reg, err, code = validate()
    if err:
        return err, code

    try:
        # Calling the API with parameters
        params = {
            "number": reg,
            "auth": "Madhav"
        }
        
        response = requests.get(BASE_API, params=params, timeout=15)
        data = response.json()
        
        # Getting specific fields
        v_num = data.get("vehicleNumber")
        m_num = data.get("mobileNo")

        # 🚨 Error handling if data is missing or N/A
        if not v_num or v_num == "N/A" or not m_num or m_num == "N/A":
            return jsonify({
                "status": "error",
                "message": "Search field try another vehicle please try again"
            }), 404

        # ✅ Formatted Success Output
        return jsonify({
            "status": "success",
            "vehicleNumber": v_num,
            "mobileNo": m_num,
            "developer": "@CyberVigilantX"
        }), 200
        
    except Exception:
        return jsonify({
            "status": "error",
            "message": "server error"
        }), 500

if __name__ == '__main__':
    # It's better to use a specific host if you need to access this over a network
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# JSON formatting settings
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Allowed Access Keys (Added 'darasingh' here)
ALLOWED_KEYS = ["1adcd", "darasingh", "3ijkl", "Happy", "4mnop", "2efgh"]

# New API Endpoint
BASE_API = "https://earnindia.top/auth.php"

def validate():
    key = request.args.get("key", "")
    reg = request.args.get("registration", "")

    if key not in ALLOWED_KEYS:
        return None, jsonify({
            "status": "failed",
            "message": "access key wrong"
        }), 401

    if not reg:
        return None, jsonify({
            "status": "failed",
            "message": "registration number required"
        }), 400

    return reg, None, None

@app.route("/mobile", methods=["GET"])
def mobile():
    reg, err, code = validate()
    if err:
        return err, code

    try:
        # Calling the API with parameters
        params = {
            "number": reg,
            "auth": "Madhav"
        }
        
        response = requests.get(BASE_API, params=params, timeout=15)
        data = response.json()
        
        # Getting specific fields
        v_num = data.get("vehicleNumber")
        m_num = data.get("mobileNo")

        # 🚨 Error handling if data is missing or N/A
        if not v_num or v_num == "N/A" or not m_num or m_num == "N/A":
            return jsonify({
                "status": "error",
                "message": "Search field try another vehicle please try again"
            }), 404

        # ✅ Formatted Success Output
        return jsonify({
            "status": "success",
            "vehicleNumber": v_num,
            "mobileNo": m_num,
            "developer": "@CyberVigilantX"
        }), 200
        
    except Exception:
        return jsonify({
            "status": "error",
            "message": "server error"
        }), 500

if __name__ == '__main__':
    # It's better to use a specific host if you need to access this over a network
    app.run(debug=True, port=5000)
