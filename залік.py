import sqlite3

def create_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        description TEXT,
                        deadline DATE,
                        status TEXT)''')
    conn.commit()
    conn.close()

def add_task():
    title = input("Введіть назву задачі: ")
    description = input("Введіть опис задачі: ")
    deadline = input("Введіть дедлайн (YYYY-MM-DD): ")
    status = input("Введіть статус (за замовчуванням 'Pending'): ") or "Pending"

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO tasks (title, description, deadline, status)
                      VALUES (?, ?, ?, ?)''', (title, description, deadline, status))
    conn.commit()
    conn.close()
    print("Задача додана!")

def view_tasks():
    sort = input("Сортувати за дедлайном? (y/n): ").lower() == 'y'

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY deadline' if sort else 'SELECT * FROM tasks')
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            print(f"\nID: {task[0]}\nНазва: {task[1]}\nОпис: {task[2]}\nДедлайн: {task[3]}\nСтатус: {task[4]}")
    else:
        print("Задачі не знайдено.")
    conn.close()

def edit_task():
    task_id = int(input("Введіть ID задачі для редагування: "))
    title = input("Нова назва (залишити порожнім, якщо без змін): ")
    description = input("Новий опис: ")
    deadline = input("Новий дедлайн (YYYY-MM-DD): ")
    status = input("Новий статус: ")

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    if title:
        cursor.execute('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))
    if description:
        cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
    if deadline:
        cursor.execute('UPDATE tasks SET deadline = ? WHERE id = ?', (deadline, task_id))
    if status:
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
    conn.commit()
    conn.close()
    print("Задача оновлена!")

def delete_task():
    task_id = int(input("Введіть ID задачі для видалення: "))
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Задача видалена!")

def main():
    create_db()
    while True:
        print("\n Менеджер задач")
        print("1. Додати задачу")
        print("2. Переглянути задачі")
        print("3. Редагувати задачу")
        print("4. Видалити задачу")
        print("5. Вихід")

        choice = input("Оберіть опцію (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == '__main__':
    main()
