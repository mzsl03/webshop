# SZFM - Webshop projekt

Egy Django alapú webshop alkalmazás, amelyet a **Szoftverfejlesztési módszertanok** kurzus keretében készítettünk.  
A projekt célja egy webáruház működésének szimulálása, felhasználókezeléssel, termékkezeléssel és számlázási funkciókkal.

---

## Felhasznált technológiák és könyvtárak
- [Django](https://www.djangoproject.com/) - Python web keretrendszer
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL adatbázis driver
- [Pillow](https://pypi.org/project/Pillow/) - Képkezelés
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel fájlok kezelése
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Környezeti változók kezelése

---

## Telepítés és futtatás

### 1. GitHub tároló klónozása

```
git clone https://github.com/mzsl03/webshop.git
```

### 2. Virtuális környezet létrehozása

- **Conda** 

```
conda create --name <tetszőleges-virtuális-környezet-neve> python=3.12
conda activate <tetszőleges-virtuális-környezet-neve>
```

Szükséges technológiák beszerzése:

```
pip install -r requirements.txt
```

- **Pip**

```
python -m venv .venv
Windows (PowerShell/CMD): .venv\Scripts\activate /
 Linux és Mac: .venv\Scripts\activate
```

A pip frissítése:

```
python.exe -m pip install --upgrade pip
```

Szükséges technológiák beszerzése:

```
pip install -r requirements.txt
```

### 3. .env fájl elérése

- Az adatbázis szerver biztonságát biztosítja az, hogy a forráskód nem tartalmazza a eléréséhez szükséges hitelesítési adatokat.
  (például: **jelszó, host**) Szükséges tehát ennek megszerzéséhez a csapatunk tagjaihoz fordulni. Köszönjük a megértést, és a türelmet!

- Létrehozni a projekt gyökér csomagjában kell `.env` néven, az alábbi struktúrával:
```
DB_NAME=*****
DB_USER=*****
DB_PASSWORD="*****"
DB_HOST=*****
DB_PORT=*****
```

