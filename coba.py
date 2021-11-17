def menu():
	import os
	os.system ("CLS")
	print ("Data Warga Kampung Vokasi")
	print ("Daftar Menu:")
	print ("1.Melihat Daftar Data")
	print ("2.Menambah Data Baru")
	print ("3.Mencari Data")
	print ("4.Update Data")
	print ("5.Menghapus Data")
	print ("6.Keluar Dari Program")
	pil = int (input("Masukan no menu yang dipilih:"))
	pilihmenu(pil)
#----------------------------------------------------------
def pilihmenu(p):
	if p==1:
		lihatdata()
	elif p==2:
		tambahdata()
	elif p==3:
		mencaridata()
	elif p==4:
		updatedata()
	elif p==5:
		menghapusdata()
	elif p==6:
		print("\n""Terimakasih !!!")
#----------------------------------------------------------
def lihatdata():
	print("\n""Anda Berada Pada Menu Menampilkan Data:""\n")
	f = open("data/Data Warga.txt")
	isi = f.readlines()
	isi.sort()
	if len(isi)==0:
		print("\n""Data Masih Kosong")
	else:
		i = 1;
		for x in isi:
			pecah = x.split(",")
			print (str(i)+". ",end="")
			print(pecah[0]+" | "+pecah[1]+" | "+pecah[2],end="")
			i +=1
	print("\n""Tekan [Enter] Untuk Melanjutkan")
	f.close()
	input()
	menu()
#----------------------------------------------------------
def tambahdata():
	print ("\n""Anda Berada Pada Menu Menambah Data")
	print ("\n""Masukan Data Baru")
	n = input ("Nama		:")
	a = input ("NIK		:")
	j = input ("No. Rumah	:")
	f = open ("data/Data Warga.txt","a")
	f.writelines([n+","+a+","+j+"\n"])
	print('tekan[enter] untuk melanjutkan')
	f.close()
	input()
	menu()
#----------------------------------------------------------
def  mencaridata():
	f = open("data/Data Warga.txt","r")
	nama = input("\nCari Warga Dengan Nama :")
	found=[]
	isi = f.readlines()
	if len(isi)==0:
		print("\nData Masih Kosong")
	else:
		for x in isi:
			pecah = x.split(",")
			if nama==pecah[0]:
				found=pecah
	if found:
		print("\nData Warga Ditemukan!")
		print("Nama\t\t:",found[0]+" "+ "\nNIK\t\t:",found[1]+" "+"\nNo. Rumah\t:",found[2],end="\n")
	else:
		print("\nData Tidak Ditemukan!\n")
	f.close()
	print("Tekan [Enter] Untuk Kembali Ke Menu")
	input()
	menu()

#---------------------------------------------------------- 
def updatedata():
	print("\n""Anda Berada Pada Menu Menambah Data")
	nx = input("\n""Masukan Nama Data Yang Ingin Diupdate :")
	print("\n""Masukan Data Baru!")
	nb = input("\n""Masukan Nama Baru 			:")
	ab = input("\n""Masukan NIK Baru 			:")
	jb = input("\n""Masukan No. Rumah Baru 			:")
	f = open ("data/Data Warga.txt")
	isi = f.readlines()
	print(isi)
	idx = 0
	for x in isi:
		xp = x.split(",")
		if xp[0]==nx:
			xp[0] = nb
			xp[1] = ab
			xp[2] = jb+"\n"
			xg = ",".join(xp)
			print(xp)
			print(xg)
			isi[idx]=xg
		idx +=1
	print(isi)
	f.close()
	
	f = open ("data/Data Warga.txt","w")
	isi = f.writelines(isi)
	print('Tekan [Enter] Untuk Melanjutkan')
	f.close()
	input()
	menu()
	
#----------------------------------------------------------
def menghapusdata():
	print("\nData Warga Yang Ingin Dihapus\n")
	f = open("data/Data Warga.txt","r")
	isi = f.readlines()
	isi.sort()
	if len(isi)==0:
		print("Data Masih Kosong")
	else:
		i = 1;
		for x in isi:
			pecah = x.split(",")
			print(str(i)+".",end="")
			print("Nama\t	:",pecah[0]+" "+"\nNIK\t\t:",pecah[1]+" "+"\nNo. Rumah\t	:",pecah[2], end="\n")
			i +=1
	pil = int(input("\n""Masukan No Warga Yang Ingin Anda Hapus :"))
	y = (pil)-1
	del isi[y]
	
	f = open("data/Data Warga.txt","w")
	f.writelines(isi)
	print("\n""Data Sudah Terhapus!\n")
	f.close()
	print("tekan [enter] untuk kembali")
	input()
	menu()
 
