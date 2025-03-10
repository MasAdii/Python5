def kalkulator():
    while True:
        print("      \n======================")
        print("           KALKULATOR         ")
        print("      ======================\n")
    
        opsi = input("Pilih salah satu opsi(+, -, *, /): ")
    
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    
        if(opsi == "+"):
            hasil = angka1 + angka2
            print(f"Hasil dari {angka1} + {angka2} = {hasil}")
        elif (opsi == "-"):
            hasil = angka1 - angka2
            print(f"Hasil dari {angka1}  {angka2} = {hasil}")
        elif (opsi == "*"):
            hasil = angka1 * angka2
            print(f"Hasil dari {angka1} * {angka2} = {hasil}")
        elif (opsi == "/"):
            hasil = angka1 / angka2
            print(f"Hasil dari {angka1} / {angka2} = {hasil}")
        else:
            print("Input yang anda masukkan tidak valid!!!")
        
        
kalkulator()