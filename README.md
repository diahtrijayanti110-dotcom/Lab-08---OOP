
<body style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px;">

<h1>🎓 Lab 08 – OOP (Object-Oriented Programming)</h1>

<h2>📝 Tugas Praktikum</h2>

<p>
    Buat program sederhana dengan mengaplikasikan penggunaan class. Program menampilkan daftar nilai mahasiswa dengan ketentuan:
</p>

<ul>
    <li>➕ <b>tambah()</b> – Menambah data</li>
    <li>📄 <b>tampilkan()</b> – Menampilkan data</li>
    <li>❌ <b>hapus(nama)</b> – Menghapus data berdasarkan nama</li>
    <li>✏️ <b>ubah(nama)</b> – Mengubah data berdasarkan nama</li>
</ul>

<hr>

<h2>🧩 📘 Diagram Class Program</h2>

<p><b>📐 Diagram class yang menggambarkan struktur OOP program:</b></p>

<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/a3a1209e-9d19-4e39-81c0-b195a36696b3"
         alt="diagram class"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>🔍 Penjelasan:</b><br>
Diagram menunjukkan atribut: <i>nama</i>, <i>nim</i>, dan <i>nilai</i>, serta method: <i>tambah</i>, <i>tampilkan</i>, 
<i>hapus</i>, dan <i>ubah</i>. Class berfungsi mengelola daftar nilai mahasiswa.</p>

<hr>

<h2>🔄 📊 Flowchart Program</h2>

<p><b>🧭 Alur kerja program:</b></p>

<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/090a1c6e-4b7c-48fe-bcef-950c0602aafb"
         alt="Flowchart"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b><br>
Flowchart menjelaskan proses input menu → eksekusi → kembali ke menu sampai user memilih keluar.</p>

<hr>

<h2>📘 🧠 Penjelasan Bagian Program</h2>

<h3>🧩 1️⃣ Bagian 1 – Inisialisasi Class</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/2f43201b-d4b8-4696-9518-0b2c3d1b463b"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Mendefinisikan class dan struktur data awal mahasiswa.</p>

<h3>🧩 2️⃣ Method tambah()</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/7eb521ad-3661-480a-958b-8c97ac736095"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Menerima input nama, nim, nilai dan menyimpannya ke list.</p>

<h3>🧩 3️⃣ Method tampilkan()</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/86349e1c-ece7-41f9-8330-aa6b5f00b9fa"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Menampilkan seluruh data mahasiswa atau pesan jika kosong.</p>

<h3>🧩 4️⃣ Method hapus(nama)</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/5eb0ed60-14bc-434b-b795-cf0660b64ae0"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Menghapus data yang memiliki nama sesuai input.</p>

<h3>🧩 5️⃣ Method ubah(nama)</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/64948a94-78d9-4b0c-a142-039f8c9203ca"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Mengubah nilai mahasiswa berdasarkan nama.</p>

<h3>🧩 6️⃣ Menu Program</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/7e2a7aa8-30aa-4357-a73c-553200dcab85"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Menyediakan menu: tambah, tampilkan, hapus, ubah, keluar.</p>

<h3>🧩 7️⃣ Loop Program</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/5d981f79-56f5-4628-b019-a1090ff2cb18"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<p><b>Penjelasan:</b> Program terus berulang hingga user memilih keluar.</p>

<hr>

<h2>🖥️ 📌 Hasil Running Program</h2>

<h3>➕ 1. Menambahkan Data</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/3fbd6f21-955f-4a09-95ce-a2b8ccd3ab3a"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<h3>📄 2. Menampilkan Data</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/bd9ffdc6-d905-4e9d-83e1-5886300c902d"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<h3>✏️ 3. Mengubah Data</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/f24c8b64-0246-4ba4-98c7-b63c427eb424"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<h3>❌ 4. Menghapus Data</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/a289ff3f-a5b9-4e3c-9568-f48641517632"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<h3>🔄 5. Data Setelah Perubahan</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/f3c51a87-7edd-406f-8215-5ac1dc42e403"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<h3>🚪 6. Keluar Program</h3>
<div style="text-align:center; margin: 20px 0;">
    <img src="https://github.com/user-attachments/assets/36e48c54-c12e-428d-b51a-aa5e7e65b6eb"
         style="max-width:80%; border:1px solid #ddd; padding:10px; border-radius:10px; background:#fafafa;">
</div>

<hr>

<h2>🎉 Selesai!</h2>

</body>
</html>
