# Delete huruf vokal
#def hapusVokal(kalimat):
    #for i in "aeiouAEIOU":
        # Menggunakan fungsi replace untuk merubah setiap huruf vokal menjadi string kosong
        #kalimat = kalimat.replace(i, "")
    #return kalimat

#print(hapusVokal(input("")))#



#x = input("")

#vocal = ["a", "i", "u", "e", "o"]
#result = ""

#for i in x.lower():
    #if i not in vocal:
        #result += i

#print("result : ", result)



x = input("").replace("a","").replace("i","").replace("u","").replace("e","").replace("o","").lower()

print(x)