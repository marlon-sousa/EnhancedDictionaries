# Gelişmiş Sözlükler ${addon_version}
Daha gelişmiş sözlüklerin işlenmesi için Nvda eklentisi.

## indirme:
[Gelişmiş Sözlükler ${addon_version} eklentisini indirin](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Özellikler:

### Profile özel sözlükler:
NVDA'nın belge biçimlendirme ve diğerleri gibi koşullu ayarları uygulama yolu, profillerin kullanılmasıdır.  

Profiller, birlikte ekran okuyucuya koşullu olarak uygulanabilen ayar gruplarıdır.  

Örneğin, kodlama uygulamaları için, noktalama seviyesinin tümü, girinti duyurusunun tonların ve konuşma hızının daha yavaş bir seviyeye ayarlandığı bir profil oluşturabilir, böylece kodu daha iyi okuyabilirsiniz. Daha sonra bu profili visual studio, eclipse, notepad plus plus ve Visual Studio Code ile ilişkilendirebilirsiniz, böylece bu uygulamalardan herhangi biri aktif hale geldiğinde bu konfigürasyonlar otomatik olarak uygulanacaktır.  

Sekmeyi diğer uygulamalara değiştirdiğinizde veya bu uygulamalardan birini kapatıp masaüstüne indiğinizde, örneğin, varsayılan yapılandırma gerçekleşir. Böylece, kodlama uygulamanızdan bir tarayıcıya kolayca atlamak ve herhangi bir tuşa basmadan, tarayıcıda noktalama işaretleri olmadan okumak ve kod ortamınıza geri döndüğünüzde özel yapılandırmanızın uygulanmasını sağlamak mümkündür.  

NVDA sözlükleri güçlüdür ve düzenli ifade değiştirme gibi harika özellikler sunar. Ancak, şu anda NVDA'daki profillere sözlük eklemenin bir yolu yoktur.  

Bu, varsayılan sözlükte bir değiştirme ayarlarsanız, her durumda, hatta olmasını istemediğiniz uygulamalarda veya durumlarda bile uygulanacağı anlamına gelir.  

Bu eklenti, sözlükleri işlerken ve oluştururken / düzenlerken profil bağlamını uygular.  

#### Nasıl çalışır?

Eklentiyi kurmanız yeterlidir. Aktif olduğunda:  

* Sözlükler artık aktif profil dikkate alınarak doğru bir şekilde işleniyor.
* Geçerli profil için sözlükler (varsayılan veya sese özel) varsa, bunlar kullanılır.
* Mevcut değillerse, varsayılan profil için sözlükler kullanılır. Bu, yeni bir profil oluşturduğumuzda bu yeni profilde değiştirmediğimiz konfigürasyonların varsayılandan alınması anlamında NVDA'nın davranış biçimiyle tutarlıdır.

Benzer şekilde, bir profil için sözlük ayarlamazsak, varsayılan sözlük kullanılır.

* Ses sözlükleri tam olarak aynı şekilde davranır: etkin profil için sese özel bir sözlük varsa kullanılır. Aksi takdirde, varsayılan profildeki (varsa) o sesin sözlüğü kullanılır.
* Sözlük iletişim kutusu açıldığında, başlığında her zaman sözlüğün hangi profille ilgili olduğunu gösterir.
* Etkin profil, varsayılan veya sesli sözlük menüleri etkinleştirildiğinde hangi sözlüğün düzenlenmek üzere açılacağını belirleyecektir.

Bu, NVDA'nın davranış şekliyle tutarlıdır, çünkü biri ayarlara gider ve bir ayarı değiştirirse, bu aktif profile kaydedilecektir.  

Aynı şekilde açılan sözlük de o profile ait olacaktır.  

* Aktif bir profilde belirli bir sözlük yoksa ve sözlük iletişim kutusu açılırsa, o profil için yeni bir sözlük oluşturulur.

Yeni olduğu için giriş göstermeyecektir. Ancak, kullanıcı "tamam" düğmesine tıklayarak bu iletişim kutusunu kapatana kadar kaydedilmeyecektir.  

Eğer yaparlarsa, yeni sözlük etkili olacaktır. İletişim kutusunu iptal ederlerse, varsayılan profil sözlüğü kullanılmaya devam eder ve profile özel sözlük kaydedilmez.  

* Profile özel yeni bir sözlük oluşturulduğunda, etkin hale gelir ve bu nedenle, varsayılan sözlükteki kalıplar artık o profil için etkin değildir.

    Bu istenen davranış olabilir, ama belki de değil. Belki de kullanıcı, varsayılan sözlükteki tüm kalıpları ve yalnızca bu profilde etkin olan yeni kalıpları kullanmak istiyor.  

* Bu olasılığı kapatmak için, sözlük iletişim kutusunda "varsayılan sözlük profilinden girişleri içe aktar" adlı yeni bir düğme oluşturulur.

    Bu düğme yalnızca profile özel bir sözlük düzenlenirken görünür. etkinleştirildiğinde, aşağıdaki şekilde davranır:
    
    - Varsayılan profilden varsayılan sözlükten (veya sese özel sözlükten) girdiler okunur.
    - Düzenlenmekte olan sözlükte bulunmayan girdiler buna eklenir.
    - Düzenlenmekte olan sözlükte varsayılan (veya sesli) sözlükten bir girdi bulunursa, mevcut girdinin üzerine yazmaz.
    - İçe aktarma, yeni girdileri diske kaydetmez. Yalnızca içe aktarılan girdileri sözlük iletişim kutusundaki girdiler listesine ekler. Odak listeye yerleştirilir ve kullanıcı, sanki hepsini elle yazmış gibi yeni giriş listesini gözden geçirme fırsatına sahip olur.

*  Kullanıcı belirli bir profilde bir sözlük oluşturduğunda, o profil için hemen etkilidir.
* Bir profil değiştiğinde, belirli sözlükler (varsayılan ve ses) hemen etkinleşir. Bu sözlükler yoksa, varsayılan profil birininki kullanılır.
* Yerleşik ve geçici sözlükler etkilenmezler, profillere bağımlı değildirler, ikincisi geçici olduğu için, birincisi yerleşik olduğu için.

# Katkıda bulunma ve tercüme etme:

Bu eklentiye katkıda bulunmak veya bu eklentiyi çevirmek istiyorsanız, lütfen [proje deposuna](https://github.com/marlon-sousa/EnhancedDictionaries) erişin ve ingilizce dokümantasyon dizininde Contribute.md ile ilgili talimatları bulun.

## Katkıda Bulunanlar:

Özellikle ..... 'ya teşekkür

* Ângelo Miguel Abrantes - Portekizce çeviri
* Tarik Hadžirović - Hırvatça çeviri
* Rémy Ruiz - Fransızca çeviri
* Rémy Ruiz - İspanyolca çeviri
*  Thiago Seus - Brezilya Portekizcesi çeviri
* Umut KORKMAZ - Türkçe çeviri
* Ivan Shtefuriak - Ukraynaca çeviri