Stereo matching adalah proses menemukan hubungan antara dua piksel yang diambil dari sudut pandang yang berbeda. Hubungan tersebut disebut dengan disparity map.Stereo matching merupakan teknologi inti dalam visi komputer yang bertujuan untuk memulihkan struktur 3D dunia nyata dari gambar 2D. Teknologi ini banyak digunakan dalam berbagai bidang seperti mengemudi otomatis, realitas tertambah, dan navigasi robotika. Stereo matching menentukan keakuratan dalam mendapatkan nilai depth. Kedalaman (depth) adalah estimasi jarak antara objek dengan kamera yang didapatkan dengan menghitung perbedaan jarak horisontal suatu titik yang sama pada dua buah gambar.

![image](https://github.com/user-attachments/assets/77b19d1a-ad84-494a-8f0a-f81a25196dc5)

Kode tersebut digunakan untuk menambahkan path folder Image_Lib ke dalam daftar search path modul Python (sys.path). Hal ini memungkinkan Python untuk mengimpor modul atau skrip Python dari folder tersebut, meskipun lokasinya tidak berada di directory default Python.

![Screenshot 2024-11-20 131347](https://github.com/user-attachments/assets/03a2df6d-76e0-4899-8d82-d75873cdec3b)

Fungsi detect_face bertujuan untuk mendeteksi wajah dalam sebuah gambar menggunakan Haar Cascade yang disediakan oleh OpenCV. Fungsi ini mengembalikan wajah terbesar yang terdeteksi dalam bentuk koordinat kotak pembatas (bounding box)

![image](https://github.com/user-attachments/assets/417bbdda-76e0-4ad4-a270-6fdc80299e52)

Fungsi write_ply digunakan untuk menyimpan data 3D yang telah diakumulasi dalam array global accumulated_verts ke dalam file dengan format PLY (Polygon File Format). File ini dapat digunakan untuk merepresentasikan data 3D, seperti model permukaan atau titik awan (point cloud), dan biasanya dapat dibuka dengan perangkat lunak pemodelan 3D seperti MeshLab.

![image](https://github.com/user-attachments/assets/db2e5122-fe5b-413d-a104-f8222c807d69)

Fungsi append_ply_array digunakan untuk menambahkan data baru (koordinat 3D dan warna) ke dalam array global accumulated_verts. Data ini nantinya dapat diekspor dalam format PLY untuk representasi 3D.

![image](https://github.com/user-attachments/assets/86517f4d-299e-41a1-a747-388adc901570)

Fungsi stereo_match digunakan untuk menghitung disparity map dari dua gambar stereo, yaitu gambar kiri (imgL) dan gambar kanan (imgR). Disparity map adalah representasi perbedaan posisi objek dalam gambar kiri dan kanan, yang bisa digunakan untuk merekonstruksi informasi kedalaman (depth map) dalam ruang 3D.

