meme_dict = {
            "JOMOK": "Sesuatu yang sangat jorok dan memalukan",
            "PUNCAK KOMEDI": "Tanggapan umum terhadap sesuatu yang lucu",
            "BAWAKDEHEL BWAK": "Cara untuk menaggapi bahwa lelucon mu tdk lucu"
            }
            
# print(meme_dict)        

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
# print(word)

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("Kata Yg Diketik Adalah:", word)
    print("Artine:", meme_dict.get(word))
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Ketik Apaan Sih Lu??!!")
