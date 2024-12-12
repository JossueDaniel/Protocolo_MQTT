#!/bin/bash
mosquitto_pub -h 127.0.0.1 -p 1883 -t "habitacion/sensor" -m \
"{ device_id: "5ee9df89-a719-4e9a-ac54-84b9c3096f40", \
event_time: 2025-06-12 14:07:46.580465000, \
value: 60, \
accuracy: 0.98 }"
