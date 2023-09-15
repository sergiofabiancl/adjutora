import requests
import json

# Configura tus credenciales de Slack
slack_token = ''
channel_id = ''

# URL de la API de Slack para enviar mensajes
slack_api_url = 'https://slack.com/api/chat.postMessage'

# Crea un mensaje
message = "Hola Mundo desde Python!"

# Define el cuerpo de la solicitud POST
payload = {
    'channel': channel_id,
    'text': message
}

# Configura los encabezados de la solicitud con tu token
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {slack_token}'
}

# Realiza la solicitud POST a la API de Slack
response = requests.post(slack_api_url, data=json.dumps(payload), headers=headers)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print("Mensaje enviado con éxito a Slack.")
else:
    print("Error al enviar el mensaje a Slack. Código de respuesta:", response.status_code)
    print("Respuesta:", response.text)
