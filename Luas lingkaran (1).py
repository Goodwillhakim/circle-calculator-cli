print("=" *41)
print("          Kalkulator Lingkaran")
print("=" *41)

from fractions import Fraction
import math

Jari_Jari=float(input("Masukan Jari Jari "))
pi_input=input("Masukan π ")
pecahan=input("Masukan Pecahan ")
pecahann=float(Fraction(pecahan))
pi=float(Fraction("22/7"))




hasil = pi*Jari_Jari*Jari_Jari/pecahann
print (hasil)   

    