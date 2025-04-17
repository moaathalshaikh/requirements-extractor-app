from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract-requirements', methods=['POST'])
def extract_requirements():
    data = request.json
    input_text = data.get('text', '')

    # Call the OpenAI GPT-4 API to extract requirements
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Extract functional and non-functional requirements from the following text: {input_text}"}
        ]
    )

    extracted_requirements = response['choices'][0]['message']['content']
    return jsonify({'requirements': extracted_requirements})

if __name__ == '__main__':
    app.run(debug=True)