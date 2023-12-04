import pyshark
import csv
from datetime import datetime

"""This Python script utilizes the PyShark library to capture network traffic on a specified interface, filtering packets with a
target IP address associated with a light. The code focuses on extracting and saving the payload of Transport Layer Security
(TLS) packets containing encrypted application data."""


def remove_colons(input_string):
    return input_string.replace(":", "")


def extract_encrypted_data(packet):
    # Check if the 'TLS.app_data' layer is present in the packet
    if 'TLS' in packet and hasattr(packet.TLS, 'app_data'):
        application_data = remove_colons(packet.TLS.app_data)
        return application_data


def packet_callback(pkt):
    # Check if the 'IP' layer is present in the packet
    if hasattr(pkt, 'IP'):
        # Check if the destination IP address matches the target IP
        if pkt.IP.dst == '192.168.137.9':
            if 'TLS' in pkt:
                # Extract the payload of the TLS packet
                pkt_payload = extract_encrypted_data(pkt)

                if pkt_payload:
                    # Get current time
                    timestamp = datetime.now()

                    # Extract relevant details
                    source_ip = pkt.IP.src
                    destination_ip = pkt.IP.dst

                    # Append the details to a CSV file
                    with open('packets.csv', 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = ['Timestamp', 'Day of Week', 'Source IP',
                                      'Destination IP', 'Encrypted Application Data']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                        # Write header if the file is empty
                        if csvfile.tell() == 0:
                            writer.writeheader()

                        # Write the TLS payload details
                        writer.writerow({
                            'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                            # Format to get the day of the week
                            'Day of Week': timestamp.strftime('%A'),
                            'Source IP': source_ip,
                            'Destination IP': destination_ip,
                            'Encrypted Application Data': pkt_payload
                        })

                        print(
                            f"TLS packet payload saved to packets.csv:\n{timestamp} | {source_ip} -> {destination_ip} | {pkt_payload}")


capture = pyshark.LiveCapture(
    interface='Local Area Connection* 2', display_filter='ip')
capture.apply_on_packets(packet_callback)
