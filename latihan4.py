# menghitung waktu tempuh

jamBerangkat = 6
sAB = 125
vAB = 62
istirahat = 45
sBC = 256
vBC = 70
tAB = round(sAB / vAB)
tBC = round(sBC/ vBC)
waktuPerjalanan = tAB + tBC
waktuTiba = jamBerangkat + waktuPerjalanan 
print("Pak Amir berangkat pukul 06:00 dari kota A ke kota B dan beristirahat selama 45 menit di kota B, Kemudian ia melanjutkan perjalanan dari kota B menuju kota C")
print("Jadi Pak Amir sampai di kota C pukul",waktuTiba,'.',istirahat)
