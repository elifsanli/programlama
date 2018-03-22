satismiktari=500
birimsatisfiyati=20
ciro=5000
i=1
while True :
    satismiktari=satismiktari+200
    birimsatisfiyati=birimsatisfiyati+10
    ciro=satismiktari*birimsatisfiyati
    i=i+1
    if(ciro>=500000):
        print(i,"yıl sonra 500000 ciro elde edersiniz.")
        break
