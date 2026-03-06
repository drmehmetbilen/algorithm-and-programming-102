
# Binary Search Tree  (İkili Arama Ağacı)

# Node and Tree Class Definitations
# Add New Node
# Find Value
# Size
# Height
# Delete ?



class Node():
    """Düğüm (Node) tasarımı için kullanılan temel sınıftır
Bu sınıf, ikili arama ağacındaki her bir veri parçasını (öğrenciyi) temsil eder yani el ele tutuşan her bir nesnenin tarifidir"""


    def __init__(self, text, value):
        """Bu metod, düğümden yeni bir nesne türetildiği anda çalışır ve RAM'de yer ayırır"""
        self.value = value
        """ Düğümun içinde saklanan asıl veridir. Arama yapmak için kullanılır"""
        self.text = text
        """veri kısmıdır"""
        self.left = None
        """Bir düğümün solundaki tüm alt düğümler, o düğümün değerinden daha küçük değerler içerir."""

        self.right = None
        """Bir düğümün sağındaki tüm alt düğümler, o düğümün değerinden daha büyük değerler içerir."""
(Örnek Çalışma Mantığı
Diyelim ki elimizde 10 değeri var:
7 eklemek istersen: 7 < 10 olduğu için sola gider.
15 eklemek istersen: 15 > 10 olduğu için sağa gider)

class BinaryTree():

    """İkili Arama Ağacı (Binary Search Tree) yapısını yöneten ana sınıftır.
    Bu sınıf, düğümlerin (Node) birbirine mantıksal olarak bağlanmasını sağlar"""
    def __init__(self,text:str,value:int):
        """param text: İlk (Root) düğümün isim bilgisi.
        :param value: İlk (Root) düğümün sayısal değeri"""
        """
        This methods uses text and value to construct binary tree
        text: this parameter will be used as a key
        value: this parameter will be used as a position of the Node"""
   # Dışarıdan gelen bilgiyle ağacın en tepesindeki (Root) düğümü oluşturuyoruz 
        self.root = Node(text,value)
          
    def add_node(self,text,value):
        """Ağaca yeni bir eleman ekler,eklenen değer yine varsa hata verir.
        Mantık: Değer büyükse sağa, küçükse sola doğru giderek boş yer bulur"""
        new_node = Node(text,value)
        current_node = self.root
        while True:
             # Gidilecek yer varsa devam eder, yoksa yeni düğümü yerleştirir
            if value>current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
        
                    current_node = current_node.right
            elif value<current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                print("ERRROR : Value is already exist!!")
                break

    def search_value(self,value):
       """ Ağaç içerisinde belirli bir sayısal değeri arar.
        Hocanın derste belirttiği 'hızlı arama' mantığını kullanarak 
        her adımda arama alanını yarıya indirir.
        param value: Aranacak olan tam sayı değeri (Örn: 41).
        :return: Bulunursa düğümün ismini (text), bulunamazsa hata mesajı döner.
        """
        current_node = self.root
        while True:
            # Gidilecek bir düğüm olduğu sürece döngü devam eder
            if current_node.value == value:
                return current_node.text # Değer bulundu, ismi döndür
                   
            if value<current_node.value:    # Aranan değer mevcut düğümden küçükse sola, büyükse sağa git
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            elif value>current_node.value:
                if current_node.right is None:
                    return "ERROR : Not found"  
                current_node = current_node.right
                return "ERROR: Aranan değer bulunamadı." # Döngü biterse değer yoktur

    def _delete(self, node: Node, key: int):
        """
        Silme işlemi için arka planda çalışan özyinelemeli (recursive) yardımcı metot.
        """
        if node is None:
            return None, False

        # Silinecek düğümü bulana kadar ağaçta ilerle
        if key < node.value:
            node.left, deleted = self._delete(node.left, key)
        elif key > node.value:
            node.right, deleted = self._delete(node.right, key)
             else:
            # SİLİNECEK DÜĞÜM BULUNDU!
            # Durum 1 & 2: Düğümün hiç çocuğu yoksa veya sadece bir çocuğu varsa 
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True

            # Durum 3: Düğümün iki çocuğu varsa .
            # Sağ alt ağaçtaki en küçük düğümü (Successor) buluruz
            successor = self._min_node(node.right)
            node.value = successor.value
            node.text = successor.text
            # Successor'ı eski yerinden sileriz
            node.right, _ = self._delete(node.right, successor.value)
            return node, True
        return node, deleted



    

    def size(self):
              """  Ağaçtaki toplam düğüm (eleman) sayısını hesaplar
        Kökten başlayarak tüm alt dalları özyinelemeli (recursive) olarak topla"""

        return self._size(self.root)
        
    def _size(self, current_node):
                """Size hesaplaması için iç yardımcı metot"""

        if current_node is None:
            return 0
            
            # Temel Durum (Base Case):
            # Eğer düğüm None ise, bu alt ağaçta başka eleman yok demektir. 
            # Özyinelemeli (recursive) yapıyı sonlandırmak için 0 döneriz 
        return 1 + self._size(current_node.left) + self._size(current_node.right)
# Özyinelemeli Adım (Recursive Step):
        # Toplam boyutu bulmak için: Mevcut düğüm (1) + Sol alt ağaç + Sağ alt ağaç.
        # Bu yaklaşım 'Post-order Traversal' mantığına benzer bir derinlik öncelikli aramadır [

    def height(self):        
      """  kökten en uzak yaprağına kadar olan uzunluğunu (yüksekliğini) ölçer"""
        return self._height(self.root)
    def _height(self, current_node):
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left),self._height(current_node.right))





if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet",32)
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Emirhan",31)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Burdur",15)
    my_tree.add_node("Konya",42)
    my_tree.add_node("Bilecik",11)

    print(my_tree.search_value(41))
    print(my_tree.search_value(82))
    print(my_tree.size())
    print(my_tree.height())
