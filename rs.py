import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class rs:
    def __init__(self,data):
        self.data = pd.read_json(str(data))
    
    def fungsi(self):
        #Mendeteksi pencilan/outlier atau terdapat kesalahan dalam data
        if self.data['Rating X'].max() and self.data['Rating Y'].max() and self.data['Rating Z'].max() != self.data['Rating X'].max():
            print('Terdapat pencilan atau kesalahan di dalam data rating')
        #Mengurutkan setiap rata2 produk
        y = []
        for x in self.data.mean():
            y.append(x)
        urut = np.sort(y)
        
        #Menemukan produk dari rata2 rating dari yang tertinggi hingga yang terendah
        final = []
        for x in range(1,len(data.keys())+1):
            cari = self.data.mean() == urut[len(urut) - x]
            hasil = self.data.mean()[cari]
            final.append(hasil.keys())
        final1 = np.array(final)
        global akhir
        akhir = []
        for x in range(0,len(final1)):
            for y in final1[x]:
                akhir.append(y)

rs('data.json').fungsi()
data = pd.read_json('data.json')
print("Jadi barang pertama yang akan direkomendasikan adalah {} lalu barang kedua {} dan barang terakhir adalah {} dengan masing masing nilai rata ratanya adalah {},{},{}".format(akhir[0],akhir[1],akhir[2],data[akhir[0]].mean(),data[akhir[1]].mean(),data[akhir[2]].mean()))
print("")
x = np.array(akhir)
y = np.array([data[akhir[0]].mean(),data[akhir[1]].mean(),data[akhir[2]].mean()])
plt.plot(x,y)
plt.scatter(x,y)
plt.xlabel('Rating barang')
plt.ylabel('Nilai rata rata rating barang')
plt.title('Grafik rating rata rata dari 3 barang')
plt.show()
