# HTML Rapor Şablonu

Bu dosya, `stock-analysis` skill'inin ürettiği HTML raporun tam şablonunu içerir.

## İçindekiler
1. [CSS Değişkenleri ve Temel Stiller](#css)
2. [Header Yapısı](#header)
3. [KPI Kartları](#kpi)
4. [Section Yapısı](#section)
5. [Grafik Örnekleri (Chart.js)](#charts)
6. [Tablo Şablonu](#table)
7. [Risk/Fırsat Kutuları](#risk)
8. [Tam HTML İskelet](#skeleton)

---

## CSS Değişkenleri ve Temel Stiller {#css}

```css
:root {
  --navy: #0a1628;
  --blue: #1a3a5c;
  --accent: #2563eb;
  --light-blue: #dbeafe;
  --green: #16a34a;
  --red: #dc2626;
  --orange: #ea580c;
  --gold: #d97706;
  --bg: #f8fafc;
  --card: #ffffff;
  --border: #e2e8f0;
  --text: #1e293b;
  --muted: #64748b;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; font-size: 14px; }

/* Layout */
.container { max-width: 1400px; margin: 0 auto; padding: 24px 32px; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.col-span-2 { grid-column: span 2; }
.col-span-3 { grid-column: span 3; }

/* Cards */
.card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }
.card-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--muted); margin-bottom: 16px; }
.chart-container { position: relative; height: 260px; }

/* Badges */
.badge { padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.badge-green { background: #166534; color: #bbf7d0; }
.badge-blue { background: #1e3a8a; color: #bfdbfe; }
.badge-orange { background: #92400e; color: #fed7aa; }
.badge-red { background: #7f1d1d; color: #fecaca; }

/* Sections */
.section { margin-bottom: 32px; }
.section-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 2px solid var(--border); }
.section-number { width: 36px; height: 36px; background: var(--accent); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px; flex-shrink: 0; }
.section-title { font-size: 20px; font-weight: 700; color: var(--navy); }

/* Tables */
.data-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.data-table th { background: var(--navy); color: white; padding: 10px 12px; text-align: left; font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
.data-table td { padding: 10px 12px; border-bottom: 1px solid var(--border); }
.data-table tr:nth-child(even) { background: #f8fafc; }
.data-table tr:hover { background: var(--light-blue); }
.beat { color: var(--green); font-weight: 700; }
.miss { color: var(--red); font-weight: 700; }
.inline { color: var(--gold); font-weight: 700; }

/* Progress bars (segment) */
.progress-container { margin-bottom: 12px; }
.progress-label { display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 13px; }
.progress-bar { height: 8px; background: var(--border); border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 4px; background: var(--accent); transition: width 0.3s; }

/* Thesis/Risk boxes */
.thesis-box { background: linear-gradient(135deg, #eff6ff, #dbeafe); border: 2px solid var(--accent); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
.bull-box { background: linear-gradient(135deg, #f0fdf4, #dcfce7); border: 2px solid var(--green); border-radius: 12px; padding: 20px; }
.bear-box { background: linear-gradient(135deg, #fff1f2, #ffe4e6); border: 2px solid var(--red); border-radius: 12px; padding: 20px; }
.risk-list { list-style: none; padding: 0; }
.risk-list li { padding: 8px 0; border-bottom: 1px solid rgba(0,0,0,0.05); padding-left: 20px; position: relative; }
.risk-list li:before { content: "▸"; position: absolute; left: 0; }

/* KPI tiles */
.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 32px; }
.kpi-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; border-top: 4px solid var(--accent); }
.kpi-card.green { border-top-color: var(--green); }
.kpi-card.red { border-top-color: var(--red); }
.kpi-card.gold { border-top-color: var(--gold); }
.kpi-card.orange { border-top-color: var(--orange); }
.kpi-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--muted); margin-bottom: 8px; }
.kpi-value { font-size: 24px; font-weight: 800; color: var(--navy); }
.kpi-sub { font-size: 12px; color: var(--muted); margin-top: 4px; }
.kpi-change { font-size: 13px; font-weight: 700; margin-top: 6px; }
.kpi-change.up { color: var(--green); }
.kpi-change.down { color: var(--red); }
```

---

## Header Yapısı {#header}

```html
<div class="header">
  <div class="header-meta">YATıRıM ANALİZİ • {TARİH}</div>
  <div class="header-title">{ŞİRKET ADI} ({TICKER})</div>
  <div class="header-sub">{SEKTÖR} | {BORSA}: {TICKER}</div>
  <div class="header-badges">
    <span class="badge badge-green">AL</span>  <!-- veya NÖTR / SAT -->
    <span class="badge badge-blue">Hedef: ${HEDEF_FİYAT}</span>
    <span class="badge badge-orange">{KATALİZÖR}</span>
  </div>
</div>
<div class="disclaimer-banner">
  ⚠️ Bu rapor yatırım tavsiyesi değildir. Bilgi amaçlıdır. Yatırım kararlarınızı kendi araştırmanıza dayandırınız.
</div>
```

---

## KPI Kartları {#kpi}

8 adet KPI kartı. Renk sınıfları: `(varsayılan mavi)`, `green`, `red`, `gold`, `orange`.

```html
<div class="kpi-grid">
  <div class="kpi-card green">
    <div class="kpi-label">2025 Geliri</div>
    <div class="kpi-value">$10.2B</div>
    <div class="kpi-sub">Yıllık</div>
    <div class="kpi-change up">▲ +19% YoY</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Brüt Marj</div>
    <div class="kpi-value">36.2%</div>
    <div class="kpi-sub">2025 FY</div>
    <div class="kpi-change up">▲ +210 bps</div>
  </div>
  <!-- 6 adet daha benzer kart: Faaliyet Marjı, EPS, P/E, Backlog, Temettü/buyback, Piyasa Değeri -->
</div>
```

---

## Grafik Örnekleri (Chart.js 4.4.0) {#charts}

### Bar Grafik (Yıllık Gelir)

```javascript
new Chart(document.getElementById('annualRevenueChart'), {
  type: 'bar',
  data: {
    labels: ['2021', '2022', '2023', '2024', '2025'],
    datasets: [{
      label: 'Gelir ($M)',
      data: [4900, 5700, 6900, 8200, 10200],
      backgroundColor: 'rgba(37,99,235,0.8)',
      borderColor: '#2563eb',
      borderWidth: 2,
      borderRadius: 6
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      y: { beginAtZero: false, ticks: { callback: v => '$' + (v/1000).toFixed(1) + 'B' } }
    }
  }
});
```

### Line Grafik (Marjlar)

```javascript
new Chart(document.getElementById('marginChart'), {
  type: 'line',
  data: {
    labels: ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
    datasets: [
      {
        label: 'Brüt Marj %',
        data: [34.1, 35.0, 36.2, 37.0, 35.8, 36.5, 37.1, 38.0],
        borderColor: '#2563eb', backgroundColor: 'rgba(37,99,235,0.1)',
        fill: true, tension: 0.4
      },
      {
        label: 'Faaliyet Marjı %',
        data: [11.2, 12.5, 13.8, 14.2, 13.0, 14.1, 15.0, 15.8],
        borderColor: '#16a34a', backgroundColor: 'rgba(22,163,74,0.1)',
        fill: true, tension: 0.4
      }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { position: 'top' } },
    scales: { y: { ticks: { callback: v => v + '%' } } }
  }
});
```

### Doughnut Grafik (Coğrafi Dağılım)

```javascript
new Chart(document.getElementById('geoChart'), {
  type: 'doughnut',
  data: {
    labels: ['Amerika', 'EMEA', 'Asya-Pasifik'],
    datasets: [{
      data: [58, 26, 16],
      backgroundColor: ['#2563eb', '#16a34a', '#ea580c'],
      borderWidth: 3, borderColor: '#fff'
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { position: 'right' },
      tooltip: { callbacks: { label: ctx => ctx.label + ': ' + ctx.parsed + '%' } }
    }
  }
});
```

### Yatay Bar Grafik (Rakip P/E Karşılaştırması)

```javascript
new Chart(document.getElementById('peChart'), {
  type: 'bar',
  data: {
    labels: ['{TICKER}', 'Rakip1', 'Rakip2', 'Rakip3'],
    datasets: [{
      label: 'Forward P/E',
      data: [32, 28, 35, 24],
      backgroundColor: ['#2563eb','#94a3b8','#94a3b8','#94a3b8'],
      borderRadius: 4
    }]
  },
  options: {
    indexAxis: 'y',
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } }
  }
});
```

---

## Tablo Şablonu {#table}

### Analist Beklentileri / Beat-Miss Tablosu

```html
<table class="data-table">
  <thead>
    <tr>
      <th>Dönem</th>
      <th>Beklenti (Gelir)</th>
      <th>Gerçekleşen</th>
      <th>Sapma</th>
      <th>EPS Beklenti</th>
      <th>EPS Gerçek</th>
      <th>Sonuç</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Q4 2025</td>
      <td>$2.85B</td>
      <td>$2.92B</td>
      <td class="beat">+2.5%</td>
      <td>$0.82</td>
      <td>$0.88</td>
      <td><span class="badge badge-green">BEAT</span></td>
    </tr>
    <!-- Diğer çeyrekler... -->
  </tbody>
</table>
```

### Peer Comparison Tablosu

```html
<table class="data-table">
  <thead>
    <tr><th>Şirket</th><th>Ticker</th><th>Piyasa Değeri</th><th>Gelir Büyümesi</th><th>Faaliyet Marjı</th><th>Forward P/E</th><th>EV/EBITDA</th></tr>
  </thead>
  <tbody>
    <tr style="background:#eff6ff;font-weight:700">
      <td>{ŞİRKET}</td><td>{TICKER}</td><td>$Xbn</td><td>X%</td><td>X%</td><td>Xx</td><td>Xx</td>
    </tr>
    <!-- Rakipler... -->
  </tbody>
</table>
```

---

## Risk/Fırsat Kutuları {#risk}

```html
<div class="thesis-box">
  <h3 style="margin-bottom:12px;color:#1e3a8a">📊 Yatırım Tezi</h3>
  <p>{Ana tez: 2-3 cümle, neden bu hisse ilgi çekici}</p>
</div>

<div class="grid-2">
  <div class="bull-box">
    <h3 style="margin-bottom:12px;color:#15803d">🟢 Katalizörler & Fırsatlar</h3>
    <ul class="risk-list">
      <li>Fırsat 1 açıklaması</li>
      <li>Fırsat 2 açıklaması</li>
      <li>Fırsat 3 açıklaması</li>
    </ul>
  </div>
  <div class="bear-box">
    <h3 style="margin-bottom:12px;color:#b91c1c">🔴 Riskler & Endişeler</h3>
    <ul class="risk-list">
      <li>Risk 1 açıklaması</li>
      <li>Risk 2 açıklaması</li>
      <li>Risk 3 açıklaması</li>
    </ul>
  </div>
</div>
```

---

## Tam HTML İskelet {#skeleton}

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{ŞİRKET} ({TICKER}) — Kapsamlı Yatırım Analizi</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>
  /* ← Yukarıdaki CSS'in tamamı buraya -->
</style>
</head>
<body>

<!-- HEADER -->
<div class="header"> ... </div>
<div class="disclaimer-banner"> ... </div>

<!-- MAIN CONTENT -->
<div class="container">

  <!-- KPI TILES -->
  <div class="kpi-grid"> ... </div>

  <!-- BÖLÜM 1: GELİR ANALİZİ -->
  <div class="section">
    <div class="section-header">
      <div class="section-number">1</div>
      <div class="section-title">Gelir Analizi</div>
    </div>
    <div class="grid-2">
      <div class="card">
        <div class="card-title">Yıllık Gelir Trendi</div>
        <div class="chart-container"><canvas id="annualRevenueChart"></canvas></div>
      </div>
      <div class="card">
        <div class="card-title">Çeyreklik Gelir</div>
        <div class="chart-container"><canvas id="quarterlyChart"></canvas></div>
      </div>
    </div>
  </div>

  <!-- BÖLÜM 2: KARLILIK -->
  <div class="section">
    <div class="section-header">
      <div class="section-number">2</div>
      <div class="section-title">Karlılık & Marjlar</div>
    </div>
    <div class="grid-2">
      <div class="card">
        <div class="card-title">Marj Trendi</div>
        <div class="chart-container"><canvas id="marginChart"></canvas></div>
      </div>
      <div class="card">
        <div class="card-title">EPS Trendi</div>
        <div class="chart-container"><canvas id="epsChart"></canvas></div>
      </div>
    </div>
  </div>

  <!-- BÖLÜM 3: SEGMENTLER -->
  <!-- BÖLÜM 4: BÜYÜME / BACKLOG -->
  <!-- BÖLÜM 5: BEKLENTİLER -->
  <!-- BÖLÜM 6: DEĞERLEME & RAKIPLER -->
  <!-- BÖLÜM 7: RİSK & FIRSAT -->

</div><!-- /container -->

<script>
  // Tüm Chart.js grafikleri buraya
</script>

</body>
</html>
```