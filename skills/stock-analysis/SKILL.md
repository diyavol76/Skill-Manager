---
name: stock-analysis
description: >
  Herhangi bir hisse senedi için kapsamlı, görsel yatırım analizi HTML raporu üretir. Türkçe olarak hazırlanır. WebSearch ile halka açık finansal veriler (gelir dağılımı, segment karlılığı, büyüme trendi, analist beklentileri, değerleme, riskler) toplanır; sonuç olarak Chart.js grafikleri, KPI kartları ve karşılaştırma tablolarından oluşan tek dosyalık, tarayıcıda açılabilir bir HTML rapor oluşturulur.

  Tetikleyiciler: "hisse analizi", "analiz et", "stock analysis", "equity research", "yatırım raporu", "[TICKER] analizi", "earnings analizi", "hisse senedi raporu", "[şirket adı] hakkında rapor"
---

# Stock Analysis Skill

Belirtilen hisse için Türkçe kapsamlı yatırım analizi HTML raporu üret.

## Workflow (sırayla uygula)

1. **Veri Toplama** — 8 hedefli WebSearch sorgusu (aşağıya bak)
2. **Rapor Üretimi** — Toplanan verilerle HTML raporu oluştur (`references/html-template.md`)
3. **Kaydetme** — `//outputs/Investing/` klasörüne `{TICKER}_Analiz_{YIL}.html` adıyla kaydet
4. **Paylaşma** — `computer://` linki ver

---

## 1. Veri Toplama — WebSearch Sorguları

**ÖNEMLİ:** WebSearch tool'u bu skill için zorunludur. Eğer WebSearch kullanılamıyorsa, kullanıcıya "WebSearch aracına bu oturumda erişilemiyor, lütfen yeni bir konuşma başlatıp tekrar deneyin" mesajını ver ve dur.

Aşağıdaki 5 sorguyu sırayla çalıştır (her sorgudan sonra sonuçları işle, sonrakine geç). `{TICKER}` ve `{COMPANY}` yerine gerçek değerleri koy.

```
1. "{TICKER} {COMPANY} annual revenue quarterly earnings results 2024 2025 site:investors.{domain}.com OR site:prnewswire.com OR site:stockanalysis.com"
2. "{TICKER} {COMPANY} segment revenue breakdown geographic split gross margin operating margin 2024 2025"
3. "{TICKER} {COMPANY} 2026 guidance full year revenue EPS analyst estimates consensus forecast"
4. "{TICKER} {COMPANY} valuation PE ratio EV EBITDA competitors peers comparison 2025 2026"
5. "{TICKER} {COMPANY} risks opportunities growth catalysts investment thesis 2025"
```

Toplanan verileri aşağıdaki kategorilere eşle:
- **Gelir:** Yıllık ve çeyreklik revenue (en az 2 yıl)
- **Marjlar:** Brüt kâr, faaliyet kârı, net marj, EPS (en az 4 çeyrek)
- **Segmentler:** Ürün/hizmet ve coğrafi gelir dağılımı (%)
- **Rehber:** Şirket guidance + analist konsensüs tahminleri
- **Değerleme:** P/E, EV/EBITDA, rakip karşılaştırması
- **Risk/Fırsat:** 3'er madde

Bir sorgu başarısız olursa, sorguyu daha kısa hale getirip tekrar dene. İkinci denemede de başarısız olursa o veriyi atla ve "Veri mevcut değil" yaz.

---

## 2. HTML Rapor Yapısı

HTML raporun 8 bölümü ve 10 grafiği olmalı. Detaylı şablon için bkz. `references/html-template.md`.

**Bölümler:**
1. Şirket Profili & KPI Özeti (8 KPI kartı)
2. Gelir Analizi (yıllık bar + çeyreklik bar)
3. Karlılık & Marjlar (marj line chart + EPS line chart)
4. Segment Analizi (coğrafi donut + ürün donut + progress bar'lar)
5. Büyüme Trendi & Backlog (backlog bar + siparişler bar)
6. Beklentiler & Yaklaşan Dönem (analist konsensüs tablosu)
7. Değerleme & Rakip Karşılaştırması (peer comparison table + P/E horizontal bar)
8. Risk & Fırsat (thesis kutusu + bear/bull kutuları)

**Teknik gereksinimler:**
- Chart.js 4.4.0 CDN: `https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js`
- Tek dosya (inline CSS + JS), harici CSS/font yok
- `lang="tr"`, UTF-8 encoding
- CSS değişkenleri: `--navy`, `--accent`, `--green`, `--red` (bkz. template)
- Responsive grid, disclaimer banner, section numbering

---

## 3. Veri Eksikliği Durumunda

- Çeyrek verisi yoksa yıllık toplamdan çıkart (FY − bilinen çeyrekler = tahmin)
- Segment % verileri bulunamazsa "Veri mevcut değil" yaz, grafikleri çizme
- Backlog verisi yoksa bu grafiği atla
- Her zaman disclaimer banner ekle: "Bu rapor yatırım tavsiyesi değildir."