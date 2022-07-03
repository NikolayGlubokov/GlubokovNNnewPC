def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print('Ваши данные'.center(50, '='))
            output=func(*args, **kwargs)
            print('=' * 50)
            return output
        return wrap
    return wrapper





class UserInterface:
    @add_title('Ввод данных')
    def wait_user_answer(self):

        print('Работа карточки фильма:')
        print('1 - Создать карточку для нового фильма')
        print('2 - Вся картотека')
        print('3 - Поиск карточки фильма по названию')
        print('4 - удаление карточки фильма')
        print('q - выход из программы')
        user_answer=input('Ваш выбор: ')
        print('='*50)
        return user_answer
    @add_title("Создание карточки фильма")
    def add_user_article(self):
        dict_article={
            'Название фильма: ': None,
            'Жанр: ': None,
            'Режиссер: ': None,
            'Год: ': None,
            'Длительность: ': None,
            'Студия: ': None,
            'Актёры: ': None
        }
        for key in dict_article:
            dict_article[key] = input(f'Введите пункт {key} карточки: ')
        print('=' * 50)
        return dict_article

    @add_title('Ваша библиотека фильмов')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f'{ind}. {article}')
        print('='*50)
    @add_title('Введение названия фильма')
    def get_user_article(self):
        user_article=input('Название фильма: ')
        return user_article
    @add_title('Вывод карточки фильма')
    def show_single_article(self, article):
        for key in article:
            print(f'{key} - {article[key]}')

    @add_title('Сообщение об ошибке поиска')
    def show_incorretc_title_error(self, user_title):
        print(f'Данной карточки фильма с названием {user_title} нет в вашей библиотеке')

    @add_title('Удаление карточки фильма')
    def remove_single_article(self, article):
        print(f'Карточка фильма {article} была удалена')
    @add_title('Выход за грани фунуционала программы')
    def show_incorrect_answer_error(self,answer):
        print(f'Программой не предусмотрено выполнение варианта {answer}')
