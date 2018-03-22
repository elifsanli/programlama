i=0
while True:
    a=int(input("Bir sayı giriniz.0'a basarak çıkış yapabilirsiniz"))
    if(a==0):
        print("Çıkış yaptınız!")
        break
    else:
        i=i+a%3
        print("sayını 3'e bölümünden kalanlar toplamı:",i)
