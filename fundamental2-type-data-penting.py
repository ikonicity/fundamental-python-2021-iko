print('tipe data skalar =>tipe data sederhana')
anak1 = 'iko'
anak2 = 'iko2'
anak3 = 'iko3'
anak4 = 'iko4'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['iko1', 'iko2', 'iko3', 'iko4']
print(anak)
anak.append('iko5')
print(anak)

print( '\nsapa anak ke 2')
print(f'hai {anak[1]}!')

print( '\nsapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nSapa semua anak : cara ribet')
for a in range(0, len(anak)):
    print(f'{a}.hai {anak[a]}')