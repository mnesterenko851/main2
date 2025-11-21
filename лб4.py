import sys

class SecureData:
    def __init__(self, public_data, protected_data, private_data):
        object.__setattr__(self, 'public_data', public_data)
        object.__setattr__(self, '_protected_data', protected_data)
        object.__setattr__(self, '__private_data', private_data)
        
        print("\n---  Об'єкт SecureData Створено ---")
        print(f"  public_data: '{public_data}'")
        print(f"  _protected_data: '{protected_data}'")
        print(f"  __private_data: '{private_data}'")
        print("-" * 35)

    def __getattribute__(self, name):
        print(f" [__getattribute__] Спроба доступу до: '{name}'")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print(f" [__getattr__] ПОМИЛКА: Атрибут '{name}' не знайдено.")
        return f"Помилка: Атрибут '{name}' не існує або є приватним."

    def __setattr__(self, name, value):
        print(f" [__setattr__] Спроба встановити: '{name}' = '{value}'")
        
        if name == '__private_data' or name == '_SecureData__private_data':
            print(f" [__setattr__] ВІДМОВЛЕНО: Зміна приватного атрибуту заборонена.")
        else:
            print(f" [__setattr__] ДОЗВОЛЕНО: Значення '{name}' оновлено.")
            object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f" [__delattr__] Спроба видалити: '{name}'")
        
        if name == '__private_data' or name == '_SecureData__private_data':
            print(f" [__delattr__] ВІДМОВЛЕНО: Видалення приватного атрибуту заборонено.")
        else:
            print(f" [__delattr__] ДОЗВОЛЕНО: Атрибут '{name}' видалено.")
            object.__delattr__(self, name)

print("=== Створення екземпляру ===")
data = SecureData("публічне", "захищене", "приватне")

print("\n=== 1. Спроба отримати значення атрибутів ===")
print(f"Результат: {data.public_data}")
print(f"Результат: {data._protected_data}")
print(f"Результат: {data.__private_data}")

print("\n=== 2. Зміна значень атрибутів ===")
data.public_data = "нове публічне"
data._protected_data = "нове захищене"
data.__private_data = "нове приватне"

print("\n=== 3. Перевірка нових значень (якщо є) ===")
print(f"Результат (public): {data.public_data}")
print(f"Результат (protected): {data._protected_data}")

print("\n=== 4. Видалення атрибутів ===")
del data.public_data
del data.__private_data

print("\n=== 5. Перевірка видалення ===")
print(f"Результат (public): {data.public_data}")