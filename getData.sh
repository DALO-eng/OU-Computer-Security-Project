#!/bin/bash

# Usage: ./getData.sh <IP>
LIGHT_IP=$1

while true; do

    bulbResponse=$(echo '{"method":"getPilot","params":{}}' | nc -u -w 1 "$LIGHT_IP" 38899)

    # If json array file does not exist, create it
    if [ ! -f "data.json" ]; then
        echo "[]" > data.json
    fi
    
    #Add to the json current date, time and day of the week
    json_object_one_line=$(echo $bulbResponse | jq '.result.date = "'$(date +%Y-%m-%d)'" | .result.time = "'$(date +%H:%M:%S)'" | .result.day = "'$(date +%A)'"')

    #Just take the result object
    json_object_one_line=$(echo $json_object_one_line | jq '.result')

    # Get the current json array file
    json_array=$(cat data.json)

    # Add to the json array file the current json object
    json_array=$(echo $json_array | jq '. += ['"$json_object_one_line"']')

    # Save the json array file
    echo $json_array > data.json

    # Wait
    sleep 30
    clear
done
