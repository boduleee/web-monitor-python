import urllib.request

class WebMonitor:
    def __init__(self, nazev_projektu):
        self.nazev = nazev_projektu
        self.seznam_webu = []

    def pridej_web(self, url):
        """Přidá novou adresu do seznamu pro kontrolu."""
        self.seznam_webu.append(url)
        print(f"➕ Přidán web ke sledování: {url}")

    def zkontroluj_vse(self):
        """Projde všechny weby a vypíše jejich stav."""
        print(f"\n--- Spouštím kontrolu pro projekt: {self.nazev} ---")
        
        for url in self.seznam_webu:
            try:
                status = urllib.request.urlopen(url).getcode()
                if status == 200:
                    print(f"✅ {url} -> Funguje bez problému.")
            except Exception as e:
                print(f"❌ {url} -> CHYBA! Detaily: {e}")


# --- Spuštění programu ---
if __name__ == "__main__":
    # Vytvoříme objekt našeho monitoru
    muj_hlidac = WebMonitor(nazev_projektu="Moje První IT Portfolio")
    
    # Přidáme weby, které chceme hlídat (můžete si dát jakékoliv vlastní)
    muj_hlidac.pridej_web("https://google.com")
    muj_hlidac.pridej_web("https://github.com")
    muj_hlidac.pridej_web("https://tento-web-neexistuje-12345.cz") # schválně pro test chyby
    
    # Spustíme hromadnou kontrolu
    muj_hlidac.zkontroluj_vse()
