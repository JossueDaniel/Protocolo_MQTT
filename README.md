# Protocolo_MQTT

Este proyecto utiliza el protocolo de mensajería ligera MQTT, Eclipse Mosquitto que actúa como un broker el cual facilita la comunicación entre clientes MQTT.

## Escenario
Debe simular una solución IoT que consiste en dos dispositivos:
1. Sensor de luz
2. Interruptores de encendido/apagado de las luces de una habitación
La información que publica un sensor de luz tiene la siguiente estructura en un JSON:

```json
{
    "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
    "event_time": "2025-06-12 14:07:46.580465000",
    "value": 60,
    "accuracy": 0.98
}
```

La información debe ser recibida por un suscriptor que controla las luces de una habitación. Si el sensor de luz reporta un valor menor que 50 con una precisión mayor a 0.9, debe imprimir un mensaje que indique que se encenderán las luces, caso contrario, debe imprimir un mensaje que indique que las luces serán apagadas. De esta forma simularemos el encendido/apagado de luces.
