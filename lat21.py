kuadrat = lambda x: x ** 2
print(kuadrat(4))          

siswa = [("Ani", 80), ("Budi", 95)]
print(max(siswa, key=lambda s: s[1]))


x = "global"
def tes():
    x = "lokal"		#hanya di dalam tes()
    print(x)		#lokal
tes()
print(x)		    #global