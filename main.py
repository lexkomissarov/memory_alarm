import psutil
import requests

# URL для отправки HTTP запроса
api_url = "https://example.com/api/alarm"

# Порог потребления памяти в процентах, при котором будет сгенерирован аларм
memory_threshold = 90


def check_memory_usage():
    # Получаем информацию о потреблении памяти
    memory_usage = psutil.virtual_memory()

    # Вычисляем процент используемой памяти
    memory_percent = memory_usage.percent

    print(f"Потребление памяти: {memory_percent}%")

    # Если потребление памяти превышает порог, отправляем HTTP запрос
    if memory_percent > memory_threshold:
        send_alarm()


def send_alarm():
    # Отправляем HTTP POST запрос на указанный API
    try:
        response = requests.post(api_url)
        if response.status_code == 200:
            print("HTTP запрос успешно отправлен.")
        else:
            print(f"Ошибка при отправке HTTP запроса. Код ответа: {response.status_code}")
    except Exception as e:
        print(f"Ошибка при отправке HTTP запроса: {e}")


if __name__ == "__main__":
    check_memory_usage()