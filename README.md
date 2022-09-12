# Tugas 2 PBP 12 September 2022

## 1. Bagan Request User dan korelasi `urls.py`, `models.py`, `views.py`, dan `html`

![Bagan](bagan.png)

## 2. Virtual Environtment

Virtual Environment digunakan untuk menjaga lingkungan development tetap konsisten dan terpisah dari lingkungan pribadi Anda, bisa saja anda mengerjakan projek yang menggunakan versi python berbeda dengan python yang ada di komputer pribadi Anda. Virtual environment membantu agar versioning yang instalasi yang Anda lakukan tetap terjaga didalam environment tersebut.

## 3. Penjelasan Implementasi

### 1. Implementasi `views.py`

Saya membuat 3 fungsi, yang pertama fungsi index, fungsi index bisa dilihat sebagai berikut:

```py
def index(request):
  cart = Cart.objects.first()
  cart = [{"item": cart_item.item, "count": cart_item.count} for cart_item in cart.items.all()]

  return render(request, "shop.html", {
    "cart_size": len(cart),
    "cart": cart,
    "items": Item.objects.all()
  })
```

Fungsi index mengembalikan render dari sebuah file yang bernama `shop.html` (disimpan di template/shop.html), dan diberikan context yang berisi cart_size, cart, dan items, cart, masing-masing data yang disediakan ke front-end (HTML) melalui context diambil dari database yang tabelnya dispecify di `models.py`

### 2. Implementasi `urls.py`

`urls.py` adalah file yang mengatur routing aplikasi django kita

```py
urlpatterns = [
  path('', index, name='index'),
  path('add_to_cart/<str:item_uuid>/', add_to_cart, name="add_to_cart"),
  path('reduce_from_cart/<str:item_uuid>/', reduce_from_cart, name="reduce_from_cart"),
]
```

Seperti yang bisa dilihat di kode di atas, masing-masing path yang dinyatakan masing-masing menyatakan sebuah route. Sebagai contoh:

```py
path('', index, name='index')
```

Path tersebut menyatakan `url: {domain}/shop/, function: index, nama: 'index'` . Fungsi index akan dipanggil saat route yang dipanggil sesuai dengan path yang dinyatakan.

### 3. Implementasi `shop.html`

Dari data yang kita berikan dalam bentuk context ke template (HTML), kita bisa tampilkan data yang diberikan tersebut

```html
<div class="item-card-container">
	<div class="button-container">
		{% for item in items %}
		<div class="item-card-button">
			<a href="{% url 'shop:add_to_cart' item.uuid %}" class="item-card-cover">
				<div
					style="
              font-weight: 700;
              font-size: large;
              font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
                'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            "
				>
					{{ item.name }}
				</div>
				<div
					style="
              font-weight: 500;
              font-size: medium;
              font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
                'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            "
				>
					Rp{{ item.get_price_in_rupiah }}
				</div>
				<div class="item-card-cta" style="border: none">Add to cart</div>
			</a>
			<img class="item-card-image" src="{{ item.image.url }}" />
		</div>
		{% endfor %}
	</div>
</div>
```

Seperti contoh HTML di atas, kita bisa lihat bahwa data-data yang diberikan oleh backend diterima oleh frontend kita, contoh penggunaan data `{{ item.name }}` artinya cek attribut `name` dari variabel `name` yang di-_passing_ oleh backend.

## 4. Deployment

Deployment Heroku untuk app ini bisa dilihat melalui: [Heroku App](https://andrew-pbp-tugas2.herokuapp.com/shop/).

Deployment heroku berjalan secara otomatis melalui `delpoy.yml` yang dijalankan oleh Github Actions, setelah menyesuaikan settings.py untuk deployment, push repository github dan masukkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` kepada secrets variabel di github dan heroku.
