import os
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")


@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if request.method == "POST":
        if 'url' in request.form:
            url = request.form['url']
            try:
                response = requests.get(url)
                response.raise_for_status()
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                data = ' '.join([p.get_text() for p in soup.find_all('p')])
            except Exception as e:
                return render_template("index.html", error=str(e))
        else:
            data = request.form["data"]

        API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
        headers = {
            "Authorization": f"{os.getenv('API_KEY')}"
        }

        max_length = int(request.form["maxL"])
        min_length = max_length // 4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length": min_length, "max_length": max_length},
        })

        # Check if output is in the expected format
        if isinstance(output, list) and output:
            summary_text = output[0].get("summary_text", "")
            return render_template("index.html", result=summary_text)
        else:
            error_message = "Failed to generate summary. Please try again."
            return render_template("index.html", error=error_message)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
