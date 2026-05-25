import pandas as pd
import numpy as np
import math
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('dis_klinigi_2yil_hasta_verisi.csv')

X = df.drop(columns=['tarih', 'hasta_sayisi'])
y = df['hasta_sayisi']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)


def tarihi_ozelliklere_cevir(tarih_metni, resmi_tatil=0, dini_bayram=0, bayrama_kalan_gun=999):
    tarih = pd.to_datetime(tarih_metni)

    yilin_gunu = tarih.dayofyear
    haftanin_gunu = tarih.weekday()
    ay = tarih.month

    return [yilin_gunu, haftanin_gunu, ay, resmi_tatil, dini_bayram, bayrama_kalan_gun]


def izin_durumu_hesapla(hedef_gun_ozellikleri, toplam_personel, personel_basi_kapasite, guvenlik_payi=1):
    ozellik_isimleri = ['yilin_gunu', 'haftanin_gunu', 'ay', 'resmi_tatil', 'dini_bayram', 'bayrama_kalan_gun']
    hedef_df = pd.DataFrame([hedef_gun_ozellikleri], columns=ozellik_isimleri)

    tahmini_hasta = model.predict(hedef_df)[0]

    gereken_personel = math.ceil(tahmini_hasta / personel_basi_kapasite)
    izin_verilebilir_kisi = toplam_personel - gereken_personel - guvenlik_payi
    izin_verilebilir_kisi = max(0, izin_verilebilir_kisi)

    return round(tahmini_hasta), izin_verilebilir_kisi


istenen_tarih = input("Tarih:(Y-A-G) ")

hedef_gun = tarihi_ozelliklere_cevir(
    tarih_metni=istenen_tarih,
    resmi_tatil=1,
    dini_bayram=0,
    bayrama_kalan_gun=999
)

klinik_toplam_personel = 10
personel_gunluk_kapasite = 15
guvenlik_stogu = 1

beklenen_hasta, verilebilecek_izin = izin_durumu_hesapla(
    hedef_gun,
    klinik_toplam_personel,
    personel_gunluk_kapasite,
    guvenlik_stogu
)

print("-" * 50)
print(f"Hedef Tarih: {istenen_tarih}")
print(f"Tahmini Hasta Sayısı: {beklenen_hasta}")
print(
    f"Klinikte Çalışması Gereken Personel: {math.ceil(beklenen_hasta / personel_gunluk_kapasite) + guvenlik_stogu} (Güvenlik payı dahil)")
print(f"ONAYLANABİLECEK MAKSİMUM İZİN: {verilebilecek_izin} kişi")
print("-" * 50)