
# Binary Search Tree her düğümün (node) en fazla
# iki çocuğa sahip olduğu ve şu kurala uyan bir veri yapısıdır:
#   - Sol çocuğun değeri ebeveynden küçük olmalıdır.
#   - Sağ çocuğun değeri ebeveynden büyük olmalıdır.
#
# Bu kural sayesinde arama, ekleme ve silme işlemleri çok daha hızlı gerçekleşir.
#
# İşlemler:
#   - add_node    : Yeni düğüm ekleme
#   - search_value: Değeri arama
#   - size        : Ağaçtaki toplam düğüm sayısı
#   - height      : Ağacın yüksekliği (derinliği)
#   - delete_node : Düğüm silme
# ============================================================


class Node():
    """
    BST'deki her bir düğümü (node) temsil eden sınıf.

    Özellikler:
        text  (str)  : Düğümün taşıdığı metin verisi.
        value (int)  : Düğümün sayısal değeri ağaçtaki konumunu belirler.
        left  (Node) : Sol çocuk düğüm (değeri daha küçük olan).
        right (Node) : Sağ çocuk düğüm (değeri daha büyük olan).
    """

    def __init__(self, text: str, value: int):
        """
        Node nesnesini başlatır.

        Argümanlar:
            text  (str) : Düğüme atanacak metin verisi.
            value (int) : Düğüme atanacak sayısal değer.

        Olası hatalar:
            TypeError : text str, value int değilse hata verir.
        """
        if not isinstance(text, str):
            raise TypeError(f"text parametresi(ilk parametre) string olmalıdır.")
        if not isinstance(value, (int, float)):
            raise TypeError(f"'value' parametresi(ikinci parametre) sayısal olmalıdır.")

        self.value = value   # int  — Ağaçtaki konumu belirleyen sayısal anahtar
        self.text  = text    # str  — Düğümün taşıdığı metin/isim verisi
        self.left  = None    # Node — Sol çocuk (başlangıçta boş)
        self.right = None    # Node — Sağ çocuk (başlangıçta boş)


class BinaryTree():
    """
    Binary Search Tree yapısını temsil eden sınıf.

    BST kuralı: Her düğümün sol alt ağacındaki tüm değerler o düğümden
    küçük, sağ alt ağacındaki tüm değerler ise büyüktür.

 *                        ┌─────┐
 *                        │  50 │          ← KÖK (root)
 *                        └──┬──┘
 *               ┌───────────┴───────────┐
 *            ┌──┴──┐               ┌────┴──┐
 *            │  30 │               │  70   │
 *            └──┬──┘               └───┬───┘
 *          ┌────┴────┐          ┌──────┴─────┐
 *       ┌──┴──┐   ┌──┴──┐    ┌──┴──┐      ┌──┴──┐
 *       │  20 │   │  40 │    │  60 │      │  80 │
 *       └──┬──┘   └─────┘    └─────┘      └──┬──┘
 *       ┌──┴──┐                           ┌──┴──┐
 *       │  10 │                           │  90 │
 *       └─────┘                           └─────┘
    

    Özellikler:
        root (Node): Ağacın kök (ana) düğümü.
    """

    def __init__(self, text: str, value: int):
        """
        Ağacı kök düğümle başlatır.

        Argümanlar:
            text  (str) : Kök düğümün metin verisi.
            value (int) : Kök düğümün sayısal değeri.

        Olası Hatalar:
            TypeError: Geçersiz parametre tipi girilirse hata verir.

        Örnek:
            >>> tree = BinaryTree("Kök", 50)
        """
        self.root = Node(text, value)   # Node — Tüm ağacın başlangıç noktası

    # ----------------------------------------------------------
    # EKLEME (ADD NODE)
    # ----------------------------------------------------------

    def add_node(self, text: str, value: int) -> None:
        """
        Ağaca yeni bir düğüm ekler.

        BST kuralına göre:
          - Yeni değer mevcut düğümden büyükse  → sağa git
          - Yeni değer mevcut düğümden küçükse  → sola git
          - Uygun boş yer bulununca(kurala göre sağda veya solda gidilecek düğüm kalmayınca) düğümü oraya yerleştir.

        Argümanlar:
            text  (str) : Yeni düğümün metin verisi.
            value (int) : Yeni düğümün sayısal değeri.

        Olası Hatalar:
            TypeError : Geçersiz parametre tipi girilirse hata verir.
            ValueError: Aynı value zaten varsa hata verir.

        Örnek:
            >>> tree.add_node("Ankara", 20)
        """
        new_node     = Node(text, value)   # Node — Eklenmek üzere oluşturulan yeni düğüm
        current_node = self.root           # Node — Dolaşım için başlangıç noktası (kök)

        while True:
            if value > current_node.value:
                # Yeni değer daha büyük → sağ tarafa bakıyoruz
                if current_node.right is None:
                    current_node.right = new_node  # Boş yer bulundu - ekle
                    break
                else:
                    current_node = current_node.right  # Boş değilse devam et
            elif value < current_node.value:
                # Yeni değer daha küçük → sol tarafa bakıyoruz
                if current_node.left is None:
                    current_node.left = new_node   # Boş yer bulundu -ekle
                    break
                else:
                    current_node = current_node.left   # Boş değilse devam et
            else:
                # BST'de aynı değerden iki düğüm olamaz!
                raise ValueError(f"HATA: {value} değeri zaten mevcut! BST'de tekrar eden değer eklenemez.")

    # ----------------------------------------------------------
    # ARAMA (SEARCH VALUE)
    # ----------------------------------------------------------

    def search_value(self, value: int) -> str:
        """
        Verilen sayısal değere sahip düğümü arar ve metin verisini döner.

        BST'nin yapısı sayesinde her adımda arama alanı yarıya iner.
        Bu direkt aramaya göre çok daha hızlıdır.

        Argümanlar:
            value (int): Aranacak sayısal değer.

        Dönen Değer:
            str: Bulunan düğümün text verisi.

        Olası Hatalar:
            TypeError : value sayısal değilse hata verir.
            KeyError  : Değer ağaçta bulunamazsa hata verir.

        Örnek:
            >>> tree.search_value(20)
            'Ankara'
        """
        if not isinstance(value, int):
            raise TypeError(f"'value' sayısal değer olmalıdır.")

        current_node = self.root   # Node — Aramanın başladığı düğüm

        while current_node is not None:
            if current_node.value == value:
                return current_node.text           # Bulundu!
            elif value < current_node.value:
                current_node = current_node.left   # Value düğümün valuesinden küçükse sol tarafa git
            else:
                current_node = current_node.right  # Value düğümün valuesinden büyükse sağ tarafa git

        # Döngü bitti ama bulunamadı
        raise KeyError(f"HATA: {value} değeri ağaçta bulunamadı.")

    # ----------------------------------------------------------
    # BOYUT (SIZE)
    # ----------------------------------------------------------

    def size(self) -> int:
        """
        Ağaçtaki toplam düğüm sayısını döner.

        Tüm düğümleri recursive olarak sayar.

        Dönen Değer:
            int: Toplam düğüm sayısı.

        Örnek:
            >>> tree.size()
            7
        """
        return self._size(self.root)

    def _size(self, current_node: 'Node') -> int:
        """
        Recursive yardımcı metodudur — size() tarafından çağrılır.

        Argümanlar:
            current_node (Node): İşlenen düğüm.

        Dönen Değer:
            int: Bu düğüm ve altındaki tüm düğümlerin sayısı.
        """
        if current_node is None:
            return 0
        # Bu düğüm (1) + sol alt ağaç boyutu + sağ alt ağaç boyutu
        return 1 + self._size(current_node.left) + self._size(current_node.right)
    
    #      A 
    #     / \
    #    B   C
    #   / \
    #  D   E

    # 1. Adım — _size(A) çağrılır:
    # "A'nın altında kaç düğüm var?"
    # = 1 (kendisi) + _size(B) + _size(C)

    # 2. Adım — _size(B) çağrılır:
    # "B'nin altında kaç düğüm var?"
    # = 1 (kendisi) + _size(D) + _size(E)

    # 3. Adım — _size(D) çağrılır:
    # "D'nin altında kaç düğüm var?"
    # = 1 (kendisi) + _size(None) + _size(None)
    #                   ↓                ↓
    #                   0                0
    # = 1 + 0 + 0 = 1  ✅

    # 4. Adım — _size(E) çağrılır:
    # "E'nin altında kaç düğüm var?"
    # = 1 (kendisi) + _size(None) + _size(None)
    #                   ↓                ↓
    #                   0                0
    # = 1 + 0 + 0 = 1  ✅

    # 5. Adım — Artık B sonucunu hesaplayabiliriz:
    # _size(B) = 1 (kendisi) + _size(D) + _size(E)
    #         =      1       +     1    +     1
    #         = 3  ✅

    # 6. Adım — _size(C) çağrılır:
    # "C'nin altında kaç düğüm var?"
    # = 1 (kendisi) + _size(None) + _size(None)
    #                   ↓                ↓
    #                   0                0
    # = 1 + 0 + 0 = 1  ✅

    # 7. Adım — Artık A sonucunu hesaplayabiliriz:
    # _size(A) = 1 (kendisi) + _size(B) + _size(C)
    #         = 1       +     3    +     1
    #         = 5  ✅

    # Fonksiyon önce en alta kadar iner sonra yukarı çıkarken toplar.
    



    # ----------------------------------------------------------
    # YÜKSEKLİK (HEIGHT)
    # ----------------------------------------------------------

    def height(self) -> int:
        """
        Ağacın yüksekliğini (derinliğini) döner.

        Yükseklik: Kökten en derin yaprağa kadar olan düğüm sayısı.
        Tek düğümlü ağacın yüksekliği 1'dir.
        Temel mantık:
        "Ben (1) + sol kolum ne kadar uzun, sağ kolum ne kadar uzun → hangisi uzunsa onu al"

        Dönen Değer:
            int: Ağacın yüksekliği.

        Örnek:
            >>> tree.height()
            5
        """
        return self._height(self.root)

    def _height(self, current_node: 'Node') -> int:
        """
        Recursive yardımcı metot — height() tarafından çağrılır.

        Args:
            current_node (Node): İşlenen düğüm.

        Dönen Değer:
            int: Bu düğüm altındaki en uzun yolun uzunluğu.
        """
        if current_node is None:
            return 0
        # Sol ve sağ alt ağaçların yüksekliğinin büyüğü + bu düğüm
        return 1 + max(self._height(current_node.left), self._height(current_node.right))
    
    # Size ve height fonksiyonları benzer şekilde çalışır ancak farklı bir şeyi hesaplarlar.
    # Yükseklik hesaplamasında her düğümün kendisi 1 olarak sayılır ve alt ağaçların yüksekliği karşılaştırılarak en uzun olan seçilir.
    #      A 
    #     / \
    #    B   C
    #   / \
    #  D   E
    # Örneğin bu ağaçta _height(A) çağrılır ve 1 (ben) + max(_height(B), _height(C)) hesaplanır mantık size ile aynıdır max fonksiyonu sayesninde
    # _height(B) veya _height(C) den hangisi daha büyükse o seçilir 1 eklenir ve sonuç olarak ağacın yüksekliği bulunur.


    # ----------------------------------------------------------
    # SİLME (DELETE NODE)
    # ----------------------------------------------------------

    def delete_node(self, value: int) -> None:
        """
        Verilen değere sahip düğümü ve o düğümün tüm alt ağacını siler.

        Hedef düğümün altındaki her şey (sol/sağ alt ağaç dahil) tamamen
        ağaçtan çıkarılır. Ebeveyn düğümün ilgili bağlantısı None yapılır.

        Örnek: delete_node(9) çağrılırsa aşağıdaki tüm düğümler silinir:
                      32
                     /
                    9        ← bu silinir
                   / \
                  ?   15     ← bunlar da silinir
                      ...

        Arguamanlar:
            value (int): Silinecek düğümün sayısal değeri.

        Olası Hatalar:
            TypeError : value sayısal değilse hata verir.
            KeyError  : Silinmek istenen değer ağaçta yoksa hata verir.
            ValueError: Kök düğümü silmeye çalışılırsa hata verir
                        (kök silinirse ağaç tamamen yok olur).

        Örnek:
            >>> tree.delete_node(9)   # 9 ve altındaki tüm düğümler silinir
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"'value' int veya float olmalıdır.")

        if self.root is None:
            raise KeyError("HATA: Ağaç boş, silinecek düğüm bulunamadı.")

        if self.root.value == value:
            raise ValueError("HATA: Kök düğüm silinemez. Kök silinirse ağaç tamamen yok olur.")

        self.root = self._delete_subtree(self.root, value)

    def _delete_subtree(self, current_node: 'Node', value: int) -> 'Node':
        """
        Recursive yardımcı metot — delete_node() tarafından çağrılır.

        Hedef düğümü arar; bulduğunda o düğümü ve tüm alt ağacını silerek
        ebeveyne None döner. Böylece o kol tamamen kopar.

        Arguamanlar:
            current_node (Node) : Şu an işlenen düğüm.
            value        (int)  : Silinecek değer.

        Dönen Değer:
            Node | None: Güncellenen alt ağacın kök düğümü.

        Olası Hatalar:
            KeyError: Değer bulunamazsa hata verir.
        """
        if current_node is None:
            # Ağacın sonuna gelindi fakat değer bulunamadı
            raise KeyError(f"HATA: {value} değeri ağaçta bulunamadı, silinemez.")

        if value < current_node.value:
            # Hedef sol alt ağaçta, devam et
            current_node.left = self._delete_subtree(current_node.left, value)

        elif value > current_node.value:
            # Hedef sağ alt ağaçta, devam et
            current_node.right = self._delete_subtree(current_node.right, value)

        else:
            # Hedef düğüm bulundu — silme işlemi yapılacak
            # Sol ve sağ çocukları korumadan direkt None döndürüyoruz.
            # Python düğümü ve tüm alt ağacını
            # otomatik olarak bellekten temizler.
            return None  # Bu düğüm + tüm alt ağaç silindi

        return current_node

    def _find_min(self, current_node: 'Node') -> 'Node':
        """
        Bir alt ağaçtaki minimum değerli düğümü bulur.

        BST'de en küçük değer her zaman en soldaki düğümdür.

        Argümanlar:
            current_node (Node): Arama başlangıç düğümü.

        Dönen Değer:
            Node: Minimum değerli düğüm.
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


# ==============================================================
# ANA PROGRAM — Test ve Kullanım Örneği
# ==============================================================

if __name__ == "__main__":

    # Ağaç oluşturuluyor (kök düğüm: Mehmet, 32)
    my_tree = BinaryTree("Mehmet", 32)

    # Düğümler ekleniyor
    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)

    # Arama testi
    print(f"41 değerindeki düğüm : {my_tree.search_value(41)}")   # Ata
    print(f"9  değerindeki düğüm : {my_tree.search_value(9)}")    # Sabriye

    # Boyut ve yükseklik
    print(f"\nAğaç boyutu    : {my_tree.size()}")     # 7
    print(f"Ağaç yüksekliği: {my_tree.height()}")    # 5

    # Silme testi
    print(f"Silmeden önce boyut: {my_tree.size()}")

    my_tree.delete_node(15)   # Yaprak düğüm (Burdur)
    print(f"15 (Burdur) silindi → boyut: {my_tree.size()}")

    my_tree.delete_node(9)    # İki çocuklu düğüm (Sabriye)
    print(f"9  (Sabriye) silindi → boyut: {my_tree.size()}")
