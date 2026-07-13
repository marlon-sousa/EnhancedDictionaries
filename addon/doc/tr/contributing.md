# Katkıda Bulunan

## Eklentiyi oluşturma

İhtiyacınız olacak:

* Python 3.13 veya üzeri.
* pip yapılandırılmalıdır
* scons (pip kurulumu scons)
* markdown (pip kurulumu markdown)
* gettext; `msgfmt` ve `xgettext` araçlarını sağlar. `msgfmt` her derlemede çeviri dosyalarını derler ve `xgettext`, çeviri şablonunu oluşturmak için `scons pot` tarafından kullanılır. Windows'ta, [gettext-iconv-windows](https://github.com/mlocati/gettext-iconv-windows/releases) adresinden modern bir sürüm yükleyin (veya `scoop install gettext` / `choco install gettext` kullanın) ve `bin` dizininin PATH'inizde diğer gettext'lerden önce geldiğinden emin olun. GnuWin32 gettext paketini kullanmayın: 0.14.4 (2005) sürümünde donmuştur ve bu derleme için çok eskidir (`scons pot`, desteklenmeyen `--package-name` seçeneği nedeniyle başarısız olur).

Her şeyi yükledikten sonra, projenin kökünde scons yayınlamak, eklentiyi oluşturmalı ve dokümanlar oluşturmalıdır.

### Pre-commit

pre-commit'i yüklemeniz şiddetle önerilir.

* pip install pre-commit
* pre-commit install

Bu, pre-commit'i yükler ve kancalarını (hooks) yapılandırır; böylece her commit yaptığınızda birkaç denetim uygulanır. Bunlardan herhangi biri başarısız olursa commit'e izin verilmez.

"pre-commit run --all-files" komutunu çalıştırarak pre-commit denetimlerini commit yapmadan istediğiniz zaman çalıştırabilirsiniz.

### Flake8

pre-commit kancalarından biri, diğer şeylerin yanı sıra projenin tutarlı bir biçimlendirmeye sahip olmasını ve iyi uygulamaların yerinde olmasını sağlamaya yardımcı olan bir Python linter'ı olan Flake8'dir.

pre-commit Flake8 kancası, `flake8.ini` dosyasındaki aynı yapılandırmayı kullanır.

## çeviriler

### eklentiyi tercüme etmek

Eklentiyi oluşturmak için her şeye sahip olduğunuzu varsayarsak (önceki konuya bakın), scons pot yayınlayan kök proje dizininde bir pot dosyası oluşturmalıdır. Diliniz için .po dosyalarını oluşturmak ve katkıda bulunmak mümkündür.
Mevcut diller /addon/locale dizininde bulunabilir.

### belge tercümesi

Belge çevirileri .tpl.md (.md'den değil) dosyalarından oluşturulur. Bu nedenle, projenin kökündeki bu dosya (read.md) dışında başka .md dosyaları bulamazsınız.

.tpl.md dosyaları, bir ek içeren normal işaretleme dosyalarıdır: metninde ${[var]} kullanırsanız, [var], karşılık gelen md ve .html dosyaları oluşturulur.

Bu ada sahip bir değişken yoksa, değişim gerçekleşmez.

Bu, örneğin, belgeleri yeniden yazmak zorunda kalmadan dahil edilen eklenti sürümüyle bağlantılar ve başlıklar oluşturmak için kullanışlıdır.

Belgeleri çevirmek için projenin kökündeki benioku.tpl.md dosyasını alın ve çevirin. Çevrilen dosya readme.tpl.md olarak adlandırılmalı ve addon/doc/[lang] dizinine yerleştirilmelidir.

${[xxx]} değişkenlerinin dokunulmadan kalması gerekiyor. Dokümanları oluşturmak için, scons yayınlayın ve markdown ve HTML oluşturulacaktır.
