# FuzzyLogicUygulaması(IOT)

## Sıcaklık Sensörü ve Röle kullanılarak Fuzzy Logic(Bulanık mantık) uygulaması(IOT)

Bu sistemde bir karar sistemi uygulamak için bulanık bir mantık geliştirdim.

Bu uygulamada 2 adet DHT22 sensörü ile alınan sıcaklık ve nem değerlerini alıyoruz.

Sıcaklık için soğuk,ılık ve sıcak kararları var.Nemde ise düşük  ve yüksek olmak üzere 2 kararımız var.

Aldığımız bu karar durumlarını değerlendirerek bir klima veya kombiye iletebiliriz.

### 1) İlk olarak kütüphaneleri indirip,tanımladım.

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/1.ad%C4%B1m.jpg)

Kullandığım kütüphaneler:

Numpy:Numpy kütüphanesi, bilimsel hesaplama  işlemleri kolaylaştırmak için yazılmış olan bir python kütüphanesidir.

Bir makine öğrenmesi,görüntü işleme ve yapay zeka konularında çalışma yaparken sıkça hesaplama işlemleri yapılmaktadır.

Hesaplama işlemleri ve dönüşüm işlemlerinde sıkça kullanılan kod yapısı numpy kütüphanesi ile basit bir seviyede ve az kod yazacak şekilde tasarlanmıştır.

Matematiksel işlemleri çok hızlı yapmasından dolayı sıkça kullanılan bir kütüphanedir.

Çok boyutlu diziler (array), çeşitli türetilmiş nesneler(maskelenmiş diziler ve matrisler gibi) ve bir sürü matematiksel , mantıksal, şekil manipülasyonu, sıralama, seçme, ayrık Fourier de dahil olmak üzere diziler üzerinde hızlı işlemler yapmamızı sağlayan Python kütüphanesidir.

Matplotlib:Matplotlib; 2 boyutlu grafikler hazırlamamızı sağlayan bir Python kütüphanesidir.Tanımı böyle olmasına rağmen 3 boyutlu görselleştirme de yapılabiliyor.

plt.subplots(); bu metod ise bize bir Figure nesnesi ve istediğimiz kadar Axes nesnesi döndürür. 

matplotlib.pyplot, matplotlib'in MATLAB gibi çalışmasını sağlayan komut tarzı işlevler topluluğudur. Her pyplot işlevi bir şekil üzerinde bir miktar değişiklik yapar: örneğin, bir şekil oluşturur, bir şekildeki bir çizim alanını oluşturur, bir çizim alanında bazı çizgiler çizer, arsaları etiketlerle süsler vb.

Matplotlib.pyplot'ta fonksiyon çağrıları boyunca çeşitli durumlar korunur, böylece mevcut şekil ve çizim alanı gibi şeyleri takip eder ve çizim fonksiyonları mevcut eksenlere yönlendirilir.

### 2) Uygulamada ilk adımın ardından röle ve DHT22’nin pinlerinin atamalarını yaptım.

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/2.ad%C4%B1m.jpg)

### 3) Sonraki kısımda giriş ve çıkışları belirleyip,bunları "temperature_category()" ve "humidity_category()" içerisinde tanımlayıp üyelik oluşturdum.

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/3.ad%C4%B1m.jpg)

### 4) Ardından üyeliğimizi referans olarak yazdırıyoruz.Bunun için Matplotlib kütüphanesini kullandım.

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/4.ad%C4%B1m.jpg)

### 5) Şimdi DHT22 modülü ile sıcaklık ve nem okumaya hazırız. Sonra onları bulanık mantık sistemimiz üzerinde hesaplıyoruz.

##### * Ayrıca, girdilerimizle belirsiz çıkarımlar yapıyoruz. Çıktıyı oluşturmak için bulanık kümeleme yapıyoruz. Çıktılar sayısal bir biçimdir. Bunu düşük, ortalama ve çok rahat olarak haritalayabiliriz.
 
Bu durumdan,  hava hakkında karar verebiliriz. Soğuk ise bir makineyi açıp açmamak için karar verdiriyoruz.

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/5.ad%C4%B1m.jpg)

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/6.ad%C4%B1m.jpg)

### 6) Sonuç:

![alt text](https://github.com/fatihawk/FuzzyLogicUygulamasi-IOT-/blob/master/Sonu%C3%A7.jpg)
















