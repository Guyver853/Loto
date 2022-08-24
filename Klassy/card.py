class Chislo_Zacherk: # Класс для хранения числа, которое может быть зачёркнуто

    def __init__(self, chislo): # Инициализатор
        self.chislo = chislo
        self.zacherk = False # По умолчанию не зачёркнуто

    def __str__(self): # Зачёркиваем если надо
        return '-' if self.zacherk else str(self.chislo)

    def __gt__(self, new_chislo): # Сравнение a > b
        return self.chislo > new_chislo.chislo

    def __eq__(self, new_chislo): # Сравнение двух объектов
        return self.chislo == new_chislo.chislo


class Net_Chisla_Zacherk(ValueError): # Класс, если нет зачеркнутого числа

    def __init__(self, chislo): # Инициализируем
        self.chislo = chislo

    def __str__(self): # Приводим к строке
        return f'В карточке нет числа {self.chislo}'


class Card:

    def __init__(self, chisla): # Инициализируем
        """
        :param chisla: 15 чисел
        """
        chisla = [Chislo_Zacherk(item) for item in chisla]
        self.chisla = chisla


    # def show_numbers(self):
    #     for number in self.numbers:
    #         print(number)



    def __str__(self): # Приводим к строковому виду. 3 строки по 5 чисел
        stroka1 = sorted(self.chisla[:5])
        stroka2 = sorted(self.chisla[5:10])
        stroka3 = sorted(self.chisla[10:])
        # TODO: Как избавиться от дублирования row
        result = f"""
        --------------------------
            {stroka1[0]} {stroka1[1]} {stroka1[2]}          {stroka1[3]} {stroka1[4]}
         {stroka2[0]}    {stroka2[1]}    {stroka2[2]} {stroka2[3]}    {stroka2[4]}
           {stroka3[0]} {stroka3[1]} {stroka3[2]}     {stroka3[3]}      {stroka3[4]}
        --------------------------
        """
        return result

    def pustota(self): # Проверка, зачеркнуты ли все цифры
        for item in self.chisla:
            if not item.zacherk:
                return False
        return True

    def __contains__(self, item):# Проверка на вхождение числа в числах карточки
        if isinstance(item, int):
            item = Chislo_Zacherk(item)
        return item in self.chisla

    def zacherknuto(self, chislo): # Зачеркнуто ли число
        if isinstance(chislo, int):
            chislo = Chislo_Zacherk(chislo)
        try:
            index = self.chisla.index(chislo)
        except ValueError:
            raise Net_Chisla_Zacherk(chislo)
        else:
            self.chisla[index].zacherk = True