from audioop import reverse
from random import choices, randrange, random
from typing import List
import math

Genome = List[int]
Populasi = List[Genome]
Rank = List[float]
Cross = List[Genome]
Parent = List[Genome]

def buat_genome(length: int) -> Genome:
    return choices([0,1], k=length)

def buatPopulasi(size: int, panjangGen : int) -> Populasi:
    return [buat_genome(panjangGen) for i in range(size)]

#Masukkin rumus fitness di sini decode genome ke float dulu baru masukkin sama rumus tugas
def fitness(gen: Genome) -> float:
    return
def rankFit(populasi: Populasi) -> Rank:
    return [fitness(populasi[i]) for i in range(len(populasi))]

def sortPopulasi(populasi: Populasi, rankFit : Rank) -> Populasi:
    return [x for _, x in sorted(zip(rankFit,Populasi))]

def selectParent(populasi: Populasi, nilai : Rank) -> Parent:
    return choices(populasi, weights = nilai.reverse(), k=2)

def crossover(a: Genome, b: Genome)-> Cross:
    p = int(len(a)/2)
    return [a[0:p] + b[p], b[0:p] + a[p]]

def mutation(gen: Genome, num : int = 1, prob : float = 0.5)-> Genome:
    for i in range(num):
        idx = randrange(len(gen))
        if random() > prob :
            gen[idx] = gen[idx] 
        else:
            abs(gen[idx]-1)
    return gen


