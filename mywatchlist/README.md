# Tugas 3 PBP 19 September 2022

## Perbedaan JSON, XML, dan HTML

### JSON

JSON atau Javascript Object Notion adalah sebuah format untuk menstrukturkan data.

Beberapa keuntungan dari JSON adalah:

- _Human-readable_ dan bisa ditulis sendiri.
- Karena bentuk data yang simpel, membuat transfer data JSON ringan dan mudah dibaca dan ditulis dibandingkan XML.

- Banyak digunakan sebagai penyimpanan data dan cara berkomunikasi antar web.

- Walaupun diturunkan dari bahasa Javascript, JSON tidak bergantung pada bahasa. Maka, kode untuk membuat atau memakai JSON bisa ditulis dalam bahasa apapun.

### XML

- Extensible Markup Language (XML) adalah bahasa komputer yang dibuat oleh World Wide Web Consortium (W3C) untuk menyederhanakan proses pertukaran dan penyimpanan data.

- JSON lebih sederhana daripada XML, tetapi XML lebih kuat. Untuk aplikasi umum, semantik singkat JSON menghasilkan kode yang lebih mudah diikut i. Untuk aplikasi dengan persyaratan kompleks seputar pertukaran data, seperti di perusahaan, fitur kuat XML dapat mengurangi risiko perangkat lunak secara signifikan.

### HTML

- Hypertext Markup Language atau HTML adalah bahasa markup standar yang digunakan untuk membuat halaman website dan aplikasi web.

## Alasan _data delivery_ dibutuhkan dalam sebuah web platform.

### Penyampaian data yang disimpan di database ke frontend

- Tentunya data yang disimpan dalam database akan digunakan pada suatu saat, karena itu, _data delivery_ dibutuhkan dalam pembuatan sebuah aplikasi.

- Penyampaian data bisa dalam JSON, XML, atau format penyampaian data lainnya.

### Karena dalam sebuah tim, developer frontend dan backend adalah 2 tim yang berbeda

- Tim Frontend hanya perlu memanggil suatu url yang dikerjakan oleh tim backend dan membuat frontend yang menggunakan data yang diberikan backend

- Tim backend hanya perlu menyediakan url dan menangani request dari frontend

## Cara implementasi aplikasi mywishlist

### Pembuatan fixtures yang berisi `initial_watchlist_data.json`

- Pembuatan _constants_ film-film yang sudah/belum pernah saya tonton, diisi dengan data-data yang sesuai model `MyWatchList`.

### Pembuatan `models.py`

- Buat sebuah Model `MyWatchList` dengan fields:
  - watched: Boolean Field (default = False)
  - title: Character Field (max_length = 100)
  - rating: Decimal Field (range = [1 ... 5])
  - release_date: Date Field (menyimpan tanggal/bulan/tahun)
  - review: Text Field

### Pembuatan `views.py` dan `urls.py`

- Pembuatan `show_xml`, `show_json`, dan `show_html`

  - `show_xml` dan `show_json` hanya mengembalikan data pada model `MyWatchList` dalam bentuk **JSON** dan **XML**

  - `show_html` menerima context yang berupa data watchlist di database, dan mengembalikan `watchlist.html`

- Pembuatan `urls.py`

  - `urls.py` memiliki 3 routes, `show_html`, `show_json`, `show_xml`, dan `index` yang mengembalikan HttpResponse kosong.

### Pembuatan `watchlist.html`

- `watchlist.html` berisi frontend yang akan mengembalikan html yang menyediakan data-data `watchlist` dalam bentuk tabel.

- `{% load static %}` dan import `style.css` yang dibuat membantu agar styling css yang dibuat diterapkan ke `watchlist.html`

## Screenshot Postman Request

![HTML](/images/html.png)
![JSON](/images/json.png)
![XML](/images/xml.png)

## Screenshot Tests `OK`

![Tests](/images/test.png)
