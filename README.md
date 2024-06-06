# Deskripsi Soal
PT. Sukses Jaya Makmur adalah sebuah perusahaan yang bergerak di bidang penjualan berbagai macam barang elektronik dan kebutuhan rumah tangga. 
Perusahaan ini memiliki sistem penjualan yang mencatat setiap transaksi penjualan yang meliputi informasi nomor faktur, jenis kelamin pembeli, dan jenis barang yang dibeli. 
Data penjualan ini akan digunakan untuk melakukan analisis untuk berbagai tujuan seperti meningkatkan strategi pemasaran, memahami perilaku konsumen, dan memperkirakan penjualan di masa depan.

# Langkah Dalam Menganalisis Data:
1. Pengumpulan data dengan mengimpor pustaka yang diperlukan dan membaca data menggunakan file CSV
2. Data cleaning dengan membersihkan data dari nilai yang hilang atau tidak valid
3. Mentransformasi data sesuai kebutuhan analis
4. Melakukan Exploratory Data Analysis (EDA) untuk memahami karakteristik data
5. Membuat model prediksi penjualan berdasarkan data historis
6. Melakukan validasi model dan lakukan tuning parameter untuk meningkatkan akurasi
7. Menginterpretasikan hasil model dalam bentuk visualisasi diagram

# Hasil Visualisasi Analisis Data
## Distribusi Penjualan Berdasarkan Jenis Kelamin
![Figure_1](https://github.com/DianAnggraeni17/TugasVSCode-PengkodeandanPemrogaman/assets/167199303/2d39306d-0c3c-405f-8412-c0658f9be678) 
Pada diagram pertama yang menunjukkan distribusi penjualan berdasarkan jenis kelamin, terlihat bahwa penjualan antara pria dan wanita hampir sama, masing-masing dengan 5 transaksi. Hal ini menunjukkan bahwa tidak ada perbedaan signifikan dalam jumlah transaksi yang dilakukan oleh pria dan wanita.

## Total Penjualan Berdasarkan Jenis Barang
![Figure_2](https://github.com/DianAnggraeni17/TugasVSCode-PengkodeandanPemrogaman/assets/167199303/69b6b60d-233a-47be-9963-6f8448ea0e87) 
Diagram kedua menampilkan total penjualan berdasarkan jenis barang. Dari diagram ini, terlihat bahwa penjualan televisi mendominasi dengan total penjualan yang sangat tinggi dibandingkan dengan barang lainnya yaitu sebesar 5 barang. Laptop juga memiliki total penjualan yang cukup signifikan, sedangkan kulkas dan mesin cuci memiliki total penjualan yang lebih rendah.

## Diagram Perbandingan Aktual dan Prediksi
![Figure_3](https://github.com/DianAnggraeni17/TugasVSCode-PengkodeandanPemrogaman/assets/167199303/9e9d5a8e-00da-4a1a-92ff-065017d0af39) 
Diagram ketiga menunjukkan perbandingan antara nilai aktual dan prediksi dari model regresi yang telah dibuat. Terlihat bahwa ada perbedaan yang cukup besar antara nilai aktual dan prediksi. Hal ini menunjukkan bahwa model prediksi yang dibuat masih perlu perbaikan dan tuning parameter lebih lanjut untuk meningkatkan akurasinya.

# Rekomendasi dan Langkah Selanjutnya
Berdasarkan hasil analisis data yang telah dilakukan, ada beberapa langkah yang direkomendasikan untuk perusahaan kedepannya:
1. Penjualan antara pria dan wanita hampir sama, maka strategi pemasaran sebaiknya difokuskan secara merata untuk kedua kelompok.
2. Televisi dan laptop merupakan produk dengan total penjualan tertinggi. Perusahaan bisa fokus untuk meningkatkan stok dan promosi pada produk-produk ini.
3. Hasil dari diagram Actual vs Predicted menunjukkan bahwa model prediksi masih perlu diperbaiki. Perlu dilakukan tuning parameter, pemilihan fitur yang lebih baik, dan mungkin mencoba algoritma lain untuk meningkatkan akurasi prediksi.

