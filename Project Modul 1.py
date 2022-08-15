# Database Buku
dataBuku = [{
        'ID Buku'   : 'B001',
        'Judul'     : 'Laut Bercerita',
        'Pengarang' : 'Laila Chudori',
        'Penerbit'  : 'Gramedia',
        'Tahun'     : 2017,
        'Genre'     : 'Fiksi'
    },
    {
        'ID Buku'   : 'B002',
        'Judul'     : 'Filosofi Teras',
        'Pengarang' : 'Henry M.',
        'Penerbit'  : 'Buku Kompas',
        'Tahun'     : 2018,
        'Genre'     : 'Non Fiksi'
    },
    {
        'ID Buku'   : 'B003',
        'Judul'     : 'Tentang Kamu',
        'Pengarang' : 'Tere Liye',
        'Penerbit'  : 'Putra Bangsa',
        'Tahun'     : 2016,
        'Genre'     : 'Fiksi'
    },
    {
        'ID Buku'   : 'B004',
        'Judul'     : 'Atomic Habits',
        'Pengarang' : 'James Clear',
        'Penerbit'  : 'Avery Corp.',
        'Tahun'     : 2018,
        'Genre'     : 'Non Fiksi'
    }
]

# Show Tabel Data Buku
def tabelBuku (listBuku):
    print('\n-----------------------------------DAFTAR BUKU-----------------------------------')
    print('ID Buku\t|Judul\t\t\t|Pengarang\t|Penerbit\t|Tahun\t|Genre')
    for i in range(len(listBuku)):
        print(f"{listBuku[i]['ID Buku']}\t|{listBuku[i]['Judul']}\t\t|{listBuku[i]['Pengarang']}\t|{listBuku[i]['Penerbit']}\t|{listBuku[i]['Tahun']}\t|{listBuku[i]['Genre']}")

# Search Tools
def search(dataDicari):
    search = list(filter(lambda data : data['ID Buku'] == dataDicari, dataBuku))
    return search

# Input Menu Hanya Angka
def warningHanyaAngka():
    print('''
-------------------WARNING-------------------
Masukkan pilihan menu dengan angka yang benar
---------------------------------------------
''')

# Input ID Buku Baru
def inputIDnew(digit):
    while True:
        idNew= input('Masukkan angka 3 digit untuk ID buku baru: ')
        n = idNew.isnumeric()
        if n == True and len(idNew) == digit:
            n = 'B'+idNew
            break
        elif n == True and len(idNew) != digit:
            print('---- Masukkan angka 3 digit saja! ----')
            continue
        else:
            print('---- Masukkan data dalam bentuk angka! ----')
    return n

# Input Tahun Terbit Hanya dengan Angka
def inputtahunNew():
    while True:
        tahunNew = input('Masukkan tahun terbit buku: ')
        n = tahunNew.isnumeric()
        if n == True:
            n = int(tahunNew)
            break 
        else:
            print('''
---- Masukkan tahun terbit dengan angka! ----
            ''')
    return n

# Update Tahun Terbit Hanya dengan Angka
def inputtahunUpdate(ID):
    while True:
        tahunUpdate = input('Masukkan data baru: ')
        n = tahunUpdate.isnumeric()
        if n == True:
            n = int(tahunUpdate)
            break 
        else:
            print('''
---- Masukkan tahun terbit dengan angka! ----
            ''')
    showUpdate(search(ID),5,tahunUpdate)
    updateConfirm(search(ID),'Tahun',tahunUpdate)
    return n

# Show Update Barang Sesuai Kolom
def showUpdate(listBuku, category, newList):
    print('\n-----------------------------------Daftar Buku-----------------------------------')
    print('ID Buku\t|Judul\t\t\t|Pengarang\t|Penerbit\t|Tahun\t|Genre')
    if category == 1:
        for i in range(len(listBuku)):
            print(f"{newList}\t|{listBuku[i]['Judul']}\t\t|{listBuku[i]['Pengarang']}\t|{listBuku[i]['Penerbit']}\t|{listBuku[i]['Tahun']}\t|{listBuku[i]['Genre']}")
    elif category == 2:
        for i in range(len(listBuku)):
            print(f"{listBuku[i]['ID Buku']}\t|{newList}\t\t|{listBuku[i]['Pengarang']}\t|{listBuku[i]['Penerbit']}\t|{listBuku[i]['Tahun']}\t|{listBuku[i]['Genre']}")
    elif category == 3:
        for i in range(len(listBuku)):
            print(f"{listBuku[i]['ID Buku']}\t|{listBuku[i]['Judul']}\t\t|{newList}\t|{listBuku[i]['Penerbit']}\t|{listBuku[i]['Tahun']}\t|{listBuku[i]['Genre']}")
    elif category == 4:
        for i in range(len(listBuku)):            
            print(f"{listBuku[i]['ID Buku']}\t|{listBuku[i]['Judul']}\t\t|{listBuku[i]['Pengarang']}\t|{newList}\t|{listBuku[i]['Tahun']}\t|{listBuku[i]['Genre']}")
    elif category == 5:
        for i in range(len(listBuku)):
            print(f"{listBuku[i]['ID Buku']}\t|{listBuku[i]['Judul']}\t\t|{listBuku[i]['Pengarang']}\t|{listBuku[i]['Penerbit']}\t|{newList}\t|{listBuku[i]['Genre']}")
    else:
        for i in range(len(listBuku)):
            print(f"{listBuku[i]['ID Buku']}\t|{listBuku[i]['Judul']}\t\t|{listBuku[i]['Pengarang']}\t|{listBuku[i]['Penerbit']}\t|{listBuku[i]['Tahun']}\t|{newList}")

# Update Confirmation:
def updateConfirm(data, column, newData):
    confirm = input('Apakah Anda yakin untuk mengupdate data tersebut? (Y/N): ').capitalize()
    if confirm == 'Y':
        data[0][column] = newData
        tabelBuku(dataBuku)
        print('*** Data buku telah diperbaharui! ***')
    elif confirm == 'N':
        print('*** Data buku batal diperbaharui! ***')
    else:
        print('*** Masukkan pilihan jawaban yang benar! ***')

# Membaca Data Buku
def subMenu1():
    sub1 = input('''
=============================================
                DATABASE BUKU  
=============================================
Menu:
1. Tampilkan seluruh data
2. Cari data berdasarkan ID buku
3. Kembali ke menu utama
            
Pilih Menu (1-3): ''')
    if sub1 == '1' and dataBuku == []:                                   
        print('*** Data Buku Tidak Ada ***')                             
    elif sub1 == '1' and len(dataBuku):
        tabelBuku(dataBuku)
    elif sub1 == '2' and dataBuku == []:
        print('*** Data Buku Tidak Ada ***')
    elif sub1 == '2' and len(dataBuku):
        inputID = input('ID buku yang dicari: ').capitalize()
        search(inputID)
        if len(search(inputID)):
            tabelBuku(search(inputID))
        else:
            print(f'*** Tidak ada ID buku [{inputID}] dalam data! ***')
    elif sub1 == '3':
        menuUtama()
    else:
        warningHanyaAngka()
    subMenu1()

# Tambah Data Buku
def subMenu2():
    sub2 = input('''
=============================================
              TAMBAH DATA BUKU  
=============================================
Menu:
1. Tambahkan data buku baru
2. Kembali ke menu utama
                        
Pilih Menu (1-2): ''')
    if sub2 == '1':
        idNew= inputIDnew(3)                                                # Line 57
        search(idNew)
        if len(search(idNew)):
            print(f'*** ID buku [{idNew}] sudah ada dalam data! ***')
        else:
            judulNew = input('Masukkan judul buku: ').capitalize()
            pengarangNew = input('Masukkan nama pengarang: ').capitalize()
            penerbitNew = input('Masukkan nama penerbit: ').capitalize()
            tahunNew = inputtahunNew()                                      # Line 72
            genreNew = input('Masukkan genre buku: ').capitalize()
            dataBukuBaru= [{
                'ID Buku'   : idNew,
                'Judul'     : judulNew,
                'Pengarang' : pengarangNew,
                'Penerbit'  : penerbitNew,
                'Tahun'     : tahunNew,
                'Genre'     : genreNew
            }]
            tabelBuku(dataBukuBaru)
            checker = input('Simpan data buku? (Y/N): ').capitalize()
            if checker == 'Y':
                dataBuku.extend(dataBukuBaru)
                tabelBuku(dataBuku)
                print('*** Data berhasil disimpan! ***')
            elif checker == 'N':
                print('*** Data batal disimpan! ***')
            else:
                print('*** Masukkan pilihan jawaban yang benar! ***')
    elif sub2 == '2':
        menuUtama()
    else:
        warningHanyaAngka()
    subMenu2()                     

# Update Data Buku
def subMenu3():
    sub3 = input('''
=============================================
              UPDATE DATA BUKU  
=============================================
Menu:
1. Perbaharui data buku
2. Kembali ke menu utama
            
Pilih Menu (1-2): ''')
    if sub3 == '1':
        tabelBuku(dataBuku)
        inputID = input('Masukkan ID buku untuk data yang ingin diperbaharui: ').capitalize()
        search(inputID)                             
        if len(search(inputID)) > 0:
            tabelBuku(search(inputID))
            checker = input('Lanjutkan update data? (Y/N): ').capitalize()
            if checker == 'Y':
                edit= int(input('''
Kolom data yang akan diupdate:
1. ID Buku
2. Judul
3. Pengarang
4. Penerbit
5. Tahun
6. Genre
                 
Pilih nomor kategori (1-6): '''))
                if edit == 1:
                    addData = input('Masukkan data baru: ').capitalize()
                    showUpdate(search(inputID),1,addData)                   # Line 102
                    updateConfirm(search(inputID),'No. Buku',addData)       # Line 125
                elif edit == 2:
                    addData = input('Masukkan data baru: ').capitalize()
                    showUpdate(search(inputID),2,addData)
                    updateConfirm(search(inputID),'Judul',addData)
                elif edit == 3:                                             
                    addData = input('Masukkan data baru: ').capitalize()
                    showUpdate(search(inputID),3,addData)
                    updateConfirm(search(inputID),'Pengarang',addData)
                elif edit == 4:
                    addData = input('Masukkan data baru: ').capitalize()
                    showUpdate(search(inputID),4,addData)
                    updateConfirm(search(inputID),'Penerbit',addData)
                elif edit == 5:                                                 
                    inputtahunUpdate(inputID)                               # Line 86
                elif edit == 6:
                    addData = input('Masukkan data baru: ').capitalize()
                    showUpdate(search(inputID),6,addData)
                    updateConfirm(search(inputID),'Genre',addData)
                else:
                    print('*** Pilih kategori yang tepat! ***')
            elif checker == 'N':
                print('*** Update data dibatalkan! ***')
            else:
                print('*** Masukkan pilihan jawaban yang benar! ***')
        else:
            print(f'*** Data buku [{inputID}] tidak ada ***')  
    elif sub3 == '2':
        menuUtama()
    else:
        warningHanyaAngka()
    subMenu3()       

# Hapus Data Buku
def subMenu4():
    sub4 = input('''
=============================================
              HAPUS DATA BUKU  
=============================================
Menu:
1. Menghapus data buku
2. Kembali ke menu utama
            
Pilih Menu (1-2): ''')
    if sub4 == '1':
        tabelBuku(dataBuku)
        inputHapusID = input('Masukkan ID buku untuk data yang akan dihapus: ').capitalize()
        search(inputHapusID)                
        if len(search(inputHapusID)) > 0:
            tabelBuku(search(inputHapusID))
            checker = input('Lanjutkan hapus data? (Y/N): ').capitalize()
            if checker == 'Y':
                for i in search(inputHapusID):
                    dataBuku.remove(i)
                print('*** Data buku berhasil dihapus! ***')
            elif checker == 'N':
                print('*** Data buku batal dihapus! ***')
            else:
                print('*** Masukkan pilihan jawaban yang benar! ***')
        else:
            print(f'*** Data Buku {inputHapusID} Tidak Ada ***')
    elif sub4 == '2':
        menuUtama()
    else:
        warningHanyaAngka()
    subMenu4()   

# Menu Database Buku
def menuUtama():
    while True:
        pilihMenu = input('''
=============================================
      DATA BUKU PERPUSTAKAAN PURWADHIKA 
=============================================

Menu Utama:
1. Lihat Database Buku
2. Tambah Data Buku
3. Update Data Buku
4. Hapus Data Buku
5. Exit Program

Pilih angka menu yang ingin dijalankan (1-5): ''')

        if(pilihMenu == '1'):
            subMenu1()
        elif(pilihMenu == '2'):
            subMenu2()
        elif(pilihMenu == '3'):
            subMenu3()
        elif(pilihMenu == '4'):
            subMenu4()
        elif(pilihMenu == '5'):
            quit()
        else:
            warningHanyaAngka()                

menuUtama() 