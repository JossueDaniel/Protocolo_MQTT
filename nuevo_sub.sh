#!/bin/bash
mosquitto_sub -h 127.0.0.1 -p 1883 -t "habitacion/#" -v
