from pytest import raises
from Klassy.card import Card, Chislo_Zacherk, Net_Chisla_Zacherk


class TestChislo_Zacherk:

    def setup(self): # Вводим 3 и другое число
        self.chislo = Chislo_Zacherk(3)
        self.new_chislo = Chislo_Zacherk(4)

    def test_str(self): #  Проверка есть ли 3 в карточке,и зачёркиваем
        assert str(self.chislo) == '3'
        self.chislo.zacherk = True
        assert str(self.chislo) == '-'

    def test_gt_lt(self): # Сравниваем числа на больше меньше
        assert self.new_chislo > self.chislo
        assert self.chislo < self.new_chislo

    def test_eq(self): #
        eq_number = Chislo_Zacherk(3)
        assert eq_number == self.chislo
        assert self.new_chislo != self.chislo


class TestCard:

    def setup(self): #
        self.chisla_karty = [9, 43, 62, 74, 90, 2, 27, 75, 78, 82, 41, 56, 63, 76, 86]
        self.card = Card(self.chisla_karty)

    def test_pustota(self): #
        assert not self.card.pustota()
        # Если вычеркнуть все чифры?
        for item in self.chisla_karty:
            self.card.zacherknuto(item)

        assert self.card.pustota()

    def test_str(self): # Сравниваем строки карточек
        result = """
        --------------------------
            9 43 62          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert result == str(self.card)

    def test_contains(self): # Проверяем числа на вхождение
        assert 9 in self.card
        assert 99 not in self.card
        assert Chislo_Zacherk(9) in self.card
        assert Chislo_Zacherk(99) not in self.card

    def test_zacherknuto(self): # Проверка зачеркнутых чисел
        # Зачеркиваем число которое есть
        self.card.zacherknuto(43)
        result = """
        --------------------------
            9 - 62          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert str(self.card) == result

        self.card.zacherknuto(Chislo_Zacherk(62))
        result = """
        --------------------------
            9 - -          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert str(self.card) == result

        # В карточке нет такого числа
        with raises(Net_Chisla_Zacherk):
            self.card.zacherknuto(Chislo_Zacherk(99))