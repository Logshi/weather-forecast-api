import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
from src.utils.weather_data import get_weather

# Örnek veri toplama (Son 30 gün için rastgele hava durumu oluştur)
np.random.seed(42)
dates = pd.date_range("2023-01-01", periods=30)
temps = np.random.normal(loc=15, scale=5, size=len(dates))  # Ortalama sıcaklıklar

df = pd.DataFrame({"date": dates, "temperature": temps})
df["day"] = df.index

# Makine Öğrenimi Modeli
X = df["day"].values.reshape(-1, 1)
y = df["temperature"].values

model = LinearRegression()
model.fit(X, y)

# Modeli Kaydet
with open("models/weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model eğitildi ve kaydedildi!")
