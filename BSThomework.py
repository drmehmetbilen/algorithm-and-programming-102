from typing import Optional, Tuple

"""
PROJE STANDARTLARI:
- Mantık: Ağaç bütünlüğünü korumak için 'Pointer Re-linking' (Bağlantı Yeniden Kurma) ile özyinelemeli silme.
- Optimizasyon: İki çocuklu düğüm silme işlemlerinde 'Successor' stratejisi.
- Dokümantasyon: Tip İpuçları (Type Hints) ve Docstring ile kendi kendini belgeleyen kod yapısı.
- Güvenilirlik: Boş kök dizinleri ve bulunamayan anahtarlar için uç durum (Edge Case) yönetimi.
"""
"""
NOT:
Optional:Sol ve sağ çocukların boş (None) olabileceğini tip sistemine bildirerek 'Null Pointer' hatalarını önceden önler.
"""

class Node:
    """
    BST içerisindeki her bir düğümü (node) temsil eden veri yapısı.

    Özellikler:
        text : Düğümün taşıdığı veris.
        value : Düğümün sayısal değerini (konumunu) belirler.
        left : Sol çocuk düğüm (değeri daha küçük).
        right : Sağ çocuk düğüm (değeri daha büyük).
    """
    def __init__(self, text: str, value: int) -> None:
        self.text: str = text
        self.value: int = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class BinaryTree:
    """
    Binary Search Tree (BST) ana yönetim sınıfı.
    BST Kuralı:
    Her düğümün sol çocuğu kendisinden küçük, sağ çocuğu ise kendisinden büyük değer taşır.
    """

    def __init__(self, text: Optional[str] = None, value: Optional[int] = None):
        """
        Ağacı başlatan metod.
        Parametreler:
        text (str): Düğümün metin verisi.(Örn: 'Mehmet')
        value (int): Düğümün sayısal değeri.
        """
        # Eğer dışarıdan bir isim ve değer geldiyse ağacı dolu başlatır.
        if text is not None and value is not None:
            self.root: Optional[Node] = Node(text, value)
        # Gelmediyse ağacı boş (None) olarak başlatır.
        else:
            self.root: Optional[Node] = None

    # EKLEME (ADD NODE)       

    def add_node(self, text: str, value: int) -> None:
        """
        Ağaca yeni bir düğüm ekler.
        Aynı değer eklenirse ValueError hatası verir. 
        BST kuralına göre küçük değerleri sola, büyükleri sağa yerleştirerek ağacı büyütür.

        Strateji:
        Özyineleme yerine 'while' döngüsü kullanılır. Ekleme tek bir hat üzerinde (aşağı) ilerlediği için 
        döngü belleği (RAM) daha verimli kullanır ve 'Stack Overflow' riskini ortadan kaldırır.
        """
        new_node = Node(text, value)
        current_node = self.root

        # Durum 1: Ağaç boşsa, yeni düğüm 'Kök' olur.
        if self.root is None:
            self.root = new_node
            return

        # Durum 2: Ağaç doluysa, boş yeri bulana kadar aşağı inilir.
        while True:
            # Gelen değer büyükse sağ tarafa gidilir.
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break # Yer bulundu, döngüden çık.
                current_node = current_node.right
            
            # Gelen değer küçükse sol tarafa gidilir.
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break # Yer bulundu, döngüden çık.
                current_node = current_node.left
            
            # Değer zaten mevcutsa hata verir.
            else:
                raise ValueError(f"Duplicate Error: {value} zaten mevcut!")
            
    # ARAMA (SEARCH VALUE)
            
    def search_value(self, value: int) -> str:
        """
        Ağaçta sayısal bir değere göre arama yapar. 
        Bulursa o değerin karşılık geldiği metni, bulamazsa None dönderir.

        Strateji:
        Her adımda tek bir yöne gidildiğinden özyineleme yerine döngü tercih edilmiştir.
        """
        current_node: Optional[Node]= self.root
        
        while current_node:
            # Aranan değer bulundu.
            if current_node.value == value:
                return current_node.text
            # Değer küçükse sola git.
            if value<current_node.value:
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            # Değer büyükse sağa git.    
            elif value>current_node.value:
                if current_node.right is None:
                    return "ERROR : Not found"
                current_node = current_node.right
        return "ERROR : Not found."
    
    # BOYUT (SIZE)

    def size(self) -> int:
            """
            Kullanıcının çağırdığı ana metot. 
            Ağaçtaki toplam düğüm sayısını dönderir.
            """
            # İşlemi en tepeden (root) başlatması için işlemin yapılacağı _size fonksiyonuna devreder.
            return self._size(self.root)
            
    def _size(self, current_node: Optional[Node]) -> int:
        """
        Recursive çalışan yardımcı metod.
        Base Case  : Düğüm yoksa 0 döner.
        Recursive  : 1 (kendim) + sol boyut + sağ boyut.
        """

        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)
    
    # YÜKSEKLİK (HEIGHT)

    def height(self) -> int:
            """
            Kullanıcının çağırdığı ana metot. 
            Ağacın en derin noktasına olan uzaklığı (en uzun yolu) döndürür.
            """
            # En tepeden (root) ölçümü başlatır.
            return self._height(self.root)

    def _height(self, current_node: Optional[Node]) -> int:
        """
        Yardımcı metot. Her dalın boyunu ölçer ve en uzununu seçer.
        Base Case  : Düğüm yoksa 0 döner.
        Recursive  : 1 (kendim) + (sol dal mı yoksa sağ dal mı daha derin?).
        max() fonksiyonu en uzun yolu otomatik seçer.
        """
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left), self._height(current_node.right))
    
    # SİLME (DELETE)

    def delete(self, value: int) -> bool:
        """
        Kullanıcının çağırdığı ana silme metodu.
        Silme başarılıysa True, değer bulunamadıysa False döner.
        """
        self.root, deleted = self._delete(self.root, value)
        return deleted

    def _delete(self, current: Optional[Node], value: int) -> Tuple[Optional[Node], bool]:
        """
        Recursive silme — 'Pointer Re-linking' stratejisiyle.

        Her recursive çağrı, tamamlandığında üst düğüme 'yeni çocuğun budur' diye haber verir.
        Böylece ağaçta kopma (dangling pointer) yaşanmaz.

        Silme Senaryoları:
            1. Değer bulunamadı      → None, False döner.
            2. Yaprak düğüm          → Direkt silinir.
            3. Tek çocuklu düğüm     → Çocuk yukarı alınır.
            4. İki çocuklu düğüm     → Successor stratejisi uygulanır.

        NOT:
            Silinen düğümün yerine geçecek değer; 
            solundaki tüm değerlerden büyük, sağındakilerden küçük olmalıdır.
            Sağ alt ağacın en küçüğü (successor) bunu sağlar.
        """
        # Durum 1: Değer ağaçta yoksa
        if current is None:
            return None, False

        # Durum 2: Aranan değeri bulana kadar dallarda ilerle
        if value < current.value:
            current.left, deleted = self._delete(current.left, value)
            return current, deleted
        elif value > current.value:
            current.right, deleted = self._delete(current.right, value)
            return current, deleted

        # Durum 3 : Değer bulundu.
        else:
            # 1 : Hiç çocuğu yoksa (Yaprak)
            if current.left is None and current.right is None:
                return None, True

            # 2 : Sadece sağ çocuğu varsa
            elif current.left is None:
                return current.right, True

            # 3 : Sadece sol çocuğu varsa
            elif current.right is None:
                return current.left, True

            # 4 : İki çocuğu da varsa
            else:
                # Sağ tarafın en küçüğünü buluyoruz
                successor = self.min_node(current.right)
                current.value = successor.value
                current.text = successor.text
                # Aşağıda kalan fazla kopyanın silinmesi ve pointer'ın yeniden bağlanması.
                current.right, _ = self._delete(current.right, successor.value)
                return current, True

    def min_node(self, node: Node) -> Node:
        """Verilen alt ağacın en sol (en küçük) düğümünü bulur."""
        while node.left is not None:
            node = node.left
        return node

# TEST

if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet", 32)
    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)

    print(f"Toplam Eleman  : {my_tree.size()}")     #7
    print(f"Ağaç Yüksekliği: {my_tree.height()}")   #4
        
    # Arama Testi
    print(f"42 değerindeki düğüm : {my_tree.search_value(42)}")   # Konya
    print(f"15  değerindeki düğüm : {my_tree.search_value(15)}")    #Burdur

    #Silme Testi
    my_tree.delete(11)   
    print(f"11-Bilecik silindi → Güncel boyut: {my_tree.size()}")   #6   

    my_tree.delete(41)   
    print(f"41-Ata silindi → Güncel boyut: {my_tree.size()}")   #5

    my_tree.delete(6)   
    print(f"6 değeri bulunamadı.→ Güncel boyut: {my_tree.size()}")  #5       