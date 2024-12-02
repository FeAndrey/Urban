import io

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)
        self.file = ''

    def get_all_words(self):
        all_words = dict()
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']      # список исключений пунктуации из строки
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as self.file:
                data = self.file.read().lower().replace('\r\n', '\n').replace('\n', '')
            for j in range(len(punct)):     # убираем пунктуацию
                data = data.replace(punct[j], ' ')
            all_words [self.file_names[i]] = data.split()   # создаем необходимы словарь
        return all_words

    # Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        quantity = 0
        dict_name_position = dict()
        for name, words in self.get_all_words().items():
            for i in words:
                quantity +=1
                if i == word.lower():    # если находим слово, то прерываем перебор
                    break
            if str(words).find(word.lower()) == -1:     # условие если нет искомого слова в файле, то пропускаем
                continue
            dict_name_position[name] = quantity  # создаем необходимы словарь
            quantity = 0  # обнуляем счетчик для следующего файла
        return dict_name_position

    # Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
    def count(self, word):
        quantity = 0
        dict_name_quantity = dict()
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    quantity +=1         # счетчик количества слов
            if str(words).find(word.lower()) == -1:  # условие если нет искомого слова в файле, то пропускаем
                continue
            dict_name_quantity[name] = quantity  # создаем необходимы словарь
            quantity=0       # обнуляем счетчик для следующего файла
        return dict_name_quantity



if __name__ == "__main__":
    pass

    finder2 = WordsFinder('test_file.txt', 'test_file2.txt', 'test_file3.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего
