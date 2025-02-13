import re
print("Вбейте логи в файл scanner.log ")
def parse_log_file(log_file):
    vulnerabilities = []
    errors = []

    with open(log_file, 'r') as file:
        for line in file:
            # Ищем строки с уязвимостями
            if "[!]" in line:
                vulnerabilities.append(line.strip())
            # Ищем строки с ошибками
            elif "Error" in line:
                errors.append(line.strip())

    return vulnerabilities, errors

def display_results(vulnerabilities, errors):
    if vulnerabilities:
        print("\nНайденные уязвимости:")
        for vuln in vulnerabilities:
            print(vuln)
    else:
        print("\nУязвимости не найдены.")

    if errors:
        print("\nОшибки:")
        for error in errors:
            print(error)
    else:
        print("\nОшибок не найдено.")

def run():
    log_file = 'vuln_scanner.log'  # Укажите ваш файл логов
    vulnerabilities, errors = parse_log_file(log_file)
    display_results(vulnerabilities, errors)

