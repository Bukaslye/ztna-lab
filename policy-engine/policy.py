from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Policy rules: identity → allowed resources
POLICIES = {
    "engineer-01": ["service-a", "service-b"],
    "analyst-01":  ["service-b"],
}

@app.route("/authorize", methods=["POST"])
def authorize():
    identity = request.json.get("identity")
    resource = request.json.get("resource")
    hour = datetime.now().hour

    # Time-based restriction (business hours only)
    if not (7 <= hour <= 20):
        return jsonify({"allow": False, "reason": "outside_hours"}), 403

    allowed = POLICIES.get(identity, [])
    if resource in allowed:
        return jsonify({"allow": True})
    return jsonify({"allow": False, "reason": "policy_denied"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
