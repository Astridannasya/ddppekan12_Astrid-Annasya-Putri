class Gempa:
    #variabel 
    loc = ''
    sk = 0
    

    #konstruktor 
    def __init__(self,lokasi,skala):
        self.loc = lokasi
        self.sk = skala

    #method
    def dampak(self):
        if self.sk < 2:
            return "Dampak gempa tidak terasa" 
        elif self.sk >=2 and self.sk <= 4: 
            return "Dampak gempa bangunan retak-retak"
        elif self.sk >=4 and self.sk <= 6: 
            return "Dampak gempa bangunan roboh"
        elif self.sk >6:
            return "Dampak gempa bangunan roboh dan berpotensi tsunami"

    def cetak(self):
        print(
        '\n==========================',
        '\nLokasi gempa\t:',self.loc,
        '\nSkala Gempa\t:',self.sk,)