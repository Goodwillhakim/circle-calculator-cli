from fractions import Fraction

print("=" * 40)
print("      Kalkulator Luas & Keliling Lingkaran")
print("=" * 40)

# Input
r = float(input("Masukkan Jari-jari (cm): "))
pi_input = input("Masukkan nilai π (contoh: 22/7 atau 3.14): ")
pi = float(Fraction(pi_input))

# Perhitungan
luas = pi * r**2
keliling = 2 * pi * r

# Output
print(f"\nLuas Lingkaran     = {luas:.2f} cm²")
print(f"Keliling Lingkaran = {keliling:.2f} cm")
