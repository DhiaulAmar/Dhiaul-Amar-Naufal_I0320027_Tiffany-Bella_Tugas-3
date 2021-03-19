#Menuliskan list nama teman
nama_teman = ['Adhi', 'Safri', 'Afiq', 'Denny', 'Vizal', 'Audrey', 'Fajri', 'Bagus', 'Cita', 'Dhea']
print(nama_teman[4], nama_teman[6], nama_teman[7])

#Mengganti list nama teman
nama_teman[3] = 'Fadhila'
nama_teman[5] = 'Attar'
nama_teman[9] = 'Erika'
print(nama_teman)

#menambah list nama teman
nama_teman.append('Elisa')
nama_teman.append('Efa')
print(nama_teman)

#menampilkan list nama teman dengan perulangan
for teman in nama_teman:
    print(teman)

#menampilkan panjang list nama teman
print(len(nama_teman))