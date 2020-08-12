Getting Started with Gauge
==========================

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, use `mvn test`
/*Kullanıcı başarılı giriş kontrol edilmeli
------------


Kredi Kartı ile Alışveriş Yapma
-----------
Tags: KrediKartı

* "n11kullanicisi@gmail.com" emaili ve "n11sifre" sifresi ile giris yap
* Sepetime tıkla
* Sepeti boşalt
* Anasayfaya tıkla
* "Bilgisayar" ürününü bul
* Ürünü sepete ekle
* Sepetime tıkla
* Satın alma butonuna tıkla
* Ön Bilgilendirme Sözleşmesini kabul et
* Kart bilgilerini doldur
* Çıkış Yap


Kategori Tab kontrol
-----------
Tags: Sağ Yan Kategori Kontrol

* "n11kullanicisi@gmail.com" emaili ve "n11sifre" sifresi ile giris yap
* Kategori sekmesini kontrol et
* Çıkış Yap


Çok Satanlar Kontrol
------------
Tags: Çok Satan Kategori

* "n11kullanicisi@gmail.com" emaili ve "n11sifre" sifresi ile giris yap
* "3" saniye bekle
* Çok Satanlar sekmesini kontrol et
* Çıkış Yap