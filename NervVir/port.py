import socket


def scan_ports(host):
    open_ports = []
    for port in range(1, 65536):  # Сканируем порты от 1 до 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Установите таймаут для подключения
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def run():
    target_host = input("Введите IP-адрес или хост для сканирования: ")

    print(f"Сканирование {target_host} всех портов от 1 до 65535...")
    open_ports = scan_ports(target_host)

    if open_ports:
        print(f"Открытые порты: {open_ports}")
    else:
        print("Открытых портов не найдено.")
