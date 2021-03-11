#asalamulaikum 
print("selamat datang di GOparkir")
print("plih option")
print("cek saldo")
print("bayar")
print("top up")
option=int(input("silahkan pilih option:"))
if option==1:
    print("saldo kamu berjumlah Rp.200.000")
elif option==2:
    print("uang kamu Rp.200.000 mau bayar berapa")
    print("1000")
    print("2000")
    uang_kamu=200000
    option2=int(input("option :"))
    if option2==1:
        hasil=uang_kamu-1000
        print("saldomu sekarang berjumlah :",hasil)
    elif option2==2:
        hasil2=uang_kamu-2000
        print("saldomu sekarang berjumlah :",hasil2)
    else:
        print("keyword anda salah")
elif option==3:
     uang_kamu=200000
     print("saldo berjumlah Rp.200.000 mau top up berapa?")
     option3=int(input("masukan jumlah uang"))
     hasil3=uang_kamu+option3
     print("jumlah saldomu sekarang adalah :",hasil3)
else:
     print("keyword anda salah")
    
#menu menu  Go parkir
print("semoga pelayanan kami menyenangkan")
