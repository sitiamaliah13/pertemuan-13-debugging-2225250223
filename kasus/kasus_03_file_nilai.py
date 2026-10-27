def baca_nilai(nama_file):
    with open(nama_file, "r") as file:
        data = file.readlines()

    return data


print(baca_nilai("data/nilai.txt"))