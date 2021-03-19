#Menuliskan data pada Dictioonary
data_dict = {'Nama':'Amar', 'Hobi 1':'Basket', 'Hobi 2':'Membaca novel', 'Hobi 3':'Bermain game',
           'Instagram': '@dhiaul_amar', 'Facebook': 'Dhiaul Amar Naufal', 'Twitter': '@dhiaulamar',
           'lagu favorit 1': '5 Sos: Youngblood', 'Lagu favorit 2': 'Coldplay : Viva la vida',
           'Lagu favorit 3': 'Weird Genius : Sweet Scar', 'Makanan favorit 1': 'Nasi goreng',
           'Makanan favorit 2': 'Indomie soto', 'Makanan favorit 3': 'Bakso'}

#Mengubah hobi dan social media pada Dictionary
data_dict['Hobi 3'] = 'Futsal'
data_dict['Twitter'] = '@amar_naufal'
print(data_dict)

#Menghapus 2 jenis makanan favorit pada Dictionary
del data_dict['Makanan favorit 2']
del data_dict['Makanan favorit 3']
print(data_dict)

#Menambahkan hobi pada Dictionary
data_dict['Hobi 4'] = 'Nongkrong'
print(data_dict)