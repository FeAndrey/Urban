class Shop:
    # Инкапсулированный атрибут __file_name = 'products.txt'.
    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name
        self.file = ''
        self.data = ''

    def get_products(self):
        self.file = open(self.__file_name,'r')
        # здесь не понятно с заданием: написано - Возвращает единую строку со всеми товарами из файла __file_name.
        #(что бы так сделать нужно раскоментировать код), а в - Вывод на консоль, строки выводятся через \n
        self.data = self.file.read()#.replace('\r\n', '\n').replace('\n', ', ')
        self.file.close()
        return  self.data

    def add(self, *products):
        # self.file = open(self.__file_name, 'r')
        self.data = self.get_products()
        # print('***********',self.data)
        for i in range(len(products)):
            if int(self.data.find(products[i].name) == -1):
                self.file = open(self.__file_name, 'a')
                self.file.write(products[i].name + ', ' + str(products[i].weight) + ', ' + products[i].category + '\n')
                self.file.close()
            else:
                print(f'Продукт {products[i].name} уже есть в магазине')


class Product:
    def __init__(self, name = str, weight = float, category = str):
        self.name =name
        self.weight =weight
        self.category = category
    def __str__(self):
        return str(self.name) +', ' + str(self.weight) +', ' + str(self.category)



if __name__ == "__main__":

    # # Пример работы программы:
    # s1 = Shop()
    # s1.get_products()
    #
    # p1 = Product('Potato', 50.5, 'Vegetables')
    # p2 = Product('Spaghetti', 3.4, 'Groceries')
    # p3 = Product('Potato', 5.5, 'Vegetables')
    # p4 = Product('milk', 1.8, 'Groceries')
    # p5 = Product('banana', 8, 'Fruit')
    # print(p2) # __str__
    # #
    # s1.add(p1,p2, p3)
    # s1.add(p4, p5)
    # s1.add(p3, p1)
    # print(s1.get_products())

    # Пример работы программы:
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2) # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())
