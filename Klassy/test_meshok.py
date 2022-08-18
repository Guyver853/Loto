from pytest import raises
from Klassy.meshok import Meshok, Pustoy_Meshok


class TestMeshok:

    def setup(self):
        # 1, 2, 3
        self.meshok = Meshok(3)

    def test_init(self):
        # 1, 2, 3
        assert len(self.meshok) == 3
        assert self.meshok._chisla == [1, 2, 3]

    def test_len(self):
        assert len(self.meshok) == 3

    def test_random_chisla(self):
        # чисел столько сколько нужно
        chisla = self.meshok.random_chisla(2)
        assert len(chisla) == 2
        # нет лишних чисел
        # TODO: сделать через set или проще
        for item in chisla:
            assert item in self.meshok._chisla

    def test_next_chislo(self):
        old_chisla = self.meshok._chisla[:]
        number = self.meshok.next_chislo()
        assert len(self.meshok) == 2
        # действительно должен быть в мешке до этого
        assert number in old_chisla

        self.meshok.next_chislo()
        self.meshok.next_chislo()

        # В мешке больше нет номеров
        with raises(Pustoy_Meshok):
            self.meshok.next_chislo()