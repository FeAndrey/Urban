import io

def custom_write (file_name, strings):
    strings_positions = dict()

    file = open(file_name, "w", encoding='utf-8')
    for i in range(len(strings)):
        strings_tuple = (i+1, file.tell())
        file.write(strings[i] + '\n')
        strings_positions [strings_tuple] = strings[i]
    file.close()
    return strings_positions

if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('test.txt', info)
    for elem in result.items():
      print(elem)

