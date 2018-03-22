calisan=50
yevmiye=90
aylikmesai=0
haftalikmaas=630
aylikmaas=0
while aylikmaas<=22:
    haftalikmesai=int(input("Haftalık mesai:"))
    aylıkmesai=haftalikmesai*4
    haftalikmaas=haftalikmaas+(haftalikmesai*yevmiye*0.10)
    aylikmaas=aylikmaas+haftalikmaas*4
    print("Aylık maaş:",aylikmaas)
else:
    print("Aylık mesai 22 saatten fazla olamaz.")
