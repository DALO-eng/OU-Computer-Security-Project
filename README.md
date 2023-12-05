# OU-Computer-Security-Project

A brief description of your project.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

List key features or functionalities of your project.

- Detect the packets that are sent a received from the smart lightbulb
- Collect the data from the lightbulb each X time and save it in a JSON and CSV file
- Read the data collected and show some information obtained about it

## Installation

To install the project you only need to clone the repository, however, you must need to have installed some programs:

### Linux commands

- Netcat (nc)
- Commandline JSON processor (jq)

### Pip modules

- Webcolors
- Scipy
- Pyshark
- Pandas
- Matplotlib


```bash
# Linux commands (Normally you should have them installed)
sudo apt-get install Netcat
# Here is a link to install jq : https://github.com/jqlang/jq/wiki/Installation

# Pip modules
pip install webcolors
pip install pyshark
pip install pandas
pip install matplotlib
```

## Usage

To use all the project correctly, first, you must be aware of some crucial factors:
1. The smart lightbulb, your phone with the Wiz app and the device where you are gonna run this code **MUST** be on the same network
2. This network **MUST** be of 2.4Ghz
3. You have to know the IP address of the bulb, since you are on the same network, is not a big deal to find it

### Collect data from UDP Packets

To start collecting data from UDP Packets
```bash
bash ./getData.sh [BULB IP ADDRESS]
```
This will be saving data to a JSON file during an infinite loop every 30 seconds, until the user decides to stop by shutting the program down.

### Convert the JSON file to CSV

To convert the JSON file received from the last file, you must execute the **dataAnalysis.py** file:
```bash
python3 dataAnalysis.py
```
This will set a CSV file ready to be analyzed in other file.

### Collect data from TLS Packets
To start collecting data from TLS Packets execute the bulb.py script. Before running it, make sure to replace IP address of the light inside of this line of code "if pkt.IP.dst == '192.168.137.34':"

The data of the packets will be saved inside the "packets.csv" file. This will set a CSV file ready to be analyzed.

### Analyze gathered data with Pandas and Matplotlib (Jupyter Notebook)
Just execute the program called "Untitled-1-checkpoint.ipynb" inside Jupyter folder and it will produce statistics.

