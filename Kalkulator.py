#KALKULATOR
def add(x,y): #Fungsi Penjumlahan
    return x + y
def subtract(x,y): #Fungsi Pengurangan
    return x - y
def multiply(x,y): #Fungsi Perkalian
    return x * y
def divide(x,y): #Fungsi Pembagian
    return x / y

#MENU UPERASI
print ("Pilih Operasi")
print ("1. Jumlah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")
choice = input ("Masukkan pilihan (1/2/3/4): ") #Meminta Input Pada User
num1 = int (input("Masukkan bilangan pertama: "))
num2 = int (input("Masukkan bilangan kedua: "))
if choice=='1':
    print (num1, "+", num2, "=", add (num1, num2))
elif choice=='2':
    print (num1, "-", num2, "=", subtract (num1, num2))
elif choice=='3':
    print (num1, "*", num2, "=", multiply (num1, num2))
elif choice=='4':
    print (num1, "/", num2, "=", divide (num1, num2))
else:
    print ("Input Salah !!")

#OPERATOR MATEMATIKA
a = int (input("Masukkakn nilai a:  "))
b = int (input("Masukkakn nilai b:  "))
#Mengguakan Operator Penjumlahan
c=a+b
print (a, "+", b, "=", c)
#Mengguakan Operator Pengurangan
c=a-b
print (a, "-", b, "=", c)
#Mengguakan Operator Perkalian
c=a*b
print (a, "*", b, "=", c)
#Mengguakan Operator Pembagian
c=a/b
print (a, "/", b, "=", c)
#Mengguakan Operator Modulo (Sisa Bagi)
c=a%b
print (a, "%", b, "=", c)
#Mengguakan Operator Pangkat
c=a**b
print (a, "**", b, "=", c)






















