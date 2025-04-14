from scapy.all import sniff
from datetime import datetime

def packet_callback(packet):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {packet.summary()}")

def main():
    print("Starting packet sniffer...\nPress Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
