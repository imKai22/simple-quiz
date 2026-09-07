import random
#mapel (add mapel like this)
#name1 = {
#  "question":"answer"
#}
IPA_bio = {
  "apa proses memngahsilkan energi pada tumbuhan":"fotosintesis",
  "istilah lain untuk pernapasan":"respirasi",
  "organ pencernaan manusia yang berfungsi sebagai penyerap nutrisi":"usus halus",
  "sel genetik paling dasar makhluk hidup":"DNA",
  #you can add inside here
}
IPA_kim = {
  "gasmulia dengan nomor atom 10":"Ne",
  "atom dengan ev 6 adalah":"O2",
  "rumus molekul metana":"CH4",
  "singkatan cloroflourocarbon":"CFC"
  #or here
}
#daftar mapel (add mapel list like this)
#name2 = list(x for x in name1.keys())
#then put the name of mapel (ex:Physics) to daftar below (don't forget use comma)
daftar = ["Kimia","Biologi"]
#----
kim = list(w for w in IPA_kim.keys())
bio = list(x for x in IPA_bio.keys())
#fungsi utama
def kuiz(mapel):
  if mapel not in daftar:
    return "Kesalahan terjadi"
    
  elif mapel in daftar and mapel == "Kimia":
    result = random.choice(kim)
    correct = IPA_kim[result]
    question = input(f"{result}?: ")
    if question == correct:
      return "Jawaban benar"
    else:
      return "Jawaban salah"
    
  elif mapel in daftar and mapel == "Biologi":
    result = random.choice(bio)
    correct = IPA_bio[result]
    question = input(f"{result}?: ")
    if question == correct:
      return "Jawaban benar"
    else:
      return "Jawaban salah"
  
  else:
    return "Kesalahan Terjadi"
  
#user mulai
user1 = input("Tulis 'START' untuk mulai ").upper()
if user1 == "START":
  print("\nPilih mapel: ")
  for i in daftar:
    print(i)
  user2 = input("Isi: ").capitalize()
  print(kuiz(user2))
else:
  print("Terjadi kesalahan atau dibatalkan pengguna")