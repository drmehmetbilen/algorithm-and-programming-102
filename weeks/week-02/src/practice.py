class Node():
    """
    Binary Search Tree  için Temel Düğüm  Sınıfı.
    Bu sınıf ağacın her bir yapı taşını oluşturur.
    
    Özellikler:
     value (int): Sıralama anahtarı. Ağaçtaki konumu belirler.
     text (str): Düğümün taşıdığı asıl veri.
     left (Node): Kendinden küçük değerlerin tutulduğu sol düğüm.
     right (Node): Kendinden büyük değerlerin tutulduğu sağ düğüm.
    """
    def __init__(self, text, value):
        self.value = value
        self.text = text
        self.left = None
        self.right = None

class BinaryTree():
    """
    Binary Search Tree (İkili Arama Ağacı) Uygulaması.
    
    * Çalışma Mantığı:
    * Kökten (Root) başlar.
    * Eklenen her yeni değer kök ile kıyaslanır.
    * Küçükse SOL kola, Büyükse SAĞ kola yönlendirilir.
    """
    
    def __init__(self, text: str, value: int):
        """
        Ağacı başlatan oluşturucu metot .
        Ağaç boş kalamaz başlatılırken mutlaka bir kök (root) atanır.
        
        Parametreler:
            self: Kendisi.
            text: Kök düğümün verisi.
            value: Kök düğümün sayısal değeri.
        """
        self.root = Node(text, value)
          
    def add_node(self, text:str, value:int):
        """
        Ağaca yeni bir düğüm ekler. 
        
        Algoritmanın mantığı:
        1. Kökten başla.
        2. Eklenecek değer (value) ile mevcut düğümü kıyasla.
        3. Küçükse sola  büyükse sağa git.
        4. Boş bir yer (None) bulana kadar ilerle ve oraya yerleş.
        """
        new_node = Node(text, value)
        current_node = self.root
        
        while True:
            if value > current_node.value:
                # Durum 1: Yeni değer mevcut düğümden büyük ise == sağa git
                if current_node.right is None:
                    # Sağ taraf boşsa buraya yerleş.
                    current_node.right = new_node
                    break
                else:
                    # Doluysa: sağdaki düğüme geç ve döngüye devam et.
                    current_node = current_node.right
    
            elif value < current_node.value:
                # Durum 2: Yeni değer mevcut düğümden küçük ise == sola git
                if current_node.left is None:
                    # Sol taraf boşsa buraya yerleş.
                    current_node.left = new_node
                    break
                else:
                    # Doluysa: soldaki düğüme geç ve döngüye devam et.
                    current_node = current_node.left
            
            # Durum 3: Eşitlik durumu olursa  (Tekrar eden değer olursa yazılmaz)
            else:
                print("ERROR : Value is already exist!! (Bu değer zaten ağaçta var)")
                break

    def search_value(self, value):
        """
        Ağaç içinde belirli bir değeri arar.
        
        Algoritmanın mantığı:
          * Hepsine tek tek bakmaz.
          * Aranan değer küçükse sadece sol tarafa , büyükse sadece sağ tarafa bakar.
          * Bu sayede arama işlemi çok hızlı gerçekleşir.
        
        Geri dönüş:
            str: Bulunursa veriyi (text) , bulunamazsa hata mesajını döner.
        """
        current_node = self.root
        while True:
            # Hedef Bulundu!
            if current_node.value == value:
                return current_node.text
             
            if value < current_node.value:
                # Aranan değer küçükse == Sola bak
                if current_node.left is None:
                    return "ERROR : Not found." # Yol bitti bulunamadı.
                current_node = current_node.left
        
            elif value > current_node.value:
                # Aranan değer büyükse == Sağa bak
                if current_node.right is None:
                    return "ERROR : Not found" # Yol bitti  bulunamadı.
                current_node = current_node.right

    def size(self):
        """
        Ağaçtaki toplam eleman (düğüm) sayısını döner.
        """
        return self._size(self.root)
        
    def _size(self, current_node):
        """
        size() fonksiyonu için yardımcı metot.
        
        Mantığı:
        Bir düğümün boyutu = 1 (Kendisi) + Solun boyutu + Sağın boyutu
        """
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self):
        """
        Ağacın yüksekliğini hesaplar.
        Kökten en uzaktaki yaprağa olan mesafedir.
        """
        return self._height(self.root)
    
    def _height(self, current_node):
        """
        height() fonksiyonu için yardımcı metot.
        
        Mantığı:
        Bir düğümün yüksekliği = 1 + Hangi taraf daha derinse orası (max)
        """
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left), self._height(current_node.right))

# Kodumuzu test edelim:
if __name__ == "__main__":
    # 1. Ağacı Kök (Mehmet , 32) ile başlatıyoruz.
    my_tree = BinaryTree("Mehmet", 32)
    
    # 2. Yeni düğümler ekliyoruz. (Küçükler sola, büyükler sağa otomatik yerleşir)
    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)


    print(my_tree.search_value(41)) # Vermesini beklediğimiz değer: Ata
    print(my_tree.search_value(82)) # 82 numara ağacımızda olmadığından vermesini beklediğimiz değer : EROR
    print(my_tree.size()) # Vermesini beklediğimiz değer : 7
    print(my_tree.height()) # Vermesini beklediğimiz değer : 5
