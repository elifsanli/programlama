x=int(input("Finansman Gelirlerini Giriniz."))
y=int(input("Pazar gelirlerini Giriniz."))
z=int(input("Kira Gelirlerini Giriniz."))
t=int(input("Ücreti giriniz."))
k=int(input("Finansman Giderlerini Giriniz."))
l=int(input("Kira Giderlerini Giriniz."))
m=int(input("Muhasebe giderlerini giriniz."))
if (x+y+z)-(t+k+l+m)>1000:
    print("İşletmeniz Karlıdır.")
else:
    print("İşletme Zarardadır.")


#a=planlanmisÜretim, b=plansizDurus
def kullanilabilirlikHesapla(a,b):
    kullanilabilirlik=(a-b)/a
    return kullanilabilirlik
#c=standartCevrim, d=üretimMiktari, e=planlanmisÜretim, f=plansizDurus
def performansHesapla(c,d,e,f):
    performans=(c*d)/(e-f)
    return performans
#g=saglamÜrün, h=toplamÜretim
def kalitehesapla(g,h):
    kalite=(g/h)
    return kalite
#OEE=ekipmanEtkinlikOrani
def OEEHesapla(kullanilabilirlik,performans,kalite):
    OEE=(kullanilabilirlik*performans*kalite)/100
    return OEE

def ciroHesapla():
    x=int(input("Satış miktarını giriniz."))
    y=int(input("Birim satış miktarını giriniz."))
    ciro=(x*y)
    return ciro
def adambasiciroHesapla():
    z=int(input("Toplam ciroyu giriniz"))
    t=int(input("toplam çalışan sayısını giriniz"))
    adambasiciro=(z/t)
    return adambasiciro



    


    


    
