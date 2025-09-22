from flask import Flask, jsonify
app = Flask(__name__)

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/bcv', methods=['GET'])
def bcv_scraper():
    try:
        print("Inicio del scraping BCV")
        response = requests.get("https://www.bcv.org.ve", timeout=10)
        response.raise_for_status()  # Lanza excepción si el status no es 200

        # Aquí deberías extraer las tasas del HTML
        # Simulación de datos extraídos:
        tasas = {
            "usd": "38.50",
            "eur": "41.20"
        }

        print("Scraping exitoso")
        return jsonify(tasas)

    except requests.exceptions.Timeout:
        print("Timeout al conectar con BCV")
        return jsonify({"status": "error", "data": {"error_id": "408", "message": "Tiempo de espera agotado"}}), 408

    except requests.exceptions.RequestException as e:
        print("Error de conexión:", str(e))
        return jsonify({"status": "error", "data": {"error_id": "500", "message": "Error de conexión", "detalle": str(e)}}), 500

    except Exception as e:
        print("Error interno:", str(e))
        return jsonify({"status": "error", "data": {"error_id": "500", "message": "Error interno", "detalle": str(e)}}), 500

if __name__ == '__main