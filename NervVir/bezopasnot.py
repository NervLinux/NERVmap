import os
import subprocess

def check_updates():
    print("Проверка наличия обновлений...")
    try:
        # Для Ubuntu/Debian
        result = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)
        if result.stdout:
            print("Доступные обновления:\n", result.stdout)
        else:
            print("Все пакеты обновлены.")
    except Exception as e:
        print(f"Ошибка при проверке обновлений: {e}")

def check_ssh_settings():
    print("Проверка настроек SSH...")
    try:
        with open('/etc/ssh/sshd_config', 'r') as file:
            config = file.read()
            if 'PasswordAuthentication no' in config:
                print("Использование аутентификации по паролю отключено.")
            else:
                print("Включена аутентификация по паролю. Рекомендуется отключить.")
    except Exception as e:
        print(f"Ошибка при проверке настроек SSH: {e}")

def check_firewall():
    print("Проверка настроек брандмауэра...")
    try:
        result = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
        print("Статус брандмауэра:\n", result.stdout)
    except Exception as e:
        print(f"Ошибка при проверке брандмауэра: {e}")

def check_unnecessary_services():
    print("Проверка ненужных служб...")
    try:
        result = subprocess.run(['systemctl', 'list-units', '--type=service', '--state=running'], capture_output=True, text=True)
        print("Запущенные службы:\n", result.stdout)
    except Exception as e:
        print(f"Ошибка при проверке служб: {e}")

def run():
    print("Запуск проверки конфигурации безопасности...")
    check_updates()
    check_ssh_settings()
    check_firewall()
    check_unnecessary_services()
    print("Проверка завершена.")

