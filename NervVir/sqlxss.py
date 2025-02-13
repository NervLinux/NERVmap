# NERV


import requests
import logging

# Настройка логирования
logging.basicConfig(
    filename='vuln_scanner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def check_sql_injection(url):
    payload = "' OR '1'='1"
    logging.info(f"Checking SQL Injection for {url} with payload: {payload}")
    try:
        response = requests.get(url + payload)
        if "error" not in response.text.lower():
            result = f"[!] Potential SQL Injection vulnerability found at {url}"
            print(result)
            logging.info(result)
        else:
            logging.info(f"No SQL Injection vulnerability found at {url}.")
    except requests.RequestException as e:
        logging.error(f"Error checking SQL Injection for {url}: {e}")

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    logging.info(f"Checking XSS for {url} with payload: {payload}")
    try:
        response = requests.get(url + "?search=" + payload)
        if payload in response.text:
            result = f"[!] Potential XSS vulnerability found at {url}"
            print(result)
            logging.info(result)
        else:
            logging.info(f"No XSS vulnerability found at {url}.")
    except requests.RequestException as e:
        logging.error(f"Error checking XSS for {url}: {e}")

def scan(urls, sql_check_enabled, xss_check_enabled):
    for url in urls:
        print(f"Scanning {url}...")
        if sql_check_enabled:
            check_sql_injection(url)
        if xss_check_enabled:
            check_xss(url)

def get_urls_from_user():
    urls = []
    while True:
        url = input("Введите URL для проверки (или нажмите Enter для завершения): ")
        if url == "":
            break
        urls.append(url)
    return urls

def get_check_type():
    print("Выберите тип проверки:")
    print("1 - Проверка на SQL-инъекцию (--sql)")
    print("2 - Проверка на XSS (--xss)")
    choice = input("Введите номер (1 или 2): ")
    return choice

def run():
    urls = get_urls_from_user()
    if not urls:
        print("Не указаны URL для проверки.")
    else:
        choice = get_check_type()
        sql_check_enabled = False
        xss_check_enabled = False

        if choice == '1':
            sql_check_enabled = True
        elif choice == '2':
            xss_check_enabled = True
        else:
            print("Неверный ввод. Пожалуйста, выберите 1 или 2.")
            exit()

        scan(urls, sql_check_enabled, xss_check_enabled)

        # Добавить запись в лог о завершении сканирования
        logging.info("Scanning completed")

