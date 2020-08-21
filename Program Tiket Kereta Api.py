print ("Program Tiket Kereta Api")
print ("------------------------")

jarak = int (input("Masukkan jarak =  "))
harga_tiket = int (input("Masukkan Harga Tiket =  "))

if (jarak>500) or (harga_tiket>500000):
    beli = harga_tiket*0.5
elif (jarak>200) or (harga_tiket>350000):
    beli = harga_tiket*0.7
else :
    beli = harga_tiket
    
print ()
print ("Hara_Tiket = Rp", beli)

