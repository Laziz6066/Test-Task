from typing import List


def display_page(entries: List[str], page_num: int, entries_per_page: int) -> None:
    """
        Выводит страницу записей на экран.

        :param entries: Список записей в справочнике.
        :param page_num: Номер текущей страницы.
        :param entries_per_page: Количество записей на странице.
        """

    start_index = (page_num - 1) * entries_per_page
    end_index = min(start_index + entries_per_page, len(entries))

    for i in range(start_index, end_index):
        if i < len(entries):
            print(f"{i + 1}. {entries[i].strip()}")


def add_entry(entries: List[str]) -> None:
    """
    Добавляет новую запись в справочник.

    :param entries: Список записей в справочнике.
    """

    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    organization = input("Организация: ")
    work_phone = input("Рабочий телефон: ")
    personal_phone = input("Личный телефон: ")

    new_entry = f"{last_name}:{first_name}:{middle_name}:{organization}:{work_phone}:{personal_phone}\n"
    entries.append(new_entry)

    with open("phonebook.txt", "a") as file:
        file.write(new_entry)

    print("Запись добавлена.")


def edit_entry(entries: List[str]) -> None:
    """
    Редактирует существующую запись в справочнике.

    :param entries: Список записей в справочнике.
    """

    display_entries(entries)

    entry_index = int(input("Введите номер записи для редактирования: ")) - 1

    if 0 <= entry_index < len(entries):
        entry = entries[entry_index].split(":")
        print("Текущая запись:")
        print(f"1. Фамилия: {entry[0]}")
        print(f"2. Имя: {entry[1]}")
        print(f"3. Отчество: {entry[2]}")
        print(f"4. Организация: {entry[3]}")
        print(f"5. Рабочий телефон: {entry[4]}")
        print(f"6. Личный телефон: {entry[5]}")

        field_to_edit = int(input("Введите номер поля для редактирования: "))
        new_value = input("Введите новое значение: ")

        if 1 <= field_to_edit <= 6:
            entry[field_to_edit - 1] = new_value
            entries[entry_index] = ":".join(entry) + "\n"

            with open("phonebook.txt", "w") as file:
                file.writelines(entries)

            print("Запись успешно отредактирована.")
        else:
            print("Неправильный номер поля.")
    else:
        print("Неправильный номер записи.")


def display_entries(entries: List[str]) -> None:
    """
    Выводит все записи на экран.

    :param entries: Список записей в справочнике.
    """

    for i, entry in enumerate(entries):
        fields = entry.split(":")
        print(f"{i + 1}. Фамилия: {fields[0]}, Имя: {fields[1]}, Отчество: {fields[2]}")


def search_entries(entries: List[str]) -> None:
    """
    Ищет записи по заданным критериям.

    :param entries: Список записей в справочнике.
    """

    print("Выберите критерии поиска:")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    organization = input("Организация: ")

    matching_entries = []

    for entry in entries:
        fields = entry.split(":")
        if (last_name in fields[0]) and (first_name in fields[1]) and (middle_name in fields[2]) and (organization in fields[3]):
            matching_entries.append(entry.strip())

    if matching_entries:
        print("Найденные записи:")
        for i, match in enumerate(matching_entries):
            print(f"{i + 1}. {match}")
    else:
        print("Записи не найдены.")


def main() -> None:
    """
    Основная функция для запуска программы.
    """

    entries = []

    # Загрузка данных из файла
    with open("phonebook.txt", "r") as file:
        entries = file.readlines()

    while True:
        print("\nТелефонный справочник")
        print("1. Вывести записи")
        print("2. Добавить новую запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            page_num = 1
            entries_per_page = 5

            while True:
                print("\nЗаписи:")
                display_page(entries, page_num, entries_per_page)

                print("\n1. Следующая страница")
                print("2. Предыдущая страница")
                print("3. Вернуться в меню")

                page_choice = input("Выберите действие: ")

                if page_choice == "1":
                    page_num += 1
                elif page_choice == "2":
                    if page_num >= 2:
                        page_num -= 1
                else:
                    break
        elif choice == "2":
            add_entry(entries)
        elif choice == "3":
            edit_entry(entries)
        elif choice == "4":
            search_entries(entries)
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
