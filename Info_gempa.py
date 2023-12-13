from Gempa import *

banten = Gempa('Banten', 1.2)
palu = Gempa('Palu', 6.1 )
cianjur = Gempa('Cianjur', 5.6)
jayapura = Gempa('Jayapura', 3.3)
garut = Gempa('Garut', 4.0)



banten.cetak()
print("Dampak gempa\t: ", banten.dampak())
palu.cetak()
print("Dampak gempa\t: ", palu.dampak())
cianjur.cetak()
print("Dampak gempa\t: ", cianjur.dampak())
jayapura.cetak()
print("Dampak gempa\t: ", jayapura.dampak())
garut.cetak()
print("Dampak gempa\t:", garut.dampak())

