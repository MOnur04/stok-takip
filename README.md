# Stok Takip Uygulaması

Dükkan veya depolardaki ürünlerin stok durumunu takip etmek ve azalan ürünleri hızlıca görmek için yazdığım basit bir Python uygulaması.

## İş Takip Panosu
- Pano linki: https://github.com/users/MOnur04/projects/4

## Yapılanlar
- **Yeni ürün ekleme (#1):** Ürün adı, stok adedi ve kritik eşik bilgisini alıp `stoklar.json` dosyasına kaydediyor.
- **Kritik stokları listeleme (#2):** Stoğu belirlenen eşiğin altına düşen ürünleri ekranda uyarı olarak gösteriyor.

## Yapılacaklar
- Tüm ürünleri listeleme (#3)
- Stok miktarı güncelleme (#4)
- Ürün silme (#5)

## Nasıl Çalıştırılır?
Ekstra bir kütüphane kurmaya gerek yok, Python 3 ile doğrudan çalışır:

```bash
python stok_takip.py
```

## Nasıl Denenir?
1. Uygulamayı `python stok_takip.py` komutuyla başlattığınızda ana menü açılır.
2. **Yeni ürün ekleme (#1):** Menüden `1` yazıp Enter'a basın. Ürün adı, mevcut stok (örneğin `2`) ve kritik eşik (örneğin `5`) bilgilerini girin; ürünün `stoklar.json` dosyasına eklendiği bilgisini göreceksiniz.
3. **Kritik stokları listeleme (#2):** Menüden `2` yazıp Enter'a basın. Mevcut stoğu kritik eşiğin altında kalan ürünlerin uyarı listesinde görüntülendiğini görebilirsiniz.
4. Çıkmak için `0` tuşuna basabilirsiniz.
