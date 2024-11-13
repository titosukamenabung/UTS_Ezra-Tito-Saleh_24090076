masukan_tahun = 2020
masukan_tahun = int(input("masukan_tahun :"))
if ("masukan_tahun % 400 == 0"):
   True
elif ("masukan_tahun % 100 == 0"):
   False
elif ("masukan_tahun % 4 == 0"):
   True
masukan_tahun = int(input("masukan_tahun :"))
if (masukan_tahun):
   print(f"{masukan_tahun} adalah tahun kabisat")
else:
   print(f"{masukan_tahun} bukan tahun kabisat")