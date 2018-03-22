gunlukuretilen=200
gunlukdefoluurun=0
toplamdefoluurun=0
i=0
while(gunlukdefoluurun<gunlukuretilen*0.20):
    gunlukdefoluurun=int(input("Günlük defolu ürün miktari:"))
    toplamdefoluurun=toplamdefoluurun+gunlukdefoluurun
    i=i+1
    if(gunlukdefoluurun>gunlukuretilen*0.20):
        print("defolu ürün sayısı limiti aştı")
        break
    print(i,"Günlük","defolu ürün sayısı:",toplamdefoluurun)
