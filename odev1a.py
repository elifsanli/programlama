#gelirler=x,giderler=y,toplamCiro=z,toplamCalisanSayisi=t
class hesapla():
    def __init__(self,x,y,z,t):
        self.x=x
        self.y=y
        self.z=z
        self.t=t
    def isletmeKari(self):
        isletmeKari=self.x-self.y
        return isletmeKari
    def adambasiCiro(self):
        adambasiCiro=self.z/self.t
        return adambasiCiro
    
