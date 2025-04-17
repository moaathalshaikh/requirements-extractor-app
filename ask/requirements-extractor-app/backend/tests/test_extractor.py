from flask import Flask, request, jsonify
from requirements_extractor.extractor import extract_requirements

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    data = request.json
    text = data.get('text', '')
    requirements = extract_requirements(text)
    return jsonify(requirements)

if __name__ == '__main__':
    app.run(debug=True)