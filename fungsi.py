from random import choices, randint, randrange, random
from typing import List
import math

Genome = List[int]
Populasi = List[Genome]
Rank = List[float]
Cross = List[Genome]
Parent = List[Genome]
Dekode = List[float]


def buat_genome(length: int) -> Genome:
    return choices([0,1], k=length)


def buatPopulasi(size: int, panjangGen : int) -> Populasi:
    return [buat_genome(panjangGen) for i in range(size)]


#Melakukan decode dari kromosom binary menjadi nilai dengna selang min dan max
def decodeKro(gen:Genome,min: int, max: int)-> Dekode:
    xB = 0
    xA = 0
    p = len(gen)//2
    for i in range(p):
        xB = xB + (2**-(i+1))
    for i in range(p):
        xA = xA + gen[i]*(2**-(i+1))
    x = min + ((max-min)/xB)*xA

    yB = 0
    yA = 0
    p2 = p+1
    i = 1
    while p2 < len(gen):
        yB = yB + (2**-i)
        p2 += 1
        i += 1
    i = 1
    p2 = p+1
    while p2 < len(gen):
        yA = yA + gen[p2]*2**(-i)
        i += 1
        p2 += 1
    y = min + ((max-min)/yB)*yA
    return [x,y]

#Memasukkan hasil decode ke rumus permasalahan
def fitness(gen: Dekode) -> float:
    return ((math.cos(gen[0])+math.sin(gen[1]))**2/((gen[0]**2)+(gen[1]**2)))

#Memilih 2 parent terbaik
def selectParent(populasi: Populasi, nilai : Rank) -> Parent:
    return choices(populasi, weights = nilai.reverse(), k=2)

#Melakukan Crossover dengan probabilitas 60%
def crossover(a: Genome, b: Genome)-> Cross:
    prob = choices([0,1], weights = [0.4,0.6], k = 1)
    if prob[0] == 1:
        p = randint(1, len(a))
        return [a[0:p] + b[p:len(a)], b[0:p] + a[p:len(b)]]
    else:
        return [a,b]

#Melakukan Mutasi dengan probabilitas 0.5%
def mutation(gen: Genome, num : int, prob : float)-> Genome:
    for i in range(num):
        idx = randrange(len(gen))
        gen[idx] = gen[idx] if random() > prob else abs(gen[idx]-1)
    return gen

#Menjalankan evolusi
def evolution(popu: int, kromo: int, min: int, max: int) -> Genome:
    p = Populasi
    p = buatPopulasi(popu, kromo)
    gen = 0
    while True:
        newP = Populasi
        newP = []
        ranking = Rank
        ranking = []
        for j in range(len(p)):
            c = Dekode
            c = decodeKro(p[j], min, max)
            ranking.append(fitness(c))
        p = [x for _, x in sorted(zip(ranking,p))]
        ranking.sort()
        #Tempat melakukan seleksi survivor dengan metode Elitism yang akan memilih 1 kromosom jika populasi ganjil dan 2 jika genap terbaik
        if popu % 2 == 0:
            newP.append(p[0])
            newP.append(p[1])
        else :
            newP.append(p[0])
        while len(newP) != len(p):
            par = selectParent(p, ranking)
            silang = Cross
            silang = crossover(par[0],par[1])
            mutA = Genome
            mutB = Genome
        #Mutasi penggunakan probabilitas 0.5%
            mutA = mutation(silang[0],1,0.5)
            mutB = mutation(silang[1],1,0.5)
            newP.append(mutA)
            newP.append(mutB)
        p = newP
        gen += 1
        #Perhentian generasi dilakukan jadi terdapat 1/2 dari jumlah populasi kromosom dengan nilai sama
        if (p[0] == p[len(p)//2]):
            break

    print("Generasi: ", gen)
    return p[0]
