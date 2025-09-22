from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/bcv')
def bcv_scraper():
    try:
        # Aquí va tu lógica de scraping
        data = scrape_bcv()
        return jsonify(data)
    except Exception as e:
        print("Error interno:", str(e))
        return jsonify({"error": "Scraper falló", "detalle": str(e)}), 500

if __name__ == '__main__':
    app.run()
