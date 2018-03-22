stokmiktari=10000
alinanurun=100
satilanurun=500
i=1
while True:
    stokmiktari=stokmiktari-satilanurun+alinanurun
    i=i+1
    if(stokmiktari<=0):
        print(i,"ay sonra sıfırlanır.")
        break
