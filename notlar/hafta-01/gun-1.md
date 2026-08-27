# Hafta 01 · Gün 1 — Sinyaller ve Sistemlere Giriş

**Faz:** Faz 01
**Bugünkü hedef:** Sürekli/ayrık sinyal, LTI sistem kavramları — okuma + repo Hafta 1 not defterini incele.
**Planlanan süre:** 1.5 sa
**Tarih:** 19–27 Ağustos 2026

## Yapılanlar
- Neso Academy "Signals and Systems" playlist, ilk 4 video: Introduction to Signals, Classification of Signals, Systems, LTI Systems
- MIT OCW 6.003 reading (Bölüm 1: Signals and Systems) okundu
- El defterine sinyal sınıflandırma ve LTI notları alındı (bkz. Fotoğraflar)
- Python ortamı kuruldu: `venv` + numpy, scipy, matplotlib, jupyter
- `aliasing_demo.py` yazıldı ve çalıştırıldı — 20 Hz ve 6 Hz örnekleme hızlarında aliasing karşılaştırması

## Fotoğraflar
<!-- el defteri sayfalarını gorseller/ klasörüne at, ![açıklama](gorseller/dosya.jpg) şeklinde ekle -->
![gün 1 - sayfa 1](gorseller/gun-1-01.jpg)
![gün 1 - sayfa 2](gorseller/gun-1-02.jpg)
![gün 1 - sayfa 3](gorseller/gun-1-03.jpg)
![gün 1 - sayfa 4](gorseller/gun-1-04.jpg)

## Öğrenilenler
- Sinyal, birim zamanda tekrar eden bir niceliktir.
- Periyot, bir tam tur için geçen süredir.
- Sürekli zamanlı sinyaller kesilmeden devam eden sinyallerdir; ayrık zamanlı sinyaller süreklilerden örnek alınarak elde edilir ve birim (n) olarak belirtilir.
- Sinyaller tek değişkenli veya çok değişkenli olabilir.
- Pratik: `day_1.py` (sinyal + periyot noktalarının işaretlenmesi), `day1_addition.py` (iki parçalı-sabit sinyalin toplamı ve çarpımı, el defterindeki sonuçla karşılaştırıldı).

## Sorunlar / takıldığım yerler
- Yok.

## Sonraki adım
- Hafta 2: Örnekleme, nicemleme ve lineer cebir temeline geç.

**Commit:** `git commit -m "hafta01-gun1: <özet>"`
