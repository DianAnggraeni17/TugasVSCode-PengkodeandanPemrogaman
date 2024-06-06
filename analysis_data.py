import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv('data_penjualan.csv')
print(data.head())

# Mengecek missing values
print(data.isnull().sum())

# Menghapus baris yang memiliki nilai hilang (jika ada)
data = data.dropna()

# Mengubah tipe data jika diperlukan (contohnya kolom 'harga' ke tipe numerik)
data['harga'] = pd.to_numeric(data['harga'], errors='coerce')
print(data.dtypes)

# Menambah kolom total penjualan
data['total_penjualan'] = data['jumlah'] * data['harga']
print(data.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Statistik deskriptif
print(data.describe())

# Visualisasi penjualan berdasarkan jenis kelamin
sns.countplot(data=data, x='jenis_kelamin')
plt.title('Distribusi Penjualan Berdasarkan Jenis Kelamin')
plt.show()

# Visualisasi total penjualan berdasarkan jenis barang
sns.barplot(data=data, x='jenis_barang', y='total_penjualan', estimator=sum)
plt.title('Total Penjualan Berdasarkan Jenis Barang')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Memisahkan fitur dan target
X = data[['jumlah', 'harga']]
y = data['total_penjualan']

# Membagi data menjadi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error

# Memprediksi data uji
y_pred = model.predict(X_test)

# Menghitung error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

