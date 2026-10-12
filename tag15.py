def gc_hesapla(dna):
    g = dna.count("G")
    c = dna.count("C")
    return(g + c) / len(dna) * 100
try:
    with open("dizi.txt") as dosya :
        with open("rapor.txt","w") as rapor:
            for satir in dosya:
                dizi = satir.strip()
                gc = round(gc_hesapla(dizi),1)
                rapor.write(dizi + " " + str(gc)+"\n")
    print("Rapor hazır:rapor.txt")
except FileNotfoundError :
    print("dizi.txt bulunumadı,dosya adını kontrol et")
        

