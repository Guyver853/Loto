from Klassy.igrok import Komputer
from Klassy.card import Card


class TestKomputer:

    def setup(self):
        card = Card([1, 2, 3])
        self.igrok = Komputer('Komp', card)

    def test_hod(self):
        assert self.igrok.pobeditel is None
        self.igrok.hod(1)
        assert self.igrok.pobeditel is None
        self.igrok.hod(10)
        assert self.igrok.pobeditel is None
        self.igrok.hod(2)
        assert self.igrok.pobeditel is None
        self.igrok.hod(3)
        assert self.igrok.pobeditel