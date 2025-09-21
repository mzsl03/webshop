1. Zsolti
### A rendszer célja

A rendszer célja, hogy az értékesítők számára egy modern, 
könnyen kezelhető és átlátható webes felületet biztosítson a termékek kezeléséhez és értékesítéséhez.
A felületnek lehetőséget nyújt a készletek nyomon követésére, a termékek keresésére és szűrésére, valamint a számlák kezelésére.
Fontos szempont, hogy az alaklamazás felhasználóbarát legyen, 
így a különböző technikai tudással rendelkező felhasználók is könnyen eligazodhatnak rajta.

A partnercégek számára biztosított felületen az értékesítők gyorsan elérhetik a hozzájuk tartozó üzletek készleteit,
és szükség esetén bővíthetik azokat egy virtuális raktárból.
Riportkészítési funkciót biztosít, amely lehetővé teszi a napi, heti és havi (utóbbi kettő autómatikusan, megadott rendszeresség alapján) 
értékesítési adatok megjelenítését Excel formátumban, így segítve az értékesítő munkáját, és a vállalat üzleti folyamatainak módosítását.

A több termék iránt érdeklődő vásárlók kielégítésének kulcsa a korsár funkció.
Az értékesítő munkatárs így egyszerre több termék árusítását tudja elvégezni.

A rendszer elsődleges célja, hogy csökkentse az értékesítési folyamatok időigényét,
egyszerűsítse a munkatársak mindennapi tevékenységeit,
valamint pontos és naprakész információkat biztosítson a készletekről és az értékesítésekről.

![Kép az alkalmazás elképzelt működési folyamatáról](./img/workflow_model.png)

*A rendszer működésének folyamatábrája*

2. Zsolti
### Projektterv

**Csapattagok és közös felelősség körök**

A négy fejlesztő egységes csapatként dolgozik, így mindenki részt vesz a backend, 
frontend, tesztelés és dokumentáció feladataiban is.

A munka megosztás dinamikusan, az aktuális projektigények szerint történik.

**Fő feladatkörök:**

- **Backend fejlesztés:** adatbázis, API-k, üzleti logika megvalósítása.
- **Frontend fejlesztés:** reszponzív Angular alapú felhasználói felület kialakítása.
- **Tesztelés:** egység- és funkcionális tesztek készítése, hibajavítás.
- **Dokumentáció:** követelmény- és rendszerterv, tesztterv, végső projektleírás elkészítése.

| Funkció / Story            | Feladat / Task                            | Prioritás | Becslés | Aktuális becslés | Eltelt idő | Hátralévő idő |
|----------------------------|-------------------------------------------|-----------|---------|------------------|------------|---------------|
| Követelményspecifikáció    | Dokumentum elkészítése                    | 0         | 10      | 10               | 10         | 0             |
| Funkcionális specifikáció  | Funkciók és folyamatok leírása            | 0         | 10      | 10               | 10         | 0             |
| Rendszerterv               | Architektúra és adatmodell kidolgozása    | 0         | 14      | 14               | 8          | 6             |
| Adatmodell                 | Adatbázis struktúra megtervezése          | 1         | 6       | 6                | 4          | 2             |
| Backend alapfunkciók       | API fejlesztés és üzleti logika           | 2         | 12      | 12               | 2          | 10            |
| Frontend alapok            | HTML/CSS, UI tervezés                     | 2         | 10      | 10               | 3          | 7             |
| Login funkció              | Bejelentkezés és jogosultságkezelés       | 2         | 8       | 8                | 0          | 8             |
| Termékkezelés              | Termékek megjelenítése, keresés, szűrés   | 2         | 10      | 10               | 0          | 10            |
| Kosár funkció              | Kosár logika és UI implementálása         | 2         | 10      | 10               | 0          | 10            |
| Riport funkció             | Napi/heti/havi riport készítése           | 1         | 8       | 8                | 0          | 8             |
| Tesztelés                  | Unit és funkcionális tesztek végrehajtása | 1         | 10      | 10               | 0          | 10            |

*Az Becslés/Aktuális becslés/Eltelt idő/Hátralévő idő oszlopok órában értendőek*

![Kép egy kördiagramról, amely százalékokat tartalmaz a hátralévő teendőkről](/img/pie_chart_of_todo_tasks.png)
*Kördiagram a hátralévő teendőkről*


3. Zoli
### Üzleti folyamatok modellje


![Kép az üzleti modellről, amely tartalmazza a felhasználok által használható funkciókat](/img/uzleti_modell.png)
*Üzleti modell*

4. Geri

# Követelmények

- Leírja nagyvonalakban, miket kell teljesítenie a programnak.  
- **Példa: Funkcionális követelmények:**

## Funkcionális követelmények

- Felhasználók regisztrációja és bejelentkezése email-cím és jelszó alapján.  
- Jogosultsági szintek kezelése (admin, értékesítő, partner).  
- Termékek listájának megjelenítése valós idejű készletadatokkal.  
- Készletfigyelés és automatikus riasztás alacsony készletszint esetén.  
- Termékek keresése név, ár, típus alapján.  
- Találatok szűrése kategóriák és árkategóriák szerint.  
- Kosár funkció: termékek hozzáadása, eltávolítása, végösszeg számítása.  
- Vásárlási folyamat támogatása számla előnézettel és kiállítással.  
- Számla sztornózása hibás tranzakció esetén.  
- Napi riport manuális indítása az eladásokról.  
- Heti és havi riportok automatikus generálása Excel formátumban.  
- Adminisztrátor által kezelt készletkezelés és felhasználó-hozzárendelés.  
- Partnercégek regisztrációja és jogosultsági kiosztása.  
- Rendszer naplózza a felhasználói és adminisztratív műveleteket.  

## Nem funkcionális követelmények

- A felhasználói felület legyen reszponzív és könnyen áttekinthető.  
- Nagy terhelés alatt is biztosítson stabil működést.  
- Keresési és szűrési műveletek maximum 2 másodpercen belül válaszoljanak.  .  
- A felület webes környezetben hibátlanul működjön.  
- A riportok letöltése szabványos formátumban (Excel) történjen.  
- Felhasználók nem férhetnek hozzá más felhasználók személyes adataihoz.  
- Adatbázis-tárolás titkosítással történjen.  
- Jelszavak biztonságos, egyirányúan kódolt formában legyenek tárolva.  
- Naplózott adatokhoz kizárólag adminisztrátor férhet hozzá.  

## Törvényi előírások, szabványok

- GDPR előírásoknak való megfelelés.  
- Adatbiztonsági szabványok (ISO/IEC 27001) követése.  
- Szoftverminőségi szabványok (ISO/IEC 25010) figyelembevétele.  
- Naplózás és adathozzáférés nyomonkövethetősége. 

5. Geri

# Funkcionális terv

## Rendszerszereplők:
- Adminisztrátor  
- Értékesítő  
- Partnercég  
- Vásárló  

## Rendszerhasználati esetek és lefutásaik:

### ADMINISZTRÁTOR:
● Teljes körű hozzáférése van a rendszerhez.    
● Jogosultsági szintek kezelése (admin, értékesítő, partner).  
● Termékek és készlet manuális bővítése, frissítése.  
● Partnercégek regisztrálása és készlet-hozzárendelés.  
● Számlák sztornózása és javítása.  
● Rendszernaplók és riportok ellenőrzése.  

### ÉRTÉKESÍTŐ:
● Bejelentkezés a rendszerbe email-címmel és jelszóval.  
● Termékek listázása és készletadatok megtekintése.  
● Termékek keresése és szűrése különféle paraméterek alapján.  
● Termékek kosárba helyezése, mennyiség módosítása, eltávolítás.  
● Vásárlás lebonyolítása és számla kiállítása.  
● Hibás számlák sztornózása.  
● Napi riport manuális indítása és letöltése.  

### PARTNERCÉG:
● Saját hozzáférés kezelése.  
● Hozzárendelt készletek megtekintése.  
● Termékek státuszának követése.  

### VÁSÁRLÓ:
● Termékek megtekintése és leírásaik olvasása.  
● Kosárba helyezés az értékesítő közreműködésével.  
● Vásárlás jóváhagyása és visszaigazolás fogadása.  

## Menü-hierarchiák:

● **BEJELENTKEZÉS**  
  - Bejelentkezés  
  - Regisztráció  
  - Segítség (Help)  

● **FŐMENÜ (Értékesítő számára)**  
  - Terméklista  
  - Keresés és szűrés  
  - Kosár megtekintése  
  - Vásárlás / számla kiállítás  
  - Riportok (Napi / Heti / Havi)  
  - Kijelentkezés  

● **ADMIN MENÜ**  
  - Felhasználókezelés  
  - Termék- és készletkezelés  
  - Partnercégek kezelése  
  - Számlák kezelése  
  - Rendszernaplók és biztonsági beállítások  

6. Zsolti
### Fizikai környezet

Az alkalmazás webes platformra készül, reszponzív kialakítással, így asztali számítógépeken és laptopokon is használható.
A rendszer nem igényel telepítést a felhasználó eszközére, mivel modern böngészőből érhető el (Chrome, Firefox, Edge, Safari).

A szerveroldali környezet a tervek szerint helyi (lokális) szerveren kerül kialakításra,
mivel ennek üzemeltetése jelentősen alacsonyabb költséggel jár,
így partnereink számára gazdaságosabb megoldást biztosít a rendszer hosszú távú fenntartására.

A rendszer teljes mértékben open source komponensekre épül, nem használ megvásárolt, zárt forráskódú szoftvert.

**Fejlesztésre használt eszközök:**

- Pycharm Professional - backend fejlesztése (Python Django keretrendszere)
- Visual Studio Code - fronted fejlesztése (HTML/CSS)
- Figma - felhasználói felület tervezése, képernyő tervezés
- Git és Github - verziókezelés és csapatmunka támogatása

7. Geri
(/img/abstract_domain_modell.png)







8. Marci









9. Zoli
### Adatbázis terv

![Kép az adatbázis kapcsolatokról, amely tartalmazza a mezőneveket és a típusokat](/img/database_relationships.png)
*Adatbázis terv*


10. Zoli
### Implementációs terv

A webes felület főként HTML, CSS és JavaScript nyelveken fog készülni. A HTML struktúrák, a CSS stíluslapok és a JavaScript kódok külön fájlokba kerülnek, hogy a rendszer átlátható, könnyen módosítható és bővíthető legyen. A frontend a backend felé REST API-n keresztül kommunikál, amely CRUD műveleteket biztosít az adatbázis kezelésére. Az oldalon a felhasználók képesek lesznek termékeket megtekinteni, kosárba helyezni és rendeléseket leadni, miközben a kosár tartalmát a kliens oldalon is nyilvántartjuk, így a felhasználó azonnal láthatja a változásokat.

A rendelési folyamat során a rendszer ellenőrzi a raktárkészletet és a felhasználói jogosultságokat. A felhasználói bejelentkezés és regisztráció biztonságos jelszókezeléssel történik, a jelszavak titkosított formában kerülnek tárolásra az adatbázisban. A backend Django keretrendszerre épül, és felelős az adatbázis lekérdezések és módosítások pontos végrehajtásáért. Az adatbázis MySQL alapú, normalizált és indexelt, a termékek, rendelések, számlák és riportok nyilvántartására.

A termékek és kategóriák listája dinamikusan jelenik meg a backend adatai alapján, míg a kosár interaktív kezelése JavaScript eseményekkel történik. A rendelés leadása előtt a backend ellenőrzi az adatok érvényességét, és a kosárban lévő mennyiségeket a szerverrel szinkronizálja. A rendelés leadása után a rendszer generálja a számlát PDF formátumban, amely letölthető és nyomtatható, továbbá lehetőség van sztornózásra, ami a rendelés státuszának módosításával történik.

A riportok menedzseri jogosultság szerint jelennek meg, és exportálhatók PDF vagy CSV formátumban. A riportok a backend aggregált adataira épülnek, és a frontend grafikonjai JavaScript (például Chart.js) segítségével jelennek meg. Az oldal reszponzív kialakítású, mobilon és asztali gépen egyaránt jól használható, a CSS biztosítja az egységes megjelenést, míg a HTML sablonok a Django Template Engine segítségével kerülnek összeállításra.

A felhasználói profil oldalon a személyes adatok szerkeszthetők, a backend pedig minden inputot validál a biztonság érdekében. A rendszer képes több felhasználó párhuzamos kezelésére, a tevékenységek naplózása biztosítja az auditálhatóságot és a hibakeresést. A REST API végpontjai dokumentáltak és verziózottak, a frontend és backend közötti kommunikáció pedig biztonságos HTTPS-en keresztül történik.

A kosár funkció lehetővé teszi a mennyiségek módosítását és termékek eltávolítását, a rendelés leadása után pedig visszaigazolást kap a felhasználó. Az admin felület biztosítja a termékek, felhasználók, rendelések és számlák kezelését, míg az oldal hibakezelése kiterjed a formák érvényesítésére és a backend válaszaira is. A weboldal teljes funkcionalitása tesztelve lesz a fejlesztés minden szakaszában, a kód dokumentált, és a rendszer könnyen karbantartható és bővíthető. Összességében a projekt célja egy átlátható, biztonságos, reszponzív és jól karbantartható értékesítési rendszer létrehozása, amely támogatja a felhasználói műveleteket, a rendeléseket, a számlázást és a riportok generálását.


11. Zsolti
### Tesztterv

A tesztelés célja, hogy a rendszer és a komponensi megfelelően működjenek, hibamenetesen szolgálják ki a felhasználók igényit, 
és megfeleljenek a funkcionális és követelmény specifikációban leírtaknak. A tesztelés során vizsgáljuk a rendszer stabilitását, 
teljesítményét, valamint a különböző böngészőkben való kompatibilitását.
A tesztelés célja továbbá a hibák feltárása és mielőbbi kijavítása, hogy az éles indulás és üzemeltetés zökkenőmentes legyen.

1. Egységtesztelés

A fejlesztés során minden implementált metódushoz "Unit" tesztet, azaz egységtesztet kell írni. 
Célja, hogy ellenőrízzük az egyes modulok és funkciók helyes működését már a fejlesztési fázisban.
- A kódlefedettség tekintetében célunk a magas arány elérése, azonban ez nem mehet a tesztek minőségének rovására.
  - 80%-90% százalékos lefedettség általában elégséges.
- A metódusok akkor tekinthetők késznek, ha a hozzájuk tartozó tesztesetek hibamentesen futnak le.
- A tesztelendő fő modulok:
  - Bejelentkezési és jogosultségkezelési logika.
  - Készletkezeléshez (termék hozzáadása, törlése, módosítása) tartozó CRUD műveletek.
  - Kosár funkció (termék hozzáadás és eltávolítása).
  - Riport generálás.

2. Alfa teszt

Az alfa tesztelés célja a rendszer funkcióinak ellenőrzése a fejlesztők és tesztelők által, belső tesztkörnyezetben.
A tesztkörnyezet ezáltal kontrollálható és konfigurálható így ideális teret ad az éles működés rekreálására.
- Vizsgáladó:
  - Böngészők közötti kompatibilitás.
  - Alapfunkciók stabilitása.

3. Béta teszt

A béta tesztelés során a tesztkörnyezet kevésbé korlátozott, azáltal, hogy ez nem tesztelők végzik.
Így jobban replikálható az éles átadás.
Az esetlegesen fellépő problémákról a tesztelésre jogosult felhasználók értesítik a fejleszők és rendszerüzemeltetők csapatát, 
amely csapat az elvárt működést próbálják elérni.

### Tesztelendő funkciók

- Backend funkciók:
  - Adatbázis kezelés:
    - adatok rögzítése, módosítása és törlése hibamentesen működjön.
  - Riport generálás:
    - napi, heti és havi riportok pontos adatokat mutassanak.
  - Raktár funkció:
    - készletnövelés működjön minden partnercég esetén.
- Frontend funkciók:
  - Bejelentkezési folyamat:
    - Helyes adatok esetén sikeres bejelentkezés.
    - Hibás adatok esetén hibaüzenet jelenjen meg.
  - Felhasználói élmény: minden böngészőben reszponzívan jelenjen meg.
  - Keresés és szűrés:
    - Termékek keresése cikkszám alapján.
    - Szűrés kategória, ár és márka alapján.
    - Eredmények frissítése valós időben.
  - Kosár funkció:
    - Termékek hozzáadása és eltávolítása.
    - Kosár végösszegének automatikus frissítése.
    - Kosár tartalmának mentése kijelentkezés után.
  - Riportok:
    - Napi riport manuális készítése.
    - Heti és havi riportok automatikus generálása.



12. ### Telepitési terv

Webes elérés és kliensoldali követelmények - A szoftver webes felületének használatához nincs szükség külön telepítendő 
alkalmazásra. A felhasználók számára elegendő egy modern, ajánlott böngésző telepítése (pl. Google Chrome, Mozilla Firefox, 
Opera vagy Safari). Az alkalmazás platformfüggetlen, és közvetlenül elérhető az interneten keresztül, így a kliensek a 
webszerverhez böngészőn keresztül csatlakoznak, további konfiguráció nélkül.


13. ### Karbantartási terv

A webáruház karbantartása rendszeres és tervezett feladatokat igényel annak érdekében, hogy a 
rendszer biztonságosan, gyorsan és megbízhatóan működjön. A karbantartási terv az alábbi területekre terjed ki:

- **Technikai karbantartás**: Rendszeres frissítések a szerver operációs rendszerére, 
a webkiszolgálóra, a backend technológiákra (pl. PHP, Node.js), valamint a használt keretrendszer 
komponenseire. A bővítmények és modulok frissítése szintén fontos a kompatibilitás és biztonság érdekében. 
Az adatbázis optimalizálása, indexek karbantartása. A biztonsági mentések rendszeres tesztelése.


- **Biztonsági karbantartás**: A webáruház SSL tanúsítványának érvényességét rendszeres ellenőrzése.
Kétlépcsős azonosítás időnkénti tesztelése.


- **Tartalomkarbantartás**: A termékadatok, árak, készletinformációk és leírások frissítése. 
Elavult vagy kifutott termékeket archiválása, törölése.
A kategóriák és szűrők újrastrukturálása ha szükséges.


- **Teljesítmény és monitoring**: A weboldal sebességét rendszeres tesztelése, PageSpeed vagy GTmetrix segítségével. 
A mobil kompatibilitás ellenőrzése.
A hibaoldalakat (404, 500) naplózása, javítása.


- **Tesztelés és minőségbiztosítás**: A vásárlási folyamatot rendszeres tesztelése, beleértve a kosár működését, 
a fizetési folyamatot.
A regisztrációs és belépési folyamatok időnkénti ellenőrzése.


- **Kommunikáció és dokumentáció**: 
A hibák és javítások dokumentálása belső naplóban vagy wiki rendszerben. 
A változások listáját (changelog) célszerű vezetése.