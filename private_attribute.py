class Product():
    __items = 4 # private
 
    def __init__(self, nama_barang):
        self.nama = nama_barang
 
    def harga_barng(self,harga_barang):
       hasil = self.__items * harga_barang
       return hasil
 
baju = Product("baju")
print(baju.harga_barng(900))
