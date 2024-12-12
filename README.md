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

### Requisitos
- mosquitto
- mosquitto-clients
- Python 3.x
- pip (gestor de paquetes python)

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/JossueDaniel/Protocolo_MQTT.git
```

```bash
cd Protocolo_MQTT
```

### 2. Instalar mosquitto y mosquitto-clients
```bash
sudo apt install mosquitto
```
```bash
sudo apt install mosquitto-clients
```

### 3. Instalar dependencias
```python
pip install -r requirements.txt
```

### 4. Iniciar mosquitto
Para poder iniciar el servidor de MQTT mosquitto se debe ejecutar el fichero de configuración mosquitto.conf
```bash
mosquitto -c mosquitto.conf
```

### 5. Establecer un subscriptor
Se establece un subscriptor "habitación" que pueda escuchar todos los mensajes de la habitación.

- Se otorga permiso para ejecutar el shell script
```bash
chmod +x nuevo_sub.sh
```
- Se ejecuta el shell script
```bash
./nuevo_sub.sh
```

### 6. Establecer el subscriptor "interruptor" de encendido y apagado de la habitación
Se debe ejecutar el script de python para establecer este nuevo subscriptor
```python
python sub_interruptor.py
```

### 7. Publicar información del sensor (topic)
Se ejecutará un shell script para enviar la información del sensor de luz a los interruptores (subscriptores) quién será el encargado de controlar las luces de la habitación

- Se otorga permiso para ejecutar el shell script
```bash
chmod +x pub_sensor.sh
```
- Se ejecuta el shell script para publicar la información del sensor de luz
```bash
./pub_sensor.sh
```
