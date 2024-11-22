import sys

def load_ascii_art(filename):
    """
    Загружает ASCII-арт символов из файла в словарь.
    :param filename: Путь к файлу с ASCII-арт шаблонами.
    :return: Словарь, где ключ — символ, значение — список строк (ASCII-арт символа).
    """
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    symbol_dict = {}
    current_symbol = []
    current_symbol_code = 32  # ASCII код для пробела

    for line in lines:
        if len(line) == 0:  # Разделение символов пустой строкой
            if current_symbol:
                symbol_dict[chr(current_symbol_code)] = current_symbol
                current_symbol = []
                current_symbol_code += 1
        else:
            current_symbol.append(line.rstrip('\n'))

    # Добавить последний символ, если он не был добавлен
    if current_symbol:
        symbol_dict[chr(current_symbol_code)] = current_symbol

    return symbol_dict

def print_ascii_art(text, symbol_dict):
    """
    Выводит текст в формате ASCII-арт.
    :param text: Строка для преобразования.
    :param symbol_dict: Словарь с ASCII-арт символами.
    """
    # Разделить строки ASCII-арта для каждого символа
    ascii_lines = zip(*(symbol_dict.get(char, [' ' * 8]) for char in text))

    # Напечатать строки ASCII-арта
    for line in ascii_lines:
        print(' '.join(line))

def main():
    """
    Основная функция программы.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    try:
        symbol_dict = load_ascii_art('standard.')  # Загрузка шаблонов ASCII-арта
    except FileNotFoundError:
        print("Error: File 'standard.txt' not found.")
        sys.exit(1)

    # Обработка строк с переносами \n
    for line in text.split('\n'):
        print_ascii_art(line, symbol_dict)
        print()  # Разделение строк

if __name__ == "__main__":
    main()
