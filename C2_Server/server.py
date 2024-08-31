from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "C2 Server is running!", 200

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
