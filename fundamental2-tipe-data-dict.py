"""
tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wive', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_ind_eng)
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['anak'])

print('\ndata ini dikirim dari server gojek, untuk memberikan info driver disekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-06-25',
    'driver_list': [
        {'nama': 'iko','jarak': 10},
        {'nama': 'iko2','jarak': 100},
        {'nama': 'iko3','jarak': 1000},
        {'nama': 'iko4','jarak': 10000}
    ]
}
print(data_dari_server_gojek)
print(f"\ndriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #2 {data_dari_server_gojek['driver_list'][1]}")
print(f"driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][1]['jarak']} meter")