1. TODO - Zoli/Zsolti - Áttekintés
A rendszer funkcionális felépítése az értékesítési folyamat támogatására épül. Az alkalmazás egyik főbb modulja a bejelentkezés és jogosultságkezelés, mivel az értékesítők csak azonosítás után tudnak a rendszerhez hozzáférni. A jogosultságok határozzák meg, hogy ki milyen funciót érhet el.
Az értékesítő látja az elérhető termékeket és ezzel együtt az aktuális készletet. A rendszer figyelmeztet alacsony készletszint esetén, és lehetőséget ad a készlet bővítésére egy fiktív raktárból.
A felhasználó keresőmező és szűrők segítségével gyorsan megtalálhatja a termékeket vagy számlákat (pl.: cikkszám, ár, típus szerint)
A kiválasztott termékek kosárba helyezhetők, majd az ügyfél döntését követően megkezdődhet a rendelés véglegesítése. A rendszer előnézetet biztosít a számla ellenőrzéséhez.
A rendszer számlát állít ki a vásárlásról. Probléma esetén az értékesítő sztorhózhatja a számlát, amely automatikusan megváltoztatja a termék státuszát.
A rendszer napi, heti és havi riportokat generál az eladásokból. A heti és havi riportok automatikus készülnek el Excel formátumban, támogatva a készlet és a bevétel ellenőrzését.


2. TODO - Zoli/Zsolti - Jelenlegi helyzet

Partnercégeink egyre nagyobb mértékben támaszkodnak digitális értékesítési csatornákra, ezért mindennapi munkájukhoz elengedhetetlenné vált egy korszerű, gyors és megbízható rendszer használata. A jelenleg működő megoldás azonban már nem képes megfelelni ezeknek az elvárásoknak. A felület bonyolult és nehezen áttekinthető, emiatt az értékesítők számára a termékek böngészése és a szükséges adatok elérése sok időt vesz igénybe.
A terhelhetőség hiányosságai miatt a rendszer lassulásokkal, időszakos fennakadásokkal működik, ami közvetlenül hátráltatja az értékesítési folyamatokat és negatívan hat az ügyfélélményre is. Különösen problémás a napi zárás folyamata: az értékesítőknek manuálisan kell összegyűjteniük az eladások és visszavételezések adatait, ami időigényes és hibalehetőségekkel terhelt.
Mindezek következtében a meglévő rendszer nemcsak a hatékony munkavégzést akadályozza, hanem hosszabb távon versenyhátrányt is okozhat partnereink számára. Az új alkalmazás bevezetésével cél, hogy egy reszponzív, jól strukturált és felhasználóbarát felület álljon rendelkezésre, amely egyszerűsíti az értékesítési folyamatokat, támogatja a mindennapi adminisztrációt, valamint biztosítja a gyors és pontos riportálást.



3. TODO - Geri
| Modul         | Név                       | Kifejtés 
| Jogosultság   | Bejelentkezés             | A felhasználó email-cím és jelszó segítségével léphet be a rendszerbe; hibás adatok esetén hibaüzenetet kap. 
| Jogosultság   | Regisztráció              | Új felhasználók számára regisztrációs lehetőség, jelszó biztonságos (kódolt) tárolásával és adatok validálásával. 
| Jogosultság   | Jogosultsági szintek      | Többszintű jogosultság (admin, értékesítő, partner, vásárló), eltérő hozzáférési és kezelési lehetőségekkel. 
| Felhasználói  | Terméklista               | Bejelentkezést követően a rendszer megjeleníti az adott üzlet aktuális készletét, frissített állapotban. 
| Felhasználói  | Készletjelzés             | Alacsony készletszámnál automatikus figyelmeztetés, valamint fiktív raktárból történő bővítési lehetőség. 
| Felhasználói  | Keresés                   | Számlaszám, terméknév, ár, típus vagy egyéb paraméter alapján történő keresés. 
| Felhasználói  | Szűrés                    | A találatok szűrése különféle tulajdonságok szerint (pl. kategória, árkategória, gyártó). 
| Felhasználói  | Kosár funkció             | A felhasználó kosárba helyezheti a kiválasztott termékeket, megtekintheti a végösszeget és a tételek listáját. 
| Felhasználói  | Vásárlás támogatása       | A rendszer biztosítja a gördülékeny vásárlási folyamatot, a tételek véglegesítését és a tranzakciók biztonságát. 
| Riport        | Napi riport               | Manuálisan indítható riport az adott napon eladott termékekről. 
| Riport        | Heti/Havi riport          | Automatikusan generált riportok Excel formátumban, időzítő segítségével, a periódust követően. 
| Riport        | Riport tartalom           | A riportok tartalmazzák az eladott termékek listáját, a készletmozgásokat és a bevételi adatokat. 
| Adminisztráció| Készletkezelés            | Az adminisztrátor jogosult a készletek manuális bővítésére, frissítésére, szinkronizálására. 
| Adminisztráció| Felhasználókezelés        | Új eladók és adminok hozzáadása, üzletekhez rendelése, jogosultsági szintek meghatározása. 
| Adminisztráció| Partner hozzáférés        | Partnercégek regisztrációja, hozzáférési szintek kiosztása, készlet-hozzárendelés az üzletekhez. 
| Adminisztráció| Számlák kezelése          | Számlák sztornózása, javítása, valamint egyedi számlaszám alapján történő visszakeresése. 
| Rendszer      | Stabil működés            | A felület reszponzív és gyors, nagy terhelés alatt is stabil működést biztosít. 
| Rendszer      | Naplózás                  | A rendszer naplózza a felhasználói műveleteket, a készletváltozásokat és a riportok generálását. 
| Rendszer      | Biztonság                 | Adatkezelés a GDPR előírásai szerint, kódolt adatbázis-tárolás és biztonságos jelszókezelés. 
| Rendszer      | Szabványoknak megfelelés  | A fejlesztésnek és működésnek igazodnia kell az ISO/IEC 27001, ISO/IEC 25010 szabványokhoz. 

4. TODO - Marci
   ### Jelenlegi üzleti folyamatok modellje
   1. Termékkezelés
   A termékeket manuálisan töltjük fel a webáruház admin felületén.
   Minden termékhez megadjuk a nevet, leírást, árat, képet és műszaki specifikációkat.
   A termékeket kategóriákba soroljuk, szükség esetén módosítjuk vagy töröljük.
   A készletet egy adatbázis táblázatban vezetjük, később integrációval bővítjük.
   2. Szűrés, keresés
   A látogatók kategóriák szerint böngészhetnek.
   Egyszerű kulcsszavas keresés áll rendelkezésre.
   A termékek szűrése ár, típus vagy márka alapján történik.
   3. Kosár és rendelés
   Az eladó kosárba helyezheti a kiválasztott termékeket.
   A kosárban módosíthatják a mennyiséget, eltávolíthatnak termékeket.
   A rendszer kiszámítja az összesített árat.
   4. Felhasználók
   Az admin regisztrálja az eladókat.
   Az eladók később bejelentkezhetnek.
   A fiókjukban nyomon követhetik rendeléseiket.
   5. Adminisztráció
   A rendelések nyilvántartása Excelben történik.
   A készletet manuálisan frissítjük.
   Bevétel és kiadás nyomon követése alap szinten történik.


5. TODO - Marci
    ### Igényelt üzleti folyamatok modellje
⦁	Termékfeltöltés - a webáruházba A rendszernek lehetővé kell tennie új termékek gyors és strukturált feltöltését az adminisztrációs felületen keresztül.
⦁   Termékadatok begyűjtése (név, leírás, ár, kép, specifikációk)- A termékekhez tartozó alapvető információk feltöltése, a vásárlók részletes tájékoztatása érdekében.
⦁	Kategorizálás, módosítása, törlése - A termékek besorolása kategóriákba segíti a kereshetőséget.
⦁	Készletkezelés integráció - A webáruház kapcsolódjon a raktárkészlethez, információt nyújtson a termékek elérhetőségéről.
⦁	Kulcsszavas keresés, szűrés kategóriák szerint - A felhasználók számára biztosítani kell egy hatékony kereső- és szűrőrendszert, hogy gyorsan megtalálják a kívánt termékeket.
⦁	Termékek hozzáadása/eltávolítása, árösszesítés - A kosár funkcióval az eladó hozzáadhatja vagy eltávolíthatja a termékeket, miközben a rendszer automatikusan kiszámítja a végösszeget.
⦁	Kosárba helyezés - A kiválasztott terméket a felhasználó egy kattintással a kosárba helyezheti, ahol később módosíthatja a mennyiséget.
⦁	Megrendelés leadása - A vásárló a kosár tartalmát megerősítve elindíthatja a rendelési folyamatot.
⦁	Rendelés visszaigazolása - A sikeres tranzakció után a vásárló automatikus visszaigazolást kap a rendelés részleteiről.
⦁	Regisztráció, bejelentkezés, rendeléskövetés - A felhasználók saját fiókot hozhatnak létre, ahol nyomon követhetik korábbi és aktuális rendeléseiket.
⦁	Termékek, rendelések, felhasználók kezelése - Az adminisztrációs felületen keresztül az üzemeltetők kezelhetik a terméklistát, a rendeléseket és a vásárlói adatokat.
⦁	Készletfigyelés - Az adminisztrátorok valós időben követhetik a készletmozgásokat, és időben reagálhatnak a hiányokra.
⦁	Bevétel-kiadás kimutatás - A webáruház pénzügyi teljesítményéről való részletes kimutatása.


6. TODO - Zsolti
 ### Használati esetek

Az Adminisztrátor felelős a rendszer problémamentes működéséért és a felhasználók kezeléséért.
Jogosultsága a teljes rendszerre kiterjed, így minden funkciót elér.
Feladatai többek között a következők:
- Bejelentkezés a rendszerbe email-cím és jelszó segítségével.
- Felhasználókezelés:
  - Hozzáférés a felhasználók listájához, ahol módosíthatja azok adatait (név, email, jelszó).
  - Új értékesítők hozzáadása a rendszerhez.
  - Felhasználók törlése a rendszerből.
- Partner hozzáférés kezelése:
  - Készletek hozzárendelése a partnercégekhez és üzletekhez.
- Globális felügyelet:
  - Rendszerbeállítások és biztonsági funkciók kezelése.
  - A riportkészítés folyamatának ellenőrzése.

Az Értékesítő a rendszer mindennapi felhasználója, aki a termékek értékesítéséért, számlák kezeléséért és riportok készítéséért felel.
Feladatai és jogosultságai a következők:
- Bejelentkezés a rendszerbe email-cím és jelszó megadásával.
- Termékek megtekintése:
  - A bejelentkezést követően megjelenik az adott üzlet aktuális készlete.
  - A készlet automatikusan frissített, így mindig pontos adatokat mutat.
- Keresés és szűrés:
  - Termékek vagy számlák keresése számlaszám, terméknév, cikkszám, ár vagy típus alapján.
  - A találatok szűrése kategória, árkategória vagy gyártó szerint.
- Kosár funkció:
  - A kiválasztott termékek kosárba helyezése.
  - A kosár tartalmának megtekintése, módosítása és a végösszeg azonnali megjelenítése.
- Vásárlás lebonyolítása:
  - A vásárló döntése után a számla elkészítése, és vásárlás véglegesítése.
- Számla sztornózása:
  - Hibás vagy érvénytelen számla esetén annak érvénytelenítése (sztornózás).
- Készletjelzés és bővítés:
  - A rendszer figyelmezteti az értékesítőt, ha a készletszint alacsony.
  - Lehetősége van fiktív raktárból bővíteni a készletet.
- Riportok készítése:
  - Napi riport manuális indítása a nap végén, amely összesíti az eladásokat és bevételeket.
  - A riport Excel formátumban letölthető.
  - Az Értékesítő célja, hogy gyorsan és pontosan kiszolgálja az ügyfeleket, miközben folyamatosan követi a készlet alakulását és adminisztrálja az értékesítési folyamatokat.

Említésre méltó ezen túl, hogy a vásárló maga az eladási folyamat egy pontján sem kap hozzáférést a funkciók kezeléséhez.
A termékleírás megtekintésén túl nincsen más privilégiuma az üzletbe betérő fogyasztónak.




7. TODO - Zsolti









8. TODO - Zoli - Forgatókönyv

- Cél: Az értékesítő sikeresen elad egy terméket, kiállítja a számlát, majd a nap végén riportot készít az eladásokról

- Szereplők:
    - Értékesítő
    - Rendszer

- Lépések:
    1. Az értékesítő bejelentkezik a rendszerbe
    2. A főoldalon megjelennek az aktuálisan elérhető termékek
    3. Az értékesítő kereséssel vagy szűréssel kiválasztja a megfelelő terméket
    4. A termékre kattintva a rendszer megjeleníti a hozzá tartozó specifikációkat, amelyeket az értékesítő az ügyfélnek bemutathat
    5. A kiválasztott termék(ek)et az értékesítő a kosárba helyezi
    6. Az ügyfél dönt a vásárlásról, majd az értékesítő kitölti a számlához szükséges adatokat
    7. A rendszer nyomtatási előnézete biztosít az adatok ellenőrzéséhez
    8. Ha minden rendben, megtörténik a fizetés és a számla kiállítása
    9. Ha a termékkel probléma merül fel, az értékesítő sztornózhatja a számlát, a rendszer ekkor automatikusan módosítja a termék státuszát
    10. A nap végén az értékesítő napi riportot generál, amely összesíti az eladott termékeket és a bevételeket

9. TODO - Zsolti

| Funkció (Név)      | Modul          | Kapcsolódó követelmény(ek)                                                                                                            |
|--------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bejelentkezés      | Jogosultság    | A rendszernek biztosítania kell, hogy csak azonosított felhasználók férjenek hozzá a funkciókhoz.                                     |
| Készletjelzés      | Jogosultság    | A rendszernek jeleznie kell az alacsony készletszintet, és lehetőséget kell biztosítania a fiktív raktárból történő készletbővítésre. |
| Terméklista        | Felhasználói   | A rendszernek meg kell jelenítenie az aktuálisan elérhető termékek listáját az adott üzlet készlete alapján.                          |
| Keresés és szűrés  | Felhasználói   | A rendszernek lehetőséget kell biztosítania termékek keresésére és szűrésére számlaszám, ár, típus és egyéb tulajdonságok szerint.    |
| Kosár funkció      | Felhasználói   | Az értékesítőnek lehetőséget kell biztosítani a kiválasztott termékek kosárba helyezésére és a végösszeg azonnali megjelenítésére.    |
| Készletkezelés     | Felhasználói   | Az értékesítőnek lehetőséget kell biztosítani a készletek frissítésére, bővítésére és az üzletek közti szinkronizálására.             |
| Napi riport        | Riport         | A rendszernek lehetőséget kell biztosítania az értékesítő számára napi riport készítésére az eladott termékekről.                     |
| Heti/Havi riport   | Riport         | A rendszernek automatikusan kell generálnia heti és havi riportokat Excel formátumban, időzítő segítségével.                          |
| Felhasználókezelés | Adminisztráció | Az adminisztrátornak kezelnie kell az eladókat és üzletekhez rendeléseiket.                                                           |
| Partner hozzáférés | Adminisztráció | A partnercégek hozzáférést kell kapjanak a rendszerhez, és az értékesítőknek az adott üzlet készletei alapján kell dolgozniuk.        |
| Stabil működés     | Rendszer       | A rendszernek reszponzívnak kell lennie, és biztosítania kell a gördülékeny működést az értékesítési folyamat során.                  |

10. TODO - Zsolti

| Fogalomtár     |                                                                                                                                     |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------|
| Értékesítő     | A rendszer felhasználója, aki termékeket értékesít, rendelések állapotát képes figyeli, számlákat kezel és napi riportokat készít.  |
| Adminisztrátor | Jogosult felhasználó, aki kezeli az eladókat, hozzárendeli őket az üzletekhez és felügyeli a rendszer működését.                    |
| Sztornózás     | Már kiállított számla érvénytelenítése a rendszerben                                                                                |
| Riport         | Összesítő dokumentum, amely tartalmazza az adott időszakban (nap, hét, hónap) eladott termékek adatait és a bevételt.               |
| Szűrés         | A termékek listájának leszűkítése ár, típus vagy egyéb paraméterek alapján a gyorsabb keresés érdekében.                            |
| Keresési mező  | Olyan funkció, amely lehetővé teszi, hogy a számlák egyedi azonosító (számlaszám) alapján gyorsan megkereshetők legyenek.           |
| Kosár          | Az eladó által kezelt gyűjtőfunkció, amely tartalmazza a vásárló által kiválasztott tételeket és azok végösszegét.                  |