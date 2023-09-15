from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/slack/saludo', methods=['POST'])
def saludar():
    data = request.form  # Obtiene los datos de la solicitud de Slack
    # print(data)

    # Verifica si la solicitud incluye el parámetro 'command'
    if 'command' in data:
        comando = data['command']
        usuario = data['user_name']

        # Verifica si el comando es "/saludo"
        if comando == '/saludo':
            respuesta = {
                "text": f"¡Hola {usuario}! ¿En qué puedo ayudarte hoy?"
            }
            # print('Mensaje recibido')
            return jsonify(respuesta)

    # Si no se proporciona el comando o no es "/saludo", devuelve un mensaje de error
    return jsonify({"text": "Comando no válido."})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
