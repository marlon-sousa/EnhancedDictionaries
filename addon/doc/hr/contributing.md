# Doprinos

## Izrada dodatka

Trebat će vam:

* Python 3.13 ili noviji.
*Konfigurirani pip
* Scons (pip install scons)
* Markdown (pip install markdown)
* gettext, koji pruža alate `msgfmt` i `xgettext`. `msgfmt` kompilira datoteke prijevoda pri svakoj izradi, a `xgettext` koristi `scons pot` za generiranje predloška prijevoda. Na sustavu Windows instalirajte modernu verziju s [gettext-iconv-windows](https://github.com/mlocati/gettext-iconv-windows/releases) (ili upotrijebite `scoop install gettext` / `choco install gettext`) i provjerite da se njegov `bin` direktorij nalazi ispred bilo kojeg drugog gettexta u vašem PATH-u. Nemojte koristiti GnuWin32 gettext paket: zamrznut je na verziji 0.14.4 (2005) i prestar je za ovu izradu (`scons pot` ne uspijeva zbog nepodržane opcije `--package-name`).

Nakon što sve instalirate, izdavanje scons-a u korijenu projekta trebalo bi izgraditi dodatak i generirati dokumente.

### Pre-commit

Snažno se preporučuje da instalirate pre-commit.

* pip install pre-commit
* pre-commit install

Ovo instalira pre-commit i konfigurira njegove hookove, tako da će se prilikom svakog commita primijeniti nekoliko provjera. Ako bilo koja od njih ne uspije, commit neće biti dopušten.

Provjere pre-commita možete pokrenuti u bilo kojem trenutku bez izvršavanja commita naredbom "pre-commit run --all-files".

### Flake8

Jedan od pre-commit hookova je Flake8, Python linter koji, između ostalog, pomaže osigurati da projekt ima dosljedno oblikovanje i da su na snazi dobre prakse.

Flake8 hook pre-commita koristi istu konfiguraciju iz `flake8.ini`.

## Prijevodi

### Prevođenje dodatka

Pod pretpostavkom da imate sve postavljeno za izgradnju dodatka (pogledajte prethodnu temu), izdavanje scons pot bi trebalo generirati pot datoteku u korijenskom direktoriju projekta. Moguće je generirati i doprinijeti .po datotekama za vaš jezik.
Trenutni jezici se mogu pronaći u: /addon/locale direktoriju

### Prevođenje dokumentacije

Prijevodi dokumentacije generiraju se iz .tpl.md (ne iz .md) datoteka. Zbog toga, osim iz ove datoteke (read.md) u korijenu projekta, nećete pronaći druge .md datoteke.

Datoteke .tpl.md normalne su datoteke za označavanje s jednim dodatkom: ako koristite ${[var]} unutar teksta, [var] će biti zamijenjena varijablom s istim imenom definiranim u buildvars.py kada se odgovarajući md i .html datoteke kreiraju.

Ako ne postoji varijabla s tim imenom, zamjena se ne vrši.

Ovo je korisno, na primjer, za generiranje poveznica i naslova s ​​uključenom verzijom dodatka bez potrebe za ponovnim pisanjem dokumentacije.

Da biste preveli dokumentaciju, zgrabite datoteku readme.tpl.md u korijenu projekta i prevedite je. Prevedena datoteka mora imati naziv readme.tpl.md i mora biti smještena unutar addon/doc/[lang] direktorija.

Varijable ${[xxx]} moraju ostati netaknute. Za generiranje dokumenata, generirat će se ikone problema i markdown i HTML.