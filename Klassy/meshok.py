import random


class Pustoy_Meshok(Exception): # Если мешок пустой

    def __str__(self): #  Приводим к строчному виду
        return 'В мешке больше нет чисел'


class Meshok: # Мешок с бочонками

    def __init__(self, bochonki): # Инициализируем бочонки
        self._chisla = list(range(1, bochonki + 1)) # Закрываем доступ

    def __len__(self): # Длина
        return len(self._chisla)

    def random_chisla(self, bochonki): # Генератор случайных чисел
        result = random.sample(self._chisla, bochonki)
        return result

    def next_chislo(self): # Получаем следующее число
        try:
            result = random.choice(self._chisla)
        except IndexError:
            raise Pustoy_Meshok
        else:
            self._chisla.remove(result)
            return result