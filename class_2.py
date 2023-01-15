class Audi:
    def __init__(self, barwa, stan):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = stan
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 14
        self.max_predkosc = 200
        self.poj_baku = 70

    def __str__(self):
        napis = (f'Audi ma kolor {self.kolor} i jest w kondycji {self.kondycja}')
        return napis

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
        return round(zasieg)

    # def ustaw_tryb(self, tryb):
    #     self.tryb = tryb
    #     if self.tryb == 'eco':
    #         self.spalanie_na_100 = 10
    #         self.tryb_ekonomiczny = True
    #         print('Tryb eco')
    #     elif self.tryb == 'normal':
    #         self.spalanie_na_100 = 14
    #         self.tryb_ekonomiczny = False
    #         print('Tryb normal')
    #     else:
    #         print('Tryb nierozpoznany, brak zmian')

    def wlacz_eco(self):
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = True
        print('Tryb eco wlaczony')

    def wlacz_normal(self):
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        print('Tryb normal wlaczony')
        return
    def tankowanie(self, ile_litrow):
        if self.poj_baku <= 5:
            print('za malo zatankowales')
        elif self.poj_baku > 70:
            print('za duzo benzyny')


moje_auto = Audi('czerwony', 3)
print(moje_auto.ilosc_paliwa)
print(moje_auto.kondycja)
# moje_auto.kondycja += 1
print(moje_auto.kondycja)

auto_sasiada = Audi('zielony', 4)
print(auto_sasiada.kondycja)
print(moje_auto)
print(auto_sasiada)
print(moje_auto.wlacz_eco())
print(moje_auto.tankowanie())
