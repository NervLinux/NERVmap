# NERV

from scapy.all import *
import time

from scapy.layers.dot11 import Dot11Beacon, Dot11Elt, Dot11

# Список для хранения информации о сетях
wifi_networks = {}

def packet_handler(packet):
    # Проверяем, является ли пакет Beacon
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode()  # Получаем SSID
        bssid = packet[Dot11].addr2  # Получаем BSSID
        channel = int(packet[Dot11Beacon].network_stats().get('channel', 0))

        # Сохраняем информацию о сети
        wifi_networks[bssid] = {
            'SSID': ssid,
            'Channel': channel,
            'Signal Strength': packet.dBm_AntSignal
        }

def start_sniffing(interface):
    print("Начинаем анализ Wi-Fi сетей...")
    sniff(iface=interface, prn=packet_handler, store=0)

def run():
    interface = input("Введите имя интерфейса для анализа (пишите 'Беспроводная сеть')")
    try:
        start_sniffing(interface)
    except KeyboardInterrupt:
        print("\nАнализ завершен.")
        print("\nНайденные Wi-Fi сети:")
        for bssid, info in wifi_networks.items():
            print(f"BSSID: {bssid}, SSID: {info['SSID']}, Channel: {info['Channel']}, Signal Strength: {info['Signal Strength']} dBm")

