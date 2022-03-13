while True :
    print ("KALKULATOR SEDERHANA".center(50,' '))
    print ("="*50)
    print ('1. perkalian')
    print ('2. pembagian')
    print ('3. penjumlahan')
    print ('4. pengurangan')
    print ('0. exit')
    operasi = int(input("masukan nomor pilihan operasi : "))
    while operasi >4 or operasi<0 :
        print ('silahkan masukan angka yang ada pada menu.')
        operasi = int(input("masukan nomor pilihan operasi : "))
        print ('')
    if operasi == 0 :
        break
    else :
        a = int(input("masukan nilai a : "))
        b = int(input("masukan nilai b : "))
        if operasi == 1:
            print ("Perkalian".center(50,'='))
            perkalian = a*b
            print (a,"*",b," = ",perkalian)
            print ("="*50)
        elif operasi == 2:
            print ("Pembagian".center(50,'='))
            pembagian = a/b
            print (a,"/",b," = ",pembagian)
            print ("="*50)
        elif operasi == 3:
            print ("Penjumlahan".center(50,'='))
            penjumlahan = a+b
            print (a,"+",b," = ",penjumlahan)
            print ("="*50)
        elif operasi == 4:
            print ("Pengurangan".center(50,'='))
            pengurangan = a-b
            print (a,"-",b," = ",pengurangan)
            print ("="*50)
     
