# Poboljšani rječnici ${addon_version}
NVDA dodatak za rukovanje naprednijom obradom rječnika

## Preuzimanje
Preuzmite [Poboljšani rječnik ${addon_version} dodatak](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Značajke

### Rječnici specifični za profil
Način na koji NVDA primjenjuje uvjetne postavke, kao što je formatiranje dokumenta i druge, je kroz korištenje profila.

Profili su skupine postavki koje se zajedno mogu uvjetno primijeniti na čitač zaslona.

Na primjer, možete stvoriti profil za aplikacije kodiranja, u kojem je razina interpunkcije postavljena na sve, najava uvlačenja postavljena je na tonove, a brzina govora postavljena je na nižu razinu, tako da možete čitati kod na bolji način. Možete, zatim, povezati ovaj profil s Visual Studiom, Eclipseom, Notepad++-om i Visual Studio Codeom, tako da kada bilo koja od ovih aplikacija postane aktivna, te će se konfiguracije automatski primijeniti.

Kada, na primjer, prebacite tipku Alt Tab na druge aplikacije ili kada zatvorite jednu od tih aplikacija i sletite na radnu površinu, odvija se zadana konfiguracija. Tada je moguće jednostavno skočiti s vaše aplikacije za kodiranje na preglednik i, bez pritiskanja bilo koje tipke, čitati bez interpunkcijskih znakova u pregledniku i primijeniti svoju specifičnu konfiguraciju kada se vratite u okruženje koda.

NVDA rječnici su moćni, nude sjajne značajke kao što je zamjena regularnih izraza. Međutim, trenutno ne postoji način za prilaganje rječnika profilima na NVDA.

To znači da ako postavite zamjenu u zadanom rječniku, ona će se primijeniti u svim slučajevima, čak i u aplikacijama ili situacijama u kojima biste željeli da nisu.

Ovaj dodatak implementira kontekst profila prilikom obrade i stvaranja/uređivanja rječnika.

#### Kako radi?

Jednostavno instalirajte dodatak. Kada je aktivan:

* Rječnicima se sada ispravno rukuje uzimajući u obzir aktivni profil.
* Ako za trenutni profil postoje rječnici (zadani ili specifični za glas), oni se koriste.
* Ako ne postoje, koriste se rječnici za zadani profil. Ovo je u skladu s načinom na koji se NVDA ponaša, u smislu da kada kreiram novi profil, konfiguracije koje ne mijenjam na ovom novom profilu preuzimaju se iz zadanog.

Slično, ako ne postavim rječnik za profil, koristi se zadani rječnik.

* Glasovni rječnici ponašaju se na potpuno isti način: ako postoji rječnik specifičan za glas za aktivni profil, on se koristi. Inače se koristi rječnik za taj glas iz zadanog profila (ako postoji).
* Dijaloški okvir rječnika, kada se otvori, u naslovu uvijek pokazuje na koji se profil taj rječnik odnosi.
* Aktivni profil će odrediti koji će rječnik biti otvoren za uređivanje kada su aktivirani zadani ili glasovni izbornici rječnika.

Ovo je u skladu s načinom na koji se NVDA ponaša, jer ako netko ode u postavke i promijeni postavku, to će biti spremljeno na aktivnom profilu.

    Slično tome, otvoreni rječnik će pripadati tom profilu.

* Ako određeni rječnik ne postoji na aktivnom profilu, a dijaloški okvir rječnika je otvoren, novi rječnik za taj profil bit će kreiran.

    Neće prikazivati ​​unose jer je nov. Međutim, neće biti spremljen sve dok korisnik ne zatvori taj dijaloški okvir klikom na "U redu".

Ako to učini, novi će rječnik biti učinkovit. Ako poništi dijaloški okvir, i dalje će se koristiti zadani rječnik profila i ne sprema se rječnik specifičan za profil.

* Kada se stvori novi rječnik specifičan za profil, on postaje učinkovit i, stoga, uzorci na zadanom rječniku više nisu aktivni za taj profil.

    Ovo bi moglo biti željeno ponašanje, ali možda i ne. Možda korisnik želi koristiti sve uzorke iz zadanog rječnika plus nove uzorke koji su aktivni samo na ovom profilu.

* Kako bi se pokrila ova mogućnost, u dijaloškom okviru rječnika stvoren je novi gumb pod nazivom "Uvezi unose iz zadanog profila rječnika".

    Ovaj se gumb pojavljuje samo kada se uređuje rječnik specifičan za profil. Prilikom aktivacije ponaša se na sljedeći način:
    
- Čitaju se unosi iz zadanog rječnika (ili rječnika specifičnog za glas) iz zadanog profila.
    - Unosi koji se ne nalaze u rječniku koji se uređuje dodaju se u njega.
    - Ako se unos iz zadanog (ili glasovnog) rječnika pronađe u rječniku koji se uređuje, on neće prebrisati trenutni unos.
    - Uvoz ne sprema nove unose na disk. Samo dodaje uvezene unose na popis unosa u dijaloškom okviru rječnika. Fokus se stavlja na popis i korisnik zatim ima priliku pregledati novi popis unosa, kao da ih je sve ručno upisao.

* Kad god korisnik kreira rječnik na određenom profilu, on odmah stupa na snagu za taj profil.
* Kad god se profil promijeni, određeni rječnici (zadani i glasovni) odmah postaju aktivni. Ako ti rječnici ne postoje, koristi se zadani profil.
* To ne utječe na ugrađene i privremene rječnike, ne ovise o profilima, potonji jer je privremen, prvi jer je ugrađen.

# Doprinos i prevođenje

Ako želite doprinijeti ili prevesti ovaj dodatak, pristupite [repozitoriju projekta](https://github.com/marlon-sousa/EnhancedDictionaries) i pronađite upute na contributing.md u direktoriju dokumentacije na engleskom jeziku.

## Suradnici

Posebna zahvala za

* Ângelo Miguel Abrantes - portugalski prijevod
* Rémy Ruiz - francuski prijevod
* Rémy Ruiz - španjolski prijevod
* Thiago Seus - brazilski portugalski prijevod
* Umut KORKMAZ - turski prijevod
* Tarik Hadžirović - hrvatski prijevod
* Ivan Shtefuriak - ukrajinski prijevod