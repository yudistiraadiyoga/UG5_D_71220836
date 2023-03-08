def ganti_kata(a,b,c):
    d = len(a)
    for i in range(d):
        if a[i]==b:
            a[i]=c
    else:
        print('kata yang Anda cari tidak ada!')
    a_baru = ' '.join(a)
    print('='*10, ' Hasil ', '='*10)
    print(f'Kalimat baru\t\t: {a_baru}')

a = str(input('Masukkan Kalimat\t: ')).split()
b = str(input('Kata yang dicari\t: '))
c = str(input('Diganti menjadi\t\t: '))
ganti_kata(a,b,c)