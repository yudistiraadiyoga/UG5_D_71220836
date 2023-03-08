import math
ja = float(input('Masukkan jarak awal (dalam meter) : '))
for i in range(1):
    while ja==str('done'or'stop'):
        ja = float(input('Masukkan jarak awal (dalam meter) : '))
        se5 = float(input('Masukkan sudut elevasi pada menit ke-5 (dalam derajat) : '))
        se6 = float(input('Masukkan sudut elevasi pada menit ke-6 (dalam derajat) : '))
        tha = ja*math.tan(se5)
        jha = ja*math.tan(se6)-math.tan(se5)
        skh = jha*math.tan(se6)
        print(f'Ketinggian drone pada menit ke-5 adalah {tha}')
        print(f'Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah {skh}')
    else:
        print('Program dihentikan.')
if ja=='berhenti'or'done':
    print('Program dihentikan.')