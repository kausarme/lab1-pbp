

## Tutorial

Anda diminta untuk menambahkan fungsionalitas AJAX ke projek `wishlist` yang sudah dibuat pada Tutorial 1.

- [x] Buatlah templat baru bernama `wishlist_ajax.html` dengan isi yang sama seperti `wishlist.html`
- [x] Buat _view_ baru yang mengarah ke halaman `wishlist_ajax.html`. Tambahkan pula _path_ `/wishlist/ajax` untuk mengakses _view_ tersebut.
- [ ] Implementasikan AJAX pada halaman `wishlist_ajax.html`
    - [ ] Lakukan pengambilan seluruh data `wishlist` dengan menggunakan **AJAX GET**. Anda dapat menggunakan endpoint JSON yang telah dibuat pada Lab 2 sebagai sumber data.
    - [ ] Buatlah `form` untuk menambahkan BarangWishlist dengan menggunakan **AJAX POST**.
        - [ ] Buatlah _view_ baru yang menerima data JSON dan menambahkan BarangWishlist baru ke _database_.
        - [ ] Tambahkan _path_ `/wishlist/ajax/submit` yang mengarah ke _view_ yang telah Anda buat.
        - [ ] Gunakan `jQuery` atau `fetch()` untuk melakukan submisi data form secara asinkronus ke _path_ yang telah dibuat.
        - [ ] Lakukan _refresh_ BarangWishlist pada tabel secara asinkronus untuk menampilkan barang yang ditambahkan tanpa _reload_ seluruh halaman.

<u>Anda harus menggunakan AJAX saat mengimplementasikan tugas ini. Submisi yang tidak menggunakan AJAX **tidak dinilai**.</u>