#menghitung tarif rental mobil

tarifUtama= 200000
tarifTambahan = 10000
jamMulai = 6
jamSelesai = 23
menitMulai = 00
menitSelesai = 50
jamSewa = jamSelesai - jamMulai
menitSewa = menitSelesai - menitMulai
print("Mobil disewa pukul 06:00")
print("Mobil dikembalikan pukul 23:50")
print("Tarif utama Rp 200000 per 12 jam")
print("Tarif tambahan Rp 10000 per jam")
lamaSewa = jamSewa + menitSewa / 60
totalSewa = int(lamaSewa)
totalBiaya = tarifUtama + tarifTambahan * 5
print("Total tarif yang harus dia bayarkan adalah Rp" , totalBiaya)
