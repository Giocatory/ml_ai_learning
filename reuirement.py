import subprocess

# Получаем список всех установленных пакетов с помощью команды pip freeze
result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)

# Открываем файл requirements.txt для записи
with open('requirements2.txt', 'w') as f:
    # Записываем список пакетов в файл requirements.txt
    f.write(result.stdout.decode('utf-8'))