# Katkıda Bulunan

## Eklentiyi oluşturma

İhtiyacınız olacak:

* Python 3.6 veya üzeri.
* pip yapılandırılmalıdır
* scons (pip kurulumu scons)
* markdown (pip kurulumu markdown)
* msgfmt yardımcı programı. Bunu elde etmenin en kolay yolu, git bash'i kurmak ve komut istemine bash araçlarını dahil etmeyi seçmektir.

Her şeyi yükledikten sonra, projenin kökünde scons yayınlamak, eklentiyi oluşturmalı ve dokümanlar oluşturmalıdır.

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
