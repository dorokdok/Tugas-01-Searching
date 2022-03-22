import fungsi as f

genakhir = f.Genome
genDekode = f.Dekode

populasi = int(input("Masukkan banyak populasi dalam satu generasi: "))
kromosom = int(input("Masukkan panjang kromosom/gen yang ingin digunakan: "))

genakhir = f.evolution(populasi,kromosom,-5,5)
genDekode = f.decodeKro(genakhir, -5,5)
print("Kromsom Terbaik", genakhir)
print("X= ", genDekode[0], "Y= ", genDekode[1])
print("Nilai akhir= ",f.fitness(genDekode))