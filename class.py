class BMW:
    kolor = 'czerwony'          #zmienne statyczne bo sa wspolne dla calej klasy, kazde auto
    bagaznik = []                   #bedzie mialo ten sam kolor i to samo w bagazniku
    def hamuj(self):
        print('tak hamuje')
        self.skrec('lewo')

    def skrec(self, strona):
        print(f'skrec w {strona}')

    def dodaj(self, a, b):
        return a + b

moje_auto = BMW()
auto_sasiada = BMW()
moje_auto.hamuj()
moje_auto.skrec('lewo')
print(moje_auto.dodaj(5, 8))
moje_auto.bagaznik.append('wiertarka')
moje_auto.bagaznik.append('telefon')
print(moje_auto.bagaznik)
print(auto_sasiada.bagaznik)