class Kendaraan(object):

  def __init__(self, nama):
    self.nama = nama
    self.penumpang = []
    
  def tambah_penumpang(self, nama_penumpang):
    self.penumpang.append(nama_penumpang)
    
# membuat class Mobil yang merupakan turunan Kendaraan
class Mobil(Kendaraan):
  pintu_terbuka = False
  
  def buka_pintu(self):
    self.pintu_terbuka = True
  def tutup_pintu(self):
    self.pintu_terbuka = False
    
mobnas = Mobil("MobilSaya")

# mobnas akan memiliki properti dari Kendaraan
mobnas.tambah_penumpang("Wiranto")
print ("Penumpang: " + str(mobnas.penumpang))
# dan memiliki properti Mobil
mobnas.buka_pintu()
print ("Pintu terbuka: " + str(mobnas.pintu_terbuka))
