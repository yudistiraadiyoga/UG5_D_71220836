def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    asal = str(input('Masukkan asal mobil (ketik "done" untuk keluar) : ')).lower()
    while asal != 'done':
        asal = str(input('Masukkan asal mobil (ketik "done" untuk keluar) : ')).lower()
        if asal=='solo':
            jumlahSol += 1
        elif asal=='surabaya':
            jumlahSur += 1
        elif asal=='jogja':
            jumlahJog += 1
        elif asal=='magelang':
            jumlahMag += 1
    else:
        NameError
    print('='*10, ' Hasil ', '='*10)
    print(f'Jumlah Mobil Solo\t: {jumlahSol}\nJumlah Mobil Surabaya\t: {jumlahSur}\nJumlah Mobil Jogja\t: {jumlahJog}\nJumlah Mobil Magelang\t: {jumlahMag}')
    return

hitung_mobil()