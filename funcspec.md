1. TODO - Zoli/Zsolti








2. TODO - Zoli/Zsolti









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

4. TODO - Marciű









5. TODO - Marci









6. TODO - Marci








7. TODO - Zsolti









8. TODO - Zsolti









9. TODO - Zoli




10. TODO - Zsolti

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


11. TODO - Zsolti

| Fogalomtár     |                                                                                                                                     |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------|
| Értékesítő     | A rendszer felhasználója, aki termékeket értékesít, rendelések állapotát képes figyeli, számlákat kezel és napi riportokat készít.  |
| Adminisztrátor | Jogosult felhasználó, aki kezeli az eladókat, hozzárendeli őket az üzletekhez és felügyeli a rendszer működését.                    |
| Sztornózás     | Már kiállított számla érvénytelenítése a rendszerben                                                                                |
| Riport         | Összesítő dokumentum, amely tartalmazza az adott időszakban (nap, hét, hónap) eladott termékek adatait és a bevételt.               |
| Szűrés         | A termékek listájának leszűkítése ár, típus vagy egyéb paraméterek alapján a gyorsabb keresés érdekében.                            |
| Keresési mező  | Olyan funkció, amely lehetővé teszi, hogy a számlák egyedi azonosító (számlaszám) alapján gyorsan megkereshetők legyenek.           |
| Kosár          | Az eladó által kezelt gyűjtőfunkció, amely tartalmazza a vásárló által kiválasztott tételeket és azok végösszegét.                  |