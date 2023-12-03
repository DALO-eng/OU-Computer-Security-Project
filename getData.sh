#!/bin/bash

# Usage: ./getData.sh <IP>
LIGHT_IP=$1

# Temporary json object
jsonTest=$(cat <<EOF
{
  "method": "getPilot",
  "env": "pro",
  "result": {
    "mac": "6c<redacted>6",
    "rssi": -46,
    "src": "",
    "state": true,
    "sceneId": 0,
    "r": 255,
    "g": 238,
    "b": 0,
    "c": 0,
    "w": 0,
    "dimming": 100
  }
}
EOF
)

while true; do

    # If json array file does not exist, create it
    if [ ! -f "data.json" ]; then
        echo "[]" > data.json
    fi
    
    #Add to the json current date and time
    json_object_one_line=$(echo $jsonTest | jq '.result.date = "'$(date +%Y-%m-%d)'" | .result.time = "'$(date +%H:%M:%S)'"')

    #Just take the result object
    json_object_one_line=$(echo $json_object_one_line | jq '.result')

    # Get the current json array file
    json_array=$(cat data.json)

    # Add to the json array file the current json object
    json_array=$(echo $json_array | jq '. += ['"$json_object_one_line"']')

    # Save the json array file
    echo $json_array > data.json

    # Wait
    sleep 60
    clear
done

# LIGHT_IP="192.168.175.27"
# LIGHT_PORT="38899"

# #Set light to RED
# echo '{"id":1,"method":"setPilot","params":{"r":255,"g":0,"b":0,"dimming":100}}' | nc -u -w 1 "$LIGHT_IP" "$LIGHT_PORT"

# while true; do

#     # Turn on the light
#     echo '{"id":1,"method":"setState","params":{"state":true}}' | nc -u -w 1 "$LIGHT_IP" "$LIGHT_PORT"
    
#     # Wait
#     sleep 0.2
#     clear

#     # Turn off the light
#     echo '{"id":1,"method":"setState","params":{"state":false}}' | nc -u -w 1 "$LIGHT_IP" "$LIGHT_PORT"
    
#     # Wait
#     sleep 0.2
#     clear
# done
    

