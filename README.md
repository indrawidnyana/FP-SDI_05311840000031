# Final Project Sistem Deteksi Intrusi
---------

## Face Gender Detection using Machine Learning Algorithm on Python (Pengimplementasian pada Tempat dengan Gender Restricted misalnya Toilet Mall)
  

--------------------------------------------


### Nama : I Gede Pradhana Indra Widnyana
### NRP  : 05311840000031

---------------------------------------------

### Deskripsi Project : 
Jika kita melihat lingkungan sekitar kita, maka masih banyak sekali hal-hal atau kegiatan yang bersifat negatif khususnya tindakan asusila terjadi. Banyak sekali contoh kegiatan asusila yang terjadi, mulai dari pelecehan seksual bahkan hingga pemerkosaan. Ironisnya kegiatan ini tidak hanya terjadi pada tempat-tempat tertutup, namun tidak jarang terjadi pada tempat umum seperti : ***Toilet umum, Toilet sekolah, Toilet mall, dll.*** Dari masalah yang sangat miris tersebut, maka dibuatlah project ini untuk mendeteksi intrusi terhadap **gender** melalui scan wajah untuk meminimalisir terjadinya kegiatan asusila tadi terutama di tempat umum.

Project ini menggunakan **Algoritma machine learning dengan bahasa pemrograman python** untuk mempelajari wajah dari target yang nantinya akan dirubah dalam bentuk model dan akan discanning pada kamera untuk memetakan apakah seseorang dapat masuk toilet umum sesuai dengan jenis kelamin mereka yang terdeteksi. metode pemrograman menggunakan bahasa pemrograman python dengan beberapa library inti yaitu ****Tensorflow (keras), OpenCv, numpy, pycurl, pushbullet library, dan lain-lain.***

---------------------
## Library Requirement

| Library | Version |
| ----------- | ----------- |
| **Tensorflow** | 2.3.0 |
| **numpy** | 1.19.2 | 
| **OpenCv** | 4.0.1 | 
| **PyCurl** | 7.43.0.6 | 
| **jsonschema** | 3.2.0 | 
| **pushbullet** | 0.12.0 | 
| **scikit-learn** | 0.23.2 | 
| **matplotlib**| 3.3.2 | 

----------------------------
## Dataset Model Gender
* Untuk dataset terdapat pada folder **gender_dataset_wajah** yang dimana folder tersebut berisi 2 folder lagi untuk deteksi wajah kedua gender, yaitu **laki-laki** dan **perempuan**
* Dalam dataset **laki-laki** berisi kurang lebih ***1529 sample*** untuk wajah laki-laki yang nantinya akan dijalankan dengan machine learning untuk membuat kumpulan model laki-laki
* Dalam dataset **perempuan** berisi kurang lebih ***1380 sample*** untuk wajah perempuan yang nantinya akan dijalankan dengan machine learning untuk membuat kumpulan model perempuan

-----------------------------
## Cara Kerja Program
