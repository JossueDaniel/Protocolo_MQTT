import ssl
import sys
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f'Conectado {client._client_id}')
    client.subscribe(topic='habitacion/sensor', qos=2)

def on_message(client, userdata, message):
    decoded_payload = message.payload.decode('utf-8')
    formatted_payload = decoded_payload.replace("'", '"') \
        .replace(": ", '": "') \
        .replace("{ ", '{"') \
        .replace(", ", '", "') \
        .replace(" }", '"}') \
        .replace('"}"', '"')

    try:
        payload_dict = json.loads(formatted_payload)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)

    value = payload_dict.get('value')
    acurracy = payload_dict.get('accuracy')
    print('-------------------------')
    print('topic: %s' % message.topic)
    print('Información: %s' % message.payload)

    if float(acurracy) > 0.9 and int(value) < 50:
        print("------>Encender luces<------")
    else:
        print("------>Apagar luces<-----")

def main():
    client = mqtt.Client(client_id='interruptor', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='127.0.0.1', port=1883)
    client.loop_forever()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
