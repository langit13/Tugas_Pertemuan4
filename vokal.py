# Delete huruf vokal
def hapusVokal(kalimat):
    for i in "aeiouAEIOU":
        # Menggunakan fungsi replace untuk merubah setiap huruf vokal menjadi string kosong
        kalimat = kalimat.replace(i, "")
    return kalimat

print(hapusVokal(input("")))
