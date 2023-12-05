# OU-Computer-Security-Project

A brief description of your project.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

List key features or functionalities of your project.

- Detect the packets that are sent a recieved from the smart lightbulb
- Collect the data from the lightbulb each X time and save it in a Json and csv file
- Read the data collected and show some information obtained about it

## Installation

To install the project you only need to clone the repository, however, you must need to have installed some programs:

### Linux commands

- Netcat (nc)
- Commandline JSON processor (jq)
- 

### Pip modules

- Webcolors
- Scipy
- 

```bash
# Linux commands (Normally you should have them installed)
sudo apt-get install Netcat
# Here is a link to instal jq : https://github.com/jqlang/jq/wiki/Installation

# Pip modules
pip install webcolors
pip install scipy
```

## Usage

To use all the project correctly, first you must be aware of some crucial factors:
1. The smart lightbulb, your phone with the Wiz app and the device where you are gonna run this code **MUST** be on the same network
2. This network **MUST** be of 2.4Ghz
3. You have to know the IP address of the bulb, since you are on the same network, is not a big deal to find it

### Collect data from UDP Packets

To start collecting data from UDP Packets, you must run the **getData.sh** file:
```bash
bash ./getData.sh [BULB IP ADDRESS]
```
This will be saving data to a json file during an infinite loop every 30 seconds, until the user decides to stop by shutting the program down.

### Convert the Json file to Csv

To convert the json file recieved from the last file, you must execute the **dataAnalysis.py** file:
```bash
python3 dataAnalysis.py
```
This will set a Csv file ready to be analized in other file.
