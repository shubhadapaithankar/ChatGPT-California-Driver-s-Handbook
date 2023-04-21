from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Load your OpenAI API key
openai.api_key = "Add the key"

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the API call to GPT-3
@app.route('/api/summarize_rules', methods=['POST'])
def summarize_rules():
    # Get the user input
    user_input = request.form['user_input']

    # Call GPT-3 API with the user input
    response = call_gpt3(user_input)

    # Extract the rules from the response
    rules = extract_rules(response)

    # Return the summarized rules
    return jsonify(rules)

# Fine-tune GPT-3 with the specific driving rules from the California Driver’s Handbook

def call_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the rules from the California Driver's Handbook, 2023 based on the following input: {prompt}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

def extract_rules(response):
    rules = [rule.strip() for rule in response.split('\n') if rule.strip()]
    return rules

if __name__ == "__main__":
    app.run(debug=True)
