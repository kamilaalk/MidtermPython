import csv
import os
from datetime import datetime

FILENAME = 'notes.csv'

def load_notes():
    notes = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                notes.append(row)
    return notes

def save_notes(notes):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body', 'timestamp'], delimiter=';')
        writer.writeheader()
        writer.writerows(notes)

def add_note():
    notes = load_notes()
    note_id = str(len(notes) + 1)
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes.append({'id': note_id, 'title': title, 'body': body, 'timestamp': timestamp})
    save_notes(notes)
    print("Заметка добавлена.")

def edit_note():
    notes = load_notes()
    note_id = input("Введите ID заметки для редактирования: ")
    for note in notes:
        if note['id'] == note_id:
            title = input(f"Новый заголовок (текущий: {note['title']}): ")
            body = input(f"Новый текст (текущий: {note['body']}): ")
            note['title'] = title if title else note['title']
            note['body'] = body if body else note['body']
            note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print("Заметка обновлена.")
            return
    print("Заметка с таким ID не найдена.")

def delete_note():
    notes = load_notes()
    note_id = input("Введите ID заметки для удаления: ")
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка удалена.")

def view_notes():
    notes = load_notes()
    if not notes:
        print("Нет заметок для отображения.")
        return
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/Время: {note['timestamp']}")
        print("-" * 40)

from datetime import datetime, timedelta

def view_notes_today():
    notes = load_notes()
    if not notes:
        print("Нет заметок для отображения.")
        return

    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)

    filtered_notes = [
        note for note in notes
        if today_start <= datetime.strptime(note['timestamp'], '%Y-%m-%d %H:%M:%S') <= today_end
    ]

    if not filtered_notes:
        print("Нет заметок за сегодняшний день.")
        return
    
    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/Время: {note['timestamp']}")
        print("-" * 40)




def main():
    while True:
        print("Меню:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Просмотреть все заметки")
        print("5. Просмотреть заметки по дате \n(Заметки, записанные сегодня, можно найти по дате следующего дня)")
        print("6. Выход")
        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            view_notes()
        elif choice == '5':
            view_notes_by_date()
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
