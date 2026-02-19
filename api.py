"""API Flask pour la calculatrice."""
from flask import Flask, jsonify, request
from app import add, subtract, multiply, divide

api = Flask(__name__)


@api.route("/health")
def health():
    """Endpoint de sante."""
    return jsonify({"status": "healthy"})


@api.route("/calculate", methods=["POST"])
def calculate():
    """Endpoint de calcul."""
    data = request.get_json()
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation is None or a is None or b is None:
        return jsonify({"error": "Champs requis : operation, a, b"}), 400

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        return jsonify({"error": f"Operation inconnue : {operation}"}), 400

    try:
        result = operations[operation](a, b)
        return jsonify({"operation": operation, "a": a, "b": b, "result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000, debug=True)
