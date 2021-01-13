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
* **Tensorflow Library dan Keras untuk algoritma pendeteksi wajah**
    > Penggunaan library ini adalah untuk mengecek apakah ada wajah yang terdapat pada frame kamera, dan semisal ada maka akan dicek kembali apakah wajar dari dalam frame tersebut merupakan wajah laki-laki atau perempuan, sehingga pada proses ini mereturn value 0 atau 1 yang dimana 0 untuk perempuan dan 1 untuk laki-laki. framing didapatkan dari input yang diberikan pada library opencv. setelah itu akan diberikan label sesuai dengan jenis yaitu **laki-laki** atau **perempuan**

* **OpenCV Library untuk framing dan penggunaan kamera**
    > Untuk frame pada saat deteksi dan juga menghidupkan kamera pada script **detect_gender_webcam.py** menggunakan OpenCV Library sehingga frame-frame tersebut dapat diolah oleh library sebelumnya yaitu **Tensorflow**

* **Capture Frame dan Menyimpan File Image**
    > Selanjutnya, semisal ada intruder maka akan dilakukan capture frame oleh OpenCV lib dan disave pada direktori dengan nama **Capture.JPG** yang dimana nantinya file tersebutlah yang akan dikirimkan ke **pushbullet notification**

* **Penggunaan PushBullet sebagai Media Notifikasi Alert Intruder**
    > Pushbullet merupakan sebuah aplikasi yang dapat dipasang di berbagai platform untuk notifikasi (push notification). dalam project ini, pushbullet dikoneksikan dengan code program dengan mengambil **API pada user**, sehingga dapat terkoneksi disaat program ingin mengirimkan notifikasi kepada PushBullet. Notifikasi yang dikirimkan adalah berupa gambar intruder yang sudah dicapture sebelumnya **(Capture.JPG)** serta notifikasi alert sebagai keterangan bahwa ada intruder yang masuk.

------------------------------------------

## Instalasi Program
### 1. Menginstall **Anaconda** sebagai platform untuk menjalankan program
* Melakukan installasi **Anaconda** sebagai platform untuk menjalankan program dan library
* membuat environment baru dalam anaconda (dapat melalui Anaconda Navigator). pada kasus ini saya menambahkan environment dengan nama **tensorflow**

> ![gambar5](/img/5.JPG)
### 2. Menginstall Library Requirement
* Membuka **Anaconda Navigator** 
* menjalankan environment yang telah dibuat sebelumnya (**tensorflow**)
* menginstall library sesuai dengan kebutuhan **library requirement** diatas
* instalasi dapat dilakukan dengan **mencari nama library dan mencentang lalu klik apply pada bagian pojok kanan bawah**

> ![gambar6](/img/6.JPG)
### 3. Instalasi dan daftar akun PushBullet
* Mendownload aplikasi PushBullet pada website resminya
* Melakukan instalasi pada program yang sudah di download (**Program PushBullet**)
* Melakukan registrasi akun pada pushbullet, registrasi pada web yang nantinya akan terkoneksi pada aplikasinya dengan melakukan login
* Instalasi PushBullet sukses

> ![gambar4](/img/4.JPG)
### 4. Setup token pada Kode program dengan menggunakan API PushBullet
* Menemukan API user pada bagian setting dalam website PushBullet
* Memasukkan API user pada file **detect_gender_webcam.py** lebih tepatnya pada bagian ***token***


> ![gambar7](/img/7.JPG)
### 4. Menjalankan program "train.py" untuk membuat model dengan metode machine learning
* program pertama dijalankan untuk membuat file **.model** yang akan digunakan untuk model pada program deteksi selanjutnya
* run program dapat dengan cara membuka **anaconda prompt** dan menghidupkan environtment yang dibuat dengan cara ***conda activate tensorflow***. tensorflow sendiri merupakan env yang kita buat pada step sebelumnya
* selanjutnya menjalankan program dengan perintah **python xx\xx\xx\xx\train.py** 
* setelah menunggu proses, maka akan ada file baru dengan nama **gender_detection.model** yang nantinya akan digunakan dalam program detection selanjutnya
*hasil plot dari machine learningnya dapat dilihat pada gambar dibawah :


> ![plot](plot.png)
### 5. Menjalankan program "detect_gender_webcam.py" untuk melakukan deteksi gender wajah
* run program dapat dengan cara membuka **anaconda prompt** dan menghidupkan environtment yang dibuat dengan cara ***conda activate tensorflow***. tensorflow sendiri merupakan env yang kita buat pada step sebelumnya
* selanjutnya menjalankan program dengan perintah **python xx\xx\xx\xx\detect_gender_webcam.py**
* setelah window webcam terbuka, maka deteksi sudah bisa dilakukan. karena dalam program diset untuk intruder muncul jika yang muncul adalah **perempuan**, maka disaat ada wajah perempuan, program akan langsung mengirimkan notifikasi pada pushbullet user. ***(contoh berikut dapat diterapkan pada toilet laki-laki)***




> ## Hasil Run Program 
![gambar1](/img/1.png)
![gambar2](/img/2.png)
![gambar3](/img/3.png)







