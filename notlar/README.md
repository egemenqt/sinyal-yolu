# Sinyal Yolu — Günlük Not Defteri

16 haftalık günlük uygulama planının git ile takip edilen hali. Her gün bir dosya; oturumu bitirince dosyayı doldur, commit at, aşağıda kutuyu işaretle.

## Nasıl kullanılır
1. O günün dosyasını aç: `notlar/hafta-NN/gun-D.md`
2. Oturumu yap, dosyayı doldur.
3. Commit: `git add notlar/hafta-NN/gun-D.md && git commit -m "hafta-NN gun-D: <özet>"`
4. Aşağıdaki checklist'te kutuyu işaretle ve bu dosyayı da commit'le.

## İlerleme

### Hafta 01 · Sinyaller ve Sistemlere Giriş (Faz 01)
- [ ] Gün 1 — Sürekli/ayrık sinyal, LTI sistem kavramları — okuma + repo Hafta 1 not defterini incele. ([notlar/hafta-01/gun-1.md](notlar/hafta-01/gun-1.md))
- [ ] Gün 2 — NumPy/Matplotlib ile sinyal üretme, repo not defterini adım adım çalıştır. ([notlar/hafta-01/gun-2.md](notlar/hafta-01/gun-2.md))
- [ ] Gün 3 — Örnekleme teoremi + aliasing demo (kendi kodun); osiloskop + fonksiyon jeneratörüyle fiziksel doğrulama. ([notlar/hafta-01/gun-3.md](notlar/hafta-01/gun-3.md))
- [ ] Gün 4 — Osiloskop gözlemini kaydet, README'ye ekle, git commit, haftayı 2 cümlede özetle. ([notlar/hafta-01/gun-4.md](notlar/hafta-01/gun-4.md))

### Hafta 02 · Örnekleme, Nicemleme ve Matematik Temeli (Faz 01)
- [ ] Gün 1 — Lineer cebir hızlı tekrar: vektör/matris işlemleri (Strang, ders 1-2). ([notlar/hafta-02/gun-1.md](notlar/hafta-02/gun-1.md))
- [ ] Gün 2 — Nicemleme (quantization) ve bit derinliği etkisi; repo Hafta 2 not defteri. ([notlar/hafta-02/gun-2.md](notlar/hafta-02/gun-2.md))
- [ ] Gün 3 — DAQ ile gerçek bir sensörden farklı örnekleme hızlarında veri topla, aliasing'i gerçek veride ara. ([notlar/hafta-02/gun-3.md](notlar/hafta-02/gun-3.md))
- [ ] Gün 4 — Bulguları not al, commit, haftayı özetle. ([notlar/hafta-02/gun-4.md](notlar/hafta-02/gun-4.md))

### Hafta 03 · Fourier Serisi ve DFT (Faz 01)
- [ ] Gün 1 — Fourier serisi teorisi — periyodik sinyali sinüzoidlere ayırma sezgisi. ([notlar/hafta-03/gun-1.md](notlar/hafta-03/gun-1.md))
- [ ] Gün 2 — DFT matematiği + repo Hafta 3 not defteri. ([notlar/hafta-03/gun-2.md](notlar/hafta-03/gun-2.md))
- [ ] Gün 3 — Kendi sensör/mikrofon kaydına DFT uygula, frekans içeriğini yorumla. ([notlar/hafta-03/gun-3.md](notlar/hafta-03/gun-3.md))
- [ ] Gün 4 — Sonuçları belgele, commit. ([notlar/hafta-03/gun-4.md](notlar/hafta-03/gun-4.md))

### Hafta 04 · FIR/IIR Filtreleri — Faz 01 kapanışı (Faz 01)
- [ ] Gün 1 — FIR vs IIR farkları, frekans tepkisi teorisi. ([notlar/hafta-04/gun-1.md](notlar/hafta-04/gun-1.md))
- [ ] Gün 2 — scipy.signal ile filtre tasarımı; repo Hafta 4 not defteri. ([notlar/hafta-04/gun-2.md](notlar/hafta-04/gun-2.md))
- [ ] Gün 3 — Faz 01 çıktı projesi: gürültülü sinyal + filtre + önce/sonra karşılaştırma, gerçek DAQ verisiyle. ([notlar/hafta-04/gun-3.md](notlar/hafta-04/gun-3.md))
- [ ] Gün 4 — GitHub'a push, README finalize, ekibe/yöneticiye 15 dk demo. ([notlar/hafta-04/gun-4.md](notlar/hafta-04/gun-4.md))

### Hafta 05 · FFT ve STFT (Faz 02)
- [ ] Gün 1 — DFT'den FFT'ye — algoritma sezgisi ve hesaplama karmaşıklığı. ([notlar/hafta-05/gun-1.md](notlar/hafta-05/gun-1.md))
- [ ] Gün 2 — STFT ve zaman-frekans çözünürlük ödünleşimi; repo Hafta 5 not defteri. ([notlar/hafta-05/gun-2.md](notlar/hafta-05/gun-2.md))
- [ ] Gün 3 — Kendi ses/sensör kaydına FFT/STFT uygula, sonuçları görselleştir. ([notlar/hafta-05/gun-3.md](notlar/hafta-05/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-05/gun-4.md](notlar/hafta-05/gun-4.md))

### Hafta 06 · Spektrogramlar (Faz 02)
- [ ] Gün 1 — Spektrogram okuma/yorumlama teorisi. ([notlar/hafta-06/gun-1.md](notlar/hafta-06/gun-1.md))
- [ ] Gün 2 — Repo Hafta 6 not defteri — kod ile spektrogram üretme. ([notlar/hafta-06/gun-2.md](notlar/hafta-06/gun-2.md))
- [ ] Gün 3 — Atölyedeki mikrofon/sensörden kayıt al, gerçek olayların spektrogramını çıkar. ([notlar/hafta-06/gun-3.md](notlar/hafta-06/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-06/gun-4.md](notlar/hafta-06/gun-4.md))

### Hafta 07 · Ses ve Konuşma İşleme (Faz 02)
- [ ] Gün 1 — Ses işleme temelleri: örnekleme hızı, pencereleme. ([notlar/hafta-07/gun-1.md](notlar/hafta-07/gun-1.md))
- [ ] Gün 2 — Repo Hafta 7 not defteri — konuşma işleme örneği. ([notlar/hafta-07/gun-2.md](notlar/hafta-07/gun-2.md))
- [ ] Gün 3 — Kendi ses kaydınla basit bir özellik çıkarımı (ör. MFCC) denemesi. ([notlar/hafta-07/gun-3.md](notlar/hafta-07/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-07/gun-4.md](notlar/hafta-07/gun-4.md))

### Hafta 08 · Ses Gürültü Giderme — Faz 02 kapanışı (Faz 02)
- [ ] Gün 1 — Gürültü giderme yöntemleri (spektral çıkarma vb.) teorisi. ([notlar/hafta-08/gun-1.md](notlar/hafta-08/gun-1.md))
- [ ] Gün 2 — Repo Hafta 8 not defteri. ([notlar/hafta-08/gun-2.md](notlar/hafta-08/gun-2.md))
- [ ] Gün 3 — Faz 02 çıktı projesi: gerçek DAQ/sensör verisinde gürültü tespiti + filtreleme + özellik çıkarımı pipeline'ı (Portföy 01-02). ([notlar/hafta-08/gun-3.md](notlar/hafta-08/gun-3.md))
- [ ] Gün 4 — GitHub push, ekip demo; aylık dış geri bildirim döngüsünü işlet. ([notlar/hafta-08/gun-4.md](notlar/hafta-08/gun-4.md))

### Hafta 09 · Biyomedikal Sinyaller (ECG/EEG) (Faz 02-03)
- [ ] Gün 1 — ECG/EEG sinyal özellikleri teorisi. ([notlar/hafta-09/gun-1.md](notlar/hafta-09/gun-1.md))
- [ ] Gün 2 — Repo Hafta 9 not defteri; biyomedikal sensör yoksa PhysioNet'ten açık veri seti indir. ([notlar/hafta-09/gun-2.md](notlar/hafta-09/gun-2.md))
- [ ] Gün 3 — ECG sinyalinde R-peak tespiti gibi basit bir analiz uygula. ([notlar/hafta-09/gun-3.md](notlar/hafta-09/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-09/gun-4.md](notlar/hafta-09/gun-4.md))

### Hafta 10 · ML ve Biyomedikal Uygulamalar (Faz 02-03)
- [ ] Gün 1 — Klasik ML sınıflandırma teorisi tazeleme (scikit-learn). ([notlar/hafta-10/gun-1.md](notlar/hafta-10/gun-1.md))
- [ ] Gün 2 — Repo Hafta 10 not defteri — biyomedikal veriyle sınıflandırma. ([notlar/hafta-10/gun-2.md](notlar/hafta-10/gun-2.md))
- [ ] Gün 3 — Kendi ECG/EEG analizine basit bir sınıflandırıcı ekle (ör. normal/anormal ayrımı). ([notlar/hafta-10/gun-3.md](notlar/hafta-10/gun-3.md))
- [ ] Gün 4 — Belgele, commit; Faz 02→03 geçiş özeti yaz. ([notlar/hafta-10/gun-4.md](notlar/hafta-10/gun-4.md))

### Hafta 11 · Radar Sinyal İşleme (Faz 03)
- [ ] Gün 1 — Radar temelleri: menzil, Doppler kayması teorisi. ([notlar/hafta-11/gun-1.md](notlar/hafta-11/gun-1.md))
- [ ] Gün 2 — Repo Hafta 11 not defteri. ([notlar/hafta-11/gun-2.md](notlar/hafta-11/gun-2.md))
- [ ] Gün 3 — SDR ile basit bir radar-benzeri deney, ya da açık veri setiyle radar sinyali analizi. ([notlar/hafta-11/gun-3.md](notlar/hafta-11/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-11/gun-4.md](notlar/hafta-11/gun-4.md))

### Hafta 12 · Modülasyon ve Demodülasyon (Faz 03)
- [ ] Gün 1 — AM/FM/dijital modülasyon teorisi. ([notlar/hafta-12/gun-1.md](notlar/hafta-12/gun-1.md))
- [ ] Gün 2 — Repo Hafta 12 not defteri. ([notlar/hafta-12/gun-2.md](notlar/hafta-12/gun-2.md))
- [ ] Gün 3 — SDR ile gerçek bir sinyali yakala, demodüle etmeyi dene. ([notlar/hafta-12/gun-3.md](notlar/hafta-12/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-12/gun-4.md](notlar/hafta-12/gun-4.md))

### Hafta 13 · IoT Sensör Akışları (Faz 03)
- [ ] Gün 1 — Streaming veri mimarisi: buffer, queue, gerçek zamanlı kısıtlar teorisi. ([notlar/hafta-13/gun-1.md](notlar/hafta-13/gun-1.md))
- [ ] Gün 2 — Repo Hafta 13 not defteri. ([notlar/hafta-13/gun-2.md](notlar/hafta-13/gun-2.md))
- [ ] Gün 3 — SDR/DAQ'tan canlı veri akışını Python streaming pipeline'ına bağla (Portföy 04 başlangıcı). ([notlar/hafta-13/gun-3.md](notlar/hafta-13/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-13/gun-4.md](notlar/hafta-13/gun-4.md))

### Hafta 14 · Gömülü DSP (Faz 03)
- [ ] Gün 1 — Gömülü sistemlerde DSP kısıtları: bellek, güç, gecikme teorisi. ([notlar/hafta-14/gun-1.md](notlar/hafta-14/gun-1.md))
- [ ] Gün 2 — Repo Hafta 14 not defteri; C++ ile basit bir filtre implementasyonu. ([notlar/hafta-14/gun-2.md](notlar/hafta-14/gun-2.md))
- [ ] Gün 3 — Algoritmayı gömülü/edge karta (Jetson/RPi) taşı, çalıştır (Portföy 05). ([notlar/hafta-14/gun-3.md](notlar/hafta-14/gun-3.md))
- [ ] Gün 4 — Belgele, commit, ekibe kısa ara demo. ([notlar/hafta-14/gun-4.md](notlar/hafta-14/gun-4.md))

### Hafta 15 · Finansal Zaman Serileri ve Kalman Filtreleri (Faz 03)
- [ ] Gün 1 — Kalman filtresi matematiği: durum-uzay modeli, tahmin-güncelleme döngüsü. ([notlar/hafta-15/gun-1.md](notlar/hafta-15/gun-1.md))
- [ ] Gün 2 — Repo Hafta 15 not defteri + Labbe'nin kitabından paralel okuma. ([notlar/hafta-15/gun-2.md](notlar/hafta-15/gun-2.md))
- [ ] Gün 3 — Kalman filtresini gerçek DAQ/sensör verisiyle bir takip görevine uygula (Portföy 03). ([notlar/hafta-15/gun-3.md](notlar/hafta-15/gun-3.md))
- [ ] Gün 4 — Belgele, commit. ([notlar/hafta-15/gun-4.md](notlar/hafta-15/gun-4.md))

### Hafta 16 · Dalgacıklar, ICA ve ML — Faz 03 kapanışı (Faz 03)
- [ ] Gün 1 — Dalgacık dönüşümü ve ICA (bağımsız bileşen analizi) teorisi. ([notlar/hafta-16/gun-1.md](notlar/hafta-16/gun-1.md))
- [ ] Gün 2 — Repo Hafta 16 not defteri. ([notlar/hafta-16/gun-2.md](notlar/hafta-16/gun-2.md))
- [ ] Gün 3 — Faz 03 kapanış taslağı: filtre + özellik + takip + streaming parçalarını tek pipeline'da birleştir (Portföy 06'nın temeli). ([notlar/hafta-16/gun-3.md](notlar/hafta-16/gun-3.md))
- [ ] Gün 4 — 16 hafta kapanışı: kapsamlı GitHub push, teknik dokümanı güncelle, ekibe/yöneticiye büyük demo; Faz 04'ü gözden geçir. ([notlar/hafta-16/gun-4.md](notlar/hafta-16/gun-4.md))
