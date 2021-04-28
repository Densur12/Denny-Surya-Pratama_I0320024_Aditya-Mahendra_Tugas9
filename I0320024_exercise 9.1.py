#####################################################
# nama file: array2.py
#####################################################
import sys

# mendefinisikan array konstan
HARI = ("minggu", "senin", "selasa", "rabu", "kamis", "jumat", "sabtu")

def main():
    #meminta user memasukkan nomor hari
    nohari = int(input("masukkan nomor hari [1..7] : "))

    if (nohari < 1) or (nohari > 7) :
        print ("Tidak ada hari ke-%s" % nohari)
        sys.exit(1)

        print("hari ke -%d adalah %s" % (nohari, HARI[nohari-1]))

    if __name__ == "__main__":
        main()