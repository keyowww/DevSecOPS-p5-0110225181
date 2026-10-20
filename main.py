from calculator import tambah, kurang

def main():
    print("=== Aplikasi Kalkulator Sederhana ===")
    a = 10
    b = 5
    print(f"Hasil {a} + {b} = {tambah(a, b)}")
    print(f"Hasil {a} - {b} = {kurang(a, b)}")

if __name__ == "__main__":
    main()