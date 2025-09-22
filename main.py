
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

def scrape_bcv():
    url = "https://www.bcv.org.ve/"
    try:
        response = requests.get(url, verify=False, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        usd_element = soup.find(id="dolar")
        eur_element = soup.find(id="euro")

        usd_value = usd_element.get_text(strip=True) if usd_element else "N/A"
        eur_value = eur_element.get_text(strip=True) if eur_element else "N/A"

        return {"USD": usd_value, "EUR": eur_value}

    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def home():
    return jsonify(scrape_bcv())

if __name__ == "__main__":
    app.run(port=3000)

