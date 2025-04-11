from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "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"
MODEL = "llama-3.3-70b-versatile"  # or any valid Groq model

@app.route("/", methods=["GET", "POST"])
def index():
    reply = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
        )
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"].strip()
        else:
            reply = f"Error {response.status_code}: {response.text}"

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)