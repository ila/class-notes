#!/usr/bin/python3

import random as ran

questions = [
    "Pattern matching con shift-and (bit-parallel)",
    "Pattern matching con Karp-Rabin",
    "Pattern matching con suffix tree",
    "Costruzione di un suffix tree a partire da una stringa T",
    "Costruzione di un suffix array da un suffix tree",
    "Costruzione di un suffix tree da un suffix array",
    "Pattern matching con suffix array",
    "Acceleranti per il pattern matching con suffix array",
    "Sottostringa comune di k stringhe con tree/array",
    "RMQ (Range Minimum Query)",
    "Needleman-Wunsch",
    "Smith-Waterman",
    "Allineamento con gap generico"
    "Allineamento con banda"
    "PAM e BLOSUM",
    "Karlin-Altschul e BLAST",
    "Allineamento multiplo",
    "Algoritmo per la shortest superstring",
    "Grafi di overlap",
    "OLC (Overlap, Layout, Consensus)",
    "SBH (Sequencing By Hydration)",
    "Filogenesi su caratteri",
    "Grande e piccola parsimonia",
    "Algoritmo di Sankoff",
    "Algoritmo di Fitch",
    "Filogenesi su distanze",
    "Orologio molecolare",
    "Ultrametrica",
    "UPGMA"
]

maxtoselect = 4

selected = ran.sample(population = questions, k = maxtoselect)

print("Rispondere a 3 delle seguenti 4 domande.")
print("Le domande sono in ordine di difficoltà [e punteggio] decrescente -- non con questo programma")
print("Tempo per l'esame: 1h (20 minuti a domanda)")
print()
[print(str(i) + ") " + item) for i, item in enumerate(selected, start = 1)]