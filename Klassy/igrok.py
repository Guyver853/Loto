class Komputer:

    def __init__(self, imya, card): # Инициализируем игрока Компьютер
        self.imya = imya
        self.card = card
        # True - победитель, False - проигравший, None - еще играет
        self.pobeditel = None

    def hod(self, chislo): # Что делает игрок в очередной ход
        if chislo in self.card:
            self.card.zacherknuto(chislo)
            # Комп всегда зачеркивает
            if self.card.pustota():
                self.pobeditel = True


class Chelovek(Komputer): # Наследуемся от Компьютер

    def hod(self, chislo):
        vopros = input('Зачеркнуть? y/n')
        if vopros == 'y':
            # Если число есть в карточке - зачеркиваем
            if chislo in self.card:
                self.card.zacherknuto(chislo)
                # Если он все зачеркнул, то он выиграл
                if self.card.pustota():
                    self.pobeditel = True
            else:
                # А если числа нет, то он проиграл
                self.pobeditel = False
        else:
            # Это ответ нет
            # Если число есть в карточке - то он проиграл
            if chislo in self.card:
                self.pobeditel = False
            # Если не зачеркнул то игра продолжается


def sozdanie_igroka(imya, tip_igroka, card):
    igroki = {
        '1': Komputer,
        '0': Chelovek
    }

    igrok = igroki[tip_igroka](imya, card)
    return igrok