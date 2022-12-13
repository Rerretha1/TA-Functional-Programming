import re, random
nama = []
pin = []
def login():
    print ("Masukkan nama beserta pin : ")
    print("=============================\n")
    while True :
        isi_nama = input ("Nama (contoh: Anang)= ")
        isi_pin = input ("Pin (contoh: 123)= ")
        tanya = input('Apakah data sudah benar ? [y]/[n]: ')
        while tanya !='y' or tanya =='y' :
            nama.append(isi_nama)
            pin.append(isi_pin)
            break
    menu()

def menu():
    simpanan = list()
    sisa_saldo = 0
    global nama

    def jumlah(wadah):
        hasil = 0
        for i in wadah :
            hasil +=1
        return hasil
    def kurang (wadah):
        hasil = 0
        for i in wadah:
            hasil-= 1
        return hasil
    def Nama(text):
        return text.upper()

    print("PILIH MENU")
    print("===========")
    while True:
        print(  "Deposit        [1]\n"+
                "Withdraw       [2]\n"+
                "Cek Saldo      [3]\n"+
                "Verifikasi Akun[4]\n"+
                "Hapus Akun     [5]\n"+
                "Pin Baru       [6]\n"+
                "Log Out        [7]")
        masuk = int(input("Masukkan kode = "))
        if masuk == 1:
            while True:
                deposit = int(input("Deposit = Rp."))
                simpanan.append(deposit)
                tanya = input ("Apakah ingin deposit lagi ? [y]/[n] :")
                while tanya != 'y'and tanya != 'n':
                    tanya = input("Apakah ingin deposit lagi ? [y]/[n] :")
                if tanya == 'n' or tanya =="N":
                    print ("Jumlah saldo anda", jumlah(simpanan))
                    break
                    menu()
        elif masuk == 2:
            if simpanan == []:
                print("saldo masih kosong lakukan Deposit")
            else:
                withdraw = int(input("Withdraw = Rp."))
                sisa_saldo = jumlah(simpanan)-withdraw
        elif masuk == 3:
            if sisa_saldo ==0:
                print("Jumlah saldo anda", jumlah(simpanan))
            else:
                print("Jumlah saldo anda", sisa_saldo)
        elif masuk == 4:
            listToStr = ' '.join([str(elem) for elem in nama])
            nasabah = NAMA 
            print("AKun sudah terverivikasi :", nasabah(listToStr))
            for regex in re.finditer('[a-z]', lisToStr):
                print(regex)
        elif masuk == 5:
            print("Akun yang terdaftar :", nama)
            hapus = lambda array, item: [x for x in array if x != item]
            orang = input ("Masukkan nama :")
            print("AKun yang terdaftar :", hapus(nama, orang))
        elif masuk == 6:
            a = random.getrandbits(20)
            print(a)
        elif masuk == 7:
            login()
        else :
            menu()
login()


        



    

