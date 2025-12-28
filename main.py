import time
import random

# Binary Search Iteratif
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, steps, True
        elif arr[mid] < target:     # descending
            high = mid - 1
        else:
            low = mid + 1

    return low, steps, False


# Binary Search Rekursif
def binary_search_recursive(arr, target, low, high, steps=0):
    if low > high:
        return low, steps, False

    steps += 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid, steps, True
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, low, mid - 1, steps)
    else:
        return binary_search_recursive(arr, target, mid + 1, high, steps)


# Buat Leaderboard
def buat_leaderboard(n, tipe):
    if tipe == "int":
        data = [random.randint(1000, 1_000_000) for _ in range(n)]
    else:
        data = [round(random.uniform(1000, 1_000_000), 2) for _ in range(n)]
    return sorted(data, reverse=True)


# Program Utama
def main():
    print("Penelitian Binary Search pada Leaderboard Game")

    # Pilih ukuran leaderboard
    try:
        n = int(input("Masukkan ukuran leaderboard: "))
        if n <= 0:
            print("Ukuran harus lebih besar dari 0.")
            return
    except ValueError:
        print("Ukuran harus berupa angka.")
        return

    # Pilih jenis data
    tipe = input("Pilih jenis data (int / float): ").lower()
    if tipe not in ["int", "float"]:
        print("Jenis data tidak valid.")
        return

    leaderboard = buat_leaderboard(n, tipe)

    while True:
        # Tampilkan leaderboard
        print(f"\nLeaderboard (20 skor teratas dari n = {n}):")
        counter = 1
        for score in leaderboard[:20]:
            print(counter, score)
            counter += 1

        masukan = input("\nMasukkan skor yang ingin dicari (atau -1 untuk keluar): ")
        if masukan == "-1":
            print("Terima kasih, program selesai.")
            break

        target = int(masukan) if tipe == "int" else float(masukan)

        # Pengujian waktu (5x)
        percobaan = 5
        iteratif_times = []
        rekursif_times = []

        for _ in range(percobaan):
            start = time.perf_counter()
            idx_i, steps_i, found_i = binary_search_iterative(leaderboard, target)
            iteratif_times.append((time.perf_counter() - start) * 1_000_000)

            start = time.perf_counter()
            idx_r, steps_r, found_r = binary_search_recursive(
                leaderboard, target, 0, len(leaderboard) - 1
            )
            rekursif_times.append((time.perf_counter() - start) * 1_000_000)

        avg_i = sum(iteratif_times) / percobaan
        avg_r = sum(rekursif_times) / percobaan

        # Output posisi
        if found_i:
            print(f"\nSkor {target} ditemukan di peringkat {idx_i + 1}")
        else:
            if idx_i == 0:
                print("\nSkor lebih tinggi dari skor tertinggi leaderboard")
            elif idx_i == len(leaderboard):
                print("\nSkor lebih rendah dari skor terendah leaderboard")
            else:
                print(f"\nSkor berada di antara {leaderboard[idx_i-1]} dan {leaderboard[idx_i]}")
            print(f"Rank (posisi sisip): {idx_i + 1}")

        # Analisis Efisiensi
        print("\nAnalisis Efisiensi")
        print(f"Langkah Iteratif  : {steps_i}")
        print(f"Langkah Rekursif  : {steps_r}")
        print(f"Rata-rata waktu Iteratif : {avg_i:.3f} µs")
        print(f"Rata-rata waktu Rekursif : {avg_r:.3f} µs")

        if avg_i < avg_r:
            print("=> Iteratif lebih efisien")
        else:
            print("=> Rekursif lebih efisien")

        print("-" * 50)


main()