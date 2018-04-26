#kasaHesabi=a,alinanCeklerHesabi=b,bankalarHesabi=c,alicakSenetelerHesabi=d,ticariMallarHesabi=e,binalarHesabi=f,tasitlarHesabi=g,demirbaslarHesabi=h
#bankaKredileriKisa=i,saticilarHesabi=j,bankaKredileriUzun=k,borcSenetleri=l,sermayeHesabi=m
class donenVarliklar:
    a=20000
    b=10000
    c=5000
    d=28000
    e=65000
class duranVarliklar:
    f=150000
    g=25000
    h=8000
class kvyk:
    i=42000
    j=60000
class uvyk:
    k=35000
    l=115000
class ozKaynaklar:
    m=59000

class hesap():
    def __init__(self,a,b,c,d,e,f,g,h,i,j,k,l,m):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        self.h=h
        self.i=i
        self.j=j
        self.k=k
        self.l=l
        self.m=m
    def aktif(self):
        aktif=self.a+self.b+self.c+self.d+self.e+self.f+self.g+self.h
        return aktif
    def pasif(self):
        pasif=self.i+self.j+self.k+self.l+self.m
        return pasif
    if (aktif==pasif):
        print("kapanış bilançocu doğru hesaplanmıştır")
    else:
        print("kapanış bilançosu yanlış hesaplanmıştır")

   

        
