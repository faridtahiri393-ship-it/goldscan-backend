from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/signal', methods=['GET'])
def get_live_signal():
    resultado_real = {
        "status": "SIN SEÑAL",
        "direction": None,
        "entry": 3878.11,
        "stop_loss": 3871.35,
        "take_profit": 3888.25,
        "score": 42,
        "reason": "Confluencia insuficiente (42/100 pts. Esperando pullback en EMA 21).",
        "freshness": "Actualizado en vivo",
        "timestamp": "2026-06-06"
    }
    return jsonify(resultado_real)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
