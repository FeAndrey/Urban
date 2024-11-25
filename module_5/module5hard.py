import time

class UrTube:
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    # добавление объектов Video в список
    def add(self, *args):
        for i in range(len(args)):
            if args[i] in self.videos:
                pass
            else:
                self.videos.append(args[i])

    # добавление объектов User в список (для тестов)
    def add_users(self, *args):
        for i in range(len(args)):
            if args[i] in self.users:
                pass
            else:
                self.users.append(args[i])

    # поиск видео файла в списке объектов независимо от регистра
    def get_videos(self, search):
        search_list = []
        search = search.lower()
        for i in range(len(self.videos)):
            if search in self.videos[i].title.lower():
                search_list.append(self.videos[i].title)
        return search_list

    # просмотр видео при условии, 18+
    def watch_video(self, watch_title):
        for i in range(len(self.videos)):
            if watch_title in self.videos[i].title:
                vid = self.videos[i]
                if self.current_user != None:
                    if self.current_user.age > 18 and self.videos[i].adult_mode == True:
                        while vid.time_now < vid.duration:
                            pass
                            vid.time_now +=1
                            time.sleep(1)
                            print(vid.time_now)
                        print('Конец видео')
                    else:
                        print(f'{self.current_user.nickname}, Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')

    # регистрация пользователя по условиям
    def register(self, nickname, password, age):
        temp_user = User(nickname, password, age)
        flag = True
        if self.users == []:    # если первый элемент списка пустой, то всегда регистрируем без всех проверок
            self.users.append(temp_user)
            self.log_in(nickname, password)
            return
        for i in range(len(self.users)):    # проверка на есть такой пользователь в списке
            if nickname in self.users[i].nickname:
                print(f'Пользователь, {nickname}, уже существует.')
                flag = False
                break
        if  flag:   # если пользователя нет в списке, то регистрируем и логинимся
            self.users.append(temp_user)
            self.log_in(nickname, password)

    # вход пользователя
    def log_in(self, nickname, password):
        if self.current_user != None:   # выход всегда, когда заново логинимся
            self.log_out()
        for i in range(len(self.users)):    # если такой пользователь есть, то логиним его, так же его в current_user
            if nickname in self.users[i].nickname:
                if hash(password) == self.users[i].password:
                    self.current_user = self.users[i]
                    break
        if self.current_user == None:
            print(f'Пользователь {nickname} не найден')
        else:
            print(f'Пользователь, {nickname}, залогинился.')

    # Метод log_out для сброса текущего пользователя на None.
    def log_out(self):
        self.current_user = None
        print('Пользователь вышел')

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now =time_now
        self.adult_mode = adult_mode

    def __str__(self):
        if self.adult_mode == True:
            return f'{self.title}, (18+)'
        else:
            return f'{self.title}'

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    # def __eq__(self, other):
    #     return self.password == other.password
    def __hash__(self):
        return hash(self.password)
    def __str__(self):
        return f'{self.nickname}-{self.age}ears, хэш_пароль - {self.password}'

#ЗАДАНИЕ
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# #ТЕСТЫ
# us1 = User('admin', '123', 40)
# us3 = User('user3', '1234', 25)
# us2 = User('user2', '54964', 35)
# us4 = User('user4', '145165', 16)
# us5 = User('user5', '123851', 17)
# v1 = Video('Лучший язык программирования 2024 года', 12)
# v2 = Video('Для чего девушкам парень программист?', 8, adult_mode=True)
# v3 = Video('Хакеры', 14)
# v4 = Video('Хоттабыч лучший программист', 11)
# v5 = Video('Крепкий орешеГ', 5, adult_mode=True)
# v6 = Video('Тоска', 3)
#
# ur1 = UrTube()
#
# # Добавление в список пользователей
# ur1.add_users(us1, us4, us3, us5)
# ur1.add_users(us2, us4, us5)
# # Добавление в список видео
# ur1.add(v1, v2, v1, v2, v1, v4)
# ur1.add(v3, v2, v1,v4)
# ur1.add(v3, v2, v6, v4, v5, v4)
#
# # Проверка логина и пароля
# print('\n*********** Вход/Регистрация *******************')
# ur1.log_in('admin', '12345')
# ur1.log_in('werwer', '12345')
# ur1.log_in('user5', '123851')
# ur1.log_in('user4', '145165')
# # Проверка регистрации
# ur1.register('user7', '54964', 40)
# ur1.register('user6', '234234234', 17)
#
# # Проверка поиска
# print('\n************** Поиск ***************************')
# print(ur1.get_videos('лучший'))
# print(ur1.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# print('\n************ Проверка на возраст ********************')
# ur1.watch_video('Для чего девушкам парень программист?')
# ur1.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur1.watch_video('Для чего девушкам парень программист?')
# ur1.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 11)
# ur1.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur1.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
#
# # Попытка воспроизведения несуществующего видео
# ur1.watch_video('Лучший язык программирования 2024 года!')
#
# print('\n\n\n************** Текущий пользователь *****************')
# print('current_user - ', ur1.current_user)
# print('\n*********** Список Users ****************************')
# for i in range(len(ur1.users)):
#     print(f'Users{i} - {ur1.users[i]}')
# print('\n*********** Список Videos ***************************')
# for i in range(len(ur1.videos)):
#     print(f'Videos{i} - {ur1.videos[i]}')