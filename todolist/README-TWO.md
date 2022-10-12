# Tugas 6 PBP 12 Oktober 2022

## Perbedaan _asynchronous programming_ dengan _synchronous programming_

- _Synchronous programming_ merupakan programming yang menjalani program dari atas sampai bawah, dan data yang dioutput akan harus diketahui sebelum kita output

- _Asynchronous programming_ kebalikan dari _synchronous programming_, dimana proses variabel yang tidak diketahui itu normal, dan bisa saja kita menunggu agar variabel sudah diload daru source lain, bisa saja dalam bentuk API/Endpoint.

## Event-driven programming

Event-driven programming merupakan sebuah paradigma dimana para objek, elemen, servis, dan lain-lain berkomunikasi dengan satu sama lain secara tidak langsung dengan cara mengirim pesan secara tidak langsung melalui medium yang dinamakan _event_

Dalam tugas ini, contoh penggunaan event adalah saat menunggu proses `/todolist/add/`, function `.done` akan menangani _event_ saat API `/todolist/add/` selesai menambahkan data yang diberikan melalui `POST` request.

## Penerapan _asynchronous programming_ pada AJAX

contoh penerapan _asynchronous programming_ pada AJAX adalah saat kita memanggil suatu API

```js
$.ajax({
	url: "/some/url/",
	method: "POST",
	data: {},
}).done((resp) => {
	// penanganan response disini
});
```

Pada contoh di atas, kita bisa lihat bahwa setelah API pada route `/some/url/` telah selesai dipanggil, response akan ditangani pada segmen dibawahnya.

## Penjelasan penrapan checklist

### Pembuatan `$.get`

```js
$.get("/todolist/json/", function (data) {
	data.map((d) => {
		const task = d.fields;
		const task_id = d.pk;
		$(".container").append(new_entry(task, task_id));
	});
});
```

`$.get()` akan memanggil API `/todolist/json/` yang sudah dibuat pada minggu-minggu sebelumnya. Data-data tersebut akan ditampilkan dalam HTML yang sudah ditulis di `todolist.html`

### Pembuatan `$.ajax({ method: "POST" })`

```js
$.ajax({
	method: "POST",
	url: "/todolist/add/",
	data: { ...data, csrfmiddlewaretoken: "{{csrf_token}}" },
}).done(function (resp) {
	$(".container").append(new_entry(resp, resp.id));
	$(function () {
		$("#create-modal").modal("toggle");
	});
});
```

Setelah data dari form sudah di-`POST` ke server, server akan mengembalikan `JsonResponse` dengan data-data yang menyatakan `task` baru yang dibuat, kita akan append `task` baru ke `.container`.

### Pembuatan `$.ajax({method: "DELETE"})`

```js
$(".delete-button").each(function (index, obj) {
	$(this).click(function () {
		const this_id = $(this).attr("id");
		$.ajax({
			url: `/todolist/delete/${this_id}`,
			type: "DELETE",
			data: { csrfmiddlewaretoken: "{{csrf_token}}" },
		});
		location.reload();
	});
});
```

Iterasi di atas menangani script untuk delete button, jika ada suatu button yang di-click, maka akan memanggil suatu DELETE request ke `/todolist/delete/${task_id}/`.
