# Sağlık Sigortası Ücret Tahmini
<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas">
  <img alt="Scikit-Learn" src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit">
  <img alt="Model Score" src="https://img.shields.io/badge/R%C2%B2%20Score-0.86-success">
</p>
Bu proje, bireylerin sağlık bilgilerini kullanarak sigorta ücretini (`charges`) tahmin eden bir makine öğrenmesi uygulamasıdır.  
Veri analizi, ön işleme, model eğitimi ve Streamlit ile etkileşimli tahmin arayüzü tek bir akışta birleştirilmiştir.
---
## Proje Özeti
- Sağlık sigortası veri seti üzerinde keşifsel veri analizi (EDA) yapıldı.
- Eksik/tekrarlı/veri tutarlılığı kontrolleri gerçekleştirildi.
- Kategorik değişkenler sayısal formata dönüştürüldü.
- `RandomForestRegressor` ile tahmin modeli kuruldu.
- Model, kullanıcıdan alınan verilerle canlı tahmin yapabilen bir Streamlit uygulamasına taşındı.
---
## Kullanılan Teknolojiler
- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
---
## Model Başarısı
- **$R^2$ Skoru: 0.86**
- **MAE** metriği ile hata analizi desteklenmiştir.
- `Actual vs Predicted` görselleştirmesi ile model çıktıları yorumlanmıştır.
> $R^2 = 0.86$ değeri, modelin hedef değişkendeki varyansın büyük bir kısmını açıkladığını gösterir.
---
## Proje Yapısı
```text
HealtRiskAnalysis/
│
├── app.py                 # Streamlit tahmin uygulaması
├── main.ipynb             # EDA, preprocessing, model eğitimi
├── insurance.csv          # Veri seti
├── insurance_model.pkl    # Eğitilmiş RandomForest modeli
└── scaler.pkl             # StandardScaler nesnesi
Uygulamayı Çalıştırma
1) Ortamı hazırlayın
Gerekli paketlerin kurulu olduğundan emin olun (streamlit, pandas, scikit-learn).

2) Uygulamayı başlatın
streamlit run app.py
3) Tahmin alın
Açılan web arayüzünde:

yaş, cinsiyet, BMI, çocuk sayısı, sigara kullanımı ve bölge bilgilerini girin,
Predict butonuna tıklayarak tahmini sigorta ücretini görüntüleyin.
Özellikler
Temiz ve kullanıcı dostu web arayüzü
Eğitim süreciyle uyumlu encoding + scaling
Gerçek zamanlı sigorta ücret tahmini
Risk segmentine yönelik hızlı yorum desteği
Geliştirme Fikirleri
Model karşılaştırması (XGBoost, Gradient Boosting, Linear Regression)
Hyperparameter tuning sonuçlarının dashboard’a eklenmesi
Tahmin açıklanabilirliği için SHAP/LIME entegrasyonu
Docker ile tek komutta deployment
