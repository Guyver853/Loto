from Klassy.meshok import Meshok
from Klassy.card import Card
from Klassy.igrok import sozdanie_igroka


def prodoljit_igru(igroki):
    for item in igroki:
        if not (item.pobeditel is None):
            return False
    return True


# создаем мешок

meshok = Meshok(90)
kol_vo_igrokov = int(input('Введите количество игроков: '))

# Создаем игроков и даем им карточки

igroki = []
for i in range(kol_vo_igrokov):
    # Имя игрока
    imya = input(f'Введите имя игрока {i + 1}')
    # Тип игрока
    tip_igroka = input(f'Введите тип игрока: Komputer - 1, Chelovek - 0')
    # Карточка
    card = Card(meshok.random_chisla(15))
    # создаем игрока
    igrok = sozdanie_igroka(imya, tip_igroka, card)
    igroki.append(igrok)

# Играем до Победителя, это значит что у всех pobeditel = None

while prodoljit_igru(igroki):
    # Цикл игры
    # У каждого игрока рисуем карточку и он делает ход
    # номер появляется из мешка
    chislo = meshok.next_chislo()
    print(f'Следующий Номер: {chislo}')
    for igrok in igroki:

        # Рисуем карточку
        # print(igrok.card)
        print(f'Карточка игрока {igrok.imya}')
        # igrok.card.show_numbers()
        print(igrok.card)
        igrok.hod(chislo)

# Объявляем победителей и проигравших
# Что будет если 1 выиграл, другой проиграл?
# Может одновременно несколько игроков проиграть
# Несколько игроков выиграть
# Может 1 проиграть, другой выиграть
# Может кто то проиграть а кто то оставаться в игре

# Проверяем победителей

# TODO: переписать компактнее
pobedivshiy = False
proigravshiy = False
for igrok in igroki:
    if igrok.pobeditel is None:
        pass
    else:
        if igrok.pobeditel:
            pobedivshiy = True
        else:
            proigravshiy = True

# Выводим результат
# Все оставшиеся будут проигравшими если pobedivshiy

if pobedivshiy:
    for igrok in igroki:
        if igrok.pobeditel:
            print(igrok.imya, 'Победил!')
        else:
            print(igrok.imya, 'Проиграл!')
elif proigravshiy:

    # Есть проигравший

    for igrok in igroki:
        if igrok.pobeditel is None:
            print(igrok.imya, 'Победил!')
        else:
            print(igrok.imya, 'Проиграл!')
else:
    print('Что то пошло не по правилам')