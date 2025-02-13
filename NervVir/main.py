# NERV

import sqlxss
import wifi
import port
import logi
import bezopasnot
import bio

def display_banner():
    print('''
███╗   ██╗███████╗██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ 
████╗  ██║██╔════╝██╔══██╗██║   ██║    ████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║█████╗  ██████╔╝██║   ██║    ██╔████╔██║███████║██████╔╝
██║╚██╗██║██╔══╝  ██╔══██╗╚██╗ ██╔╝    ██║╚██╔╝██║██╔══██║██╔═══╝
██║ ╚████║███████╗██║  ██║ ╚████╔╝     ██║ ╚═╝ ██║██║  ██║██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝
           ''')
    print("===================================")
    print("  Инструмент безопасности NERVmap   ")
    print("===================================")
    print("1. Проверка SQL-инъекций (sqlxss)")
    print("2. Проверка Wi-Fi сети (wifi)")
    print("3. Проверка портов (port)")
    print("4. Проверка логов (logi)")
    print("5. Общая проверка безопасности (bezopasnot)")
    print("6. О туле, BIO")
    print("0. Выход")
    print("===================================")

def main():
    while True:
        display_banner()
        choice = input("Выберите подходящий тул: ")

        if choice == '1':
            sqlxss.run()  # Предполагается, что в sqlxss.py есть функция run()1
        elif choice == '2':
            wifi.run()  # Предполагается, что в wifi.py есть функция run()
        elif choice == '3':
            port.run()  # Предполагается, что в port.py есть функция run()
        elif choice == '4':
            logi.run()  # Предполагается, что в logi.py есть функция run()
        elif choice == '5':
            bezopasnot.run()  # Предполагается, что в bezopasnot.py есть функция run()
        elif choice == "6":
            bio.run()
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер от 0 до 5.")

if __name__ == "__main__":
    main()

