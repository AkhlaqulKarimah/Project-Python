print (     "KASIR"       )
print ("-----------------")
def menu():
    print ("Menu Pilihan:  ")
    print ("1. Makanan:    ")
    print ("2. Minuman:    ")
    print ("3. Keluar:     ")
def makanan ():
    print ("Makanan")
    print ("1. Ikan Bakar")
    a = int (input("Jumlah Pesanan yang diinginkan:  "))
    ikan= a*12000
    print ("Jumlah:   ", ikan)
    print ("2. Ayam Bakar")
    b = int (input("Jumlah Pesanan yang diinginkan:  "))
    ayam= b*15000
    print ("Jumlah:   ", ayam)
    print ("3. Sate")
    c = int (input("Jumlah Pesanan yang diinginkan:  "))
    sate= c*10000
    print ("Jumlah:   ", sate)
    print ("4. gule")
    d = int (input("Jumlah Pesanan yang diinginkan:  "))
    gule= d*10000
    print ("Jumlah:   ", gule)
    print ("Bayar")
    Bayar = ikan+ayam+sate+gule
    print ("Jumlah:  ", Bayar)
    ulang = str (input("mau pesan kembali [Y/N] ?"))
    if ulang =="Y" or "N":
        menu()
    else:
          exit() 
                
def minuman ():
    print ("Minuman")
    print ("1. es teh")
    e = int (input("Jumlah Pesanan yang diinginkan:  "))
    teh= e*3500
    print ("Jumlah:   ", teh)
    print ("2. jus alpukat")
    f = int (input("Jumlah Pesanan yang diinginkan:  "))
    alpukat= f*10000
    print ("Jumlah:   ", alpukat)
    print ("3. es jeruk")
    g = int (input("Jumlah Pesanan yang diinginkan:  "))
    jeruk= g*4000
    print ("Jumlah:   ", jeruk)
    print ("Bayar")
    Bayar = teh+alpukat+jeruk
    print ("Jumlah:  ", Bayar)
    ulang = str (input("mau pesan kembali [Y/N] ?"))
    if ulang =="Y" or "N":
        menu()
    else:
          exit() 
          
#Program Kalkulasi perhitungan untung, rugi penjualan di Cafe Sejahtera
print ("Program perhitungan pesanan makanan dan minuman pada kasir")
print ("-----------------------KARIM BERKAH----------------------")
print
menu()
while 1:
    pilih = int (input("Menu Pilihan:  "))
    if pilih == 1 :
        makanan ()
    elif pilih == 2 :
        minuman ()
    elif pilih == 3 :
        print ("n")
        break;
        
            














