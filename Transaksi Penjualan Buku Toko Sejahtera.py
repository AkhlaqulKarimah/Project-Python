# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:27:56 2020

@author: User
"""

print ("-------------------------------")
print (" Transaksi Penjualan Buku ")
print ("      Toko Sejahtera      ")
print ("-------------------------------")
kb = int (input("Kode Buku     :"))
jb = str (input("Judul Buku    :"))
p = str (input("Penerbit       :"))
t = int (input("Tahun Terbit   :"))
h = int (input("Harga Buku     :"))
jml = int (input("Jumlah Buku  :"))
Jenis_Buku = str (input("Jenis Buku (F/N/T)   :"))
total = int (h*jml)
print ("-------------------------------")
print ("Jenis Buku   :", Jenis_Buku)
if (Jenis_Buku == ")"):
    print ("Fisika")
elif (Jenis_Buku == "N"):
    print ("Non Fisika")
elif (Jenis_Buku == "T"):
    print ("Text")
print ("Total Harga Buku  :", "Rp.", total)
print ("-------------------------------")
