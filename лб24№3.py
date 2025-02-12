from datetime import datetime

def get_weekday_from_date():
    date_str = input("Введіть дату (у форматі РРРР-ММ-ДД): ")
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"День тижня: {date_obj.strftime('%A')}")
    except ValueError:
        print("Невірний формат дати. Будь ласка, введіть у форматі РРРР-ММ-ДД.")

# Виклик функції
get_weekday_from_date()