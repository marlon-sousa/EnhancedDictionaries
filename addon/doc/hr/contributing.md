# Doprinos

## Izrada dodatka

Trebat će vam:

* Python 3.6 ili noviji.
*Konfigurirani pip
* Scons (pip install scons)
* Markdown (pip install markdown)
* Msgfmt uslužni program. Najlakši način da ga dobijete je instaliranjem Git Basha i odabirom uključivanja Bash alata u naredbenom retku.

Nakon što sve instalirate, izdavanje scons-a u korijenu projekta trebalo bi izgraditi dodatak i generirati dokumente.

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