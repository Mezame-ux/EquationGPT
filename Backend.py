from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input', '')
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=user_input,
        max_tokens=150
    )
    return jsonify(response.choices[0].text)

if __name__ == '__main__':
    app.run(debug=True)