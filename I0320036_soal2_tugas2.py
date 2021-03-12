#Biodata diri
nama = "Erysa Putri Vara Afifa."
nama_panggilan = "Erysa"
prodi = "Teknik Industri"
universitas = "Universitas Sebelas Maret"

print("Hai, semua! Perkenalkan nama saya",nama,"Saya akrab disapa",nama_panggilan,"sejak saya kecil.")
print("Kini, saya menempuh pendidikan di Program Studi",prodi,universitas+".")

#menghitung umur
tanggal_lahir = 10
bulan_lahir = 6
bulan_nama = "Juni"
tahun_lahir = 2002
tanggal_kini = 11
bulan_kini = 3
tahun_kini = 2021

#jumlah umur secara rinci
umur_hari = ((tahun_kini-tahun_lahir)*365 + (bulan_kini-bulan_lahir)*30 + (tanggal_kini-tanggal_lahir))
tahun = int((umur_hari)/365)
bulan = int(((umur_hari)%365)/30)

print("Saya lahir pada tanggal",str(tanggal_lahir)+" "+bulan_nama+" "+str(tahun_lahir)+".")
print("Sekarang, umur saya",tahun,"tahun",bulan,"bulan.")

#alamat rumah
jalan = "Jalan Genuk Baru IV"
nomor = 88
RT = "IV"
RW = "VI"
kelurahan = "Tegalsari"
kecamatan = "Candisari"
kota = "Kota Semarang"

print("Saya bertempat tinggal di",jalan,"Nomor",nomor,"RT",RT,"RW",RW+", "+kelurahan+", "+kecamatan+", "+kota+".")

#tinggi badan
tinggi = float(150*2*0.75-(141.52/2))
sepatu = int(170*1.75/7.5)

print("Tinggi badan saya",tinggi,"cm dan ukuran sepatu saya",str(sepatu)+".")

#hobi
hobi = "menonton film"
genre_1 = "science fiction"
genre_2 = "action"

print("Hobi saya adalah",hobi,"dengan genre favorit saya yaitu",genre_1,"dan",genre_2+".")