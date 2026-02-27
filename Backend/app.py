from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ Added

from utils.age_utils import check_age, future_age
from utils.mobile_utils import check_mobile
from utils.aadhaar_utils import check_aadhaar
from utils.crypto_utils import encrypt_aadhaar, decrypt_aadhaar

app = Flask(__name__)
CORS(app)   # ✅ Enable CORS

# Normal Verify Route
@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    dob = data.get("dob")
    future_year = data.get("future_year")
    mobile = data.get("mobile")
    aadhaar = data.get("aadhaar")

    # ✅ Debug log (terminal এ দেখার জন্য)
    print("Received JSON:", data)

    # ✅ Age Proof
    dob_result = check_age(dob)
    print("DOB result:", dob_result)   # Debug log

    # ✅ Future Age Proof
    future_age_result = None
    if future_year:
        try:
            future_age_result = future_age(dob, int(future_year))
        except Exception:
            future_age_result = "Proof Failed: Invalid future year"

    # ✅ Mobile & Aadhaar Proof
    mobile_result = check_mobile(mobile)
    aadhaar_result = check_aadhaar(aadhaar)

    # ✅ Refined status logic
    if ("Invalid" in dob_result or "Failed" in dob_result or
        "Invalid" in mobile_result or "Failed" in mobile_result or
        "Invalid" in aadhaar_result or "Failed" in aadhaar_result):
        status = "Proof Failed"
    else:
        status = "All Proofs Verified"

    return jsonify({
        "dob_proof": dob_result,
        "future_age_proof": future_age_result,
        "mobile_proof": mobile_result,
        "aadhaar_proof": aadhaar_result,
        "status": status
    })

# Secure Aadhaar Verify Route (ZKP-style)
@app.route("/secure_verify", methods=["POST"])
def secure_verify():
    data = request.json
    aadhaar = data.get("aadhaar")

    encrypted = encrypt_aadhaar(aadhaar)

    try:
        decrypted = decrypt_aadhaar(encrypted)
        aadhaar_result = check_aadhaar(decrypted)
    except Exception:
        aadhaar_result = "Proof Failed: Invalid Aadhaar Number"

    status = "Proof Verified" if "Valid" in aadhaar_result else "Proof Failed"

    return jsonify({
        "encrypted_aadhaar": encrypted,
        "decrypted_aadhaar": "hidden",
        "aadhaar_proof": aadhaar_result,
        "status": status
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)