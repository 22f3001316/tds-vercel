import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student marks data
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get all 'name' parameters
    marks = [student_data.get(name, None) for name in names]  # Get marks
    return jsonify({"marks": marks})

# Vercel requires this for the entry point
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run(debug=True)
