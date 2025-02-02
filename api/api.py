import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load student marks data
try:
    with open("q-vercel-python.json", "r") as file:
        student_data = json.load(file)
except Exception as e:
    student_data = {}  # Fallback in case of an error
    print("Error loading JSON file:", e)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get names from query params
    marks = [student_data.get(name, None) for name in names]  # Fetch marks
    return jsonify({"marks": marks})

# Vercel entry point
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run(debug=True)
