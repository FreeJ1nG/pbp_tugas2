# Tugas 5 PBP 6 Okt 2022

## Perbedaan inline, internal, dan external CSS

### Internal CSS

- Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
- Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
- Class dan ID bisa digunakan oleh internal stylesheet.
- Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
- Membuat performa website lebih lambat. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.

### External CSS

- Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
- Loading website menjadi lebih cepat.
  File CSS dapat digunakan di beberapa halaman website sekaligus.

### Inline CSS

- Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
- Berguna untuk memperbaiki kode dengan cepat.
- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

## HTML5 Tags

### `<div>`

> Menyatakan divisi atau suatu bagian dari dokumen.

### `<ul>`

> Unordered list

### `<a>`

> Hyperlink

### `<input>`

> Menyatakan tempat input untuk user

### `<img>`

> Menyatakan sebuah frame untuk gambar

### `<h1> sampai <h6>`

> Menyatakan header

### `<i>`

> Italic

### `<u>`

> Underline

## CSS Selector

### `.class`

> Memililh semua elemen dengan `class="class"`

### `.class1.class2`

> Memilih semua elemen yang memiliki `class1` dan `class2` dalam classnya

### `.class1 .class2`

> Memilih semua elemen dengan class `class2` yang merupakan elemen dibawah `class1`

### `#id`

> Memilih semua elemen dengan `id="id"`

### `*`

> Memilih semua elemen

## Proses membuat web responsive

### Menggunakan `@media` pada css

```css
@media only screen and (min-width: 600px) {
	.task-title {
		font-size: x-large;
		font-weight: bolder;
		font-family: "Courier New", Courier, monospace;
		color: black;
		display: flex;
		gap: 12px;
	}
}
```

Pada conton di atas, bisa dilihat bahwa class `.task-title` akan menjadi seperti yang diterakan di atas saat `width` dari `screen` $\geq$ `600 pixel`.

# Tugas 4 PBP 27 September 2022

## User accounts for this assignment

### User 1

```
username: hahahihi
password: tugaspbp
```

# User 2

```
username: usertodolist
password tugaspbp
```

## The use of `{% csrf_token %}` on `<form>` elements

Django has a `{% csrf_token %}` tag that is implemented to avoid malicious attacks. It generates a token on the server-side when rendering the page and makes sure to cross-check this token for any requests coming back in. If the incoming requests do not contain the token, they are not executed.

## Making a `<form>` element without the use of generators such as `{{ form.as_table }}`

**It is** possible to make a form without the use generators, we just need to make inputs with certain names

For example:
If you want to make a form with a name, email, and password

```html
<input type="text" name="name" placeholder="Name" />
<input type="email" name="email" placeholder="Email" />
<input type="password" name="password" placeholder="Password" />
```

As can be seen above, the datas from the inputs will be passed on to the server as a json/dictionary, with the format of `{"name_of_input": "value of input"}`, so with the example above, the data passed when the submit input is triggered will be something like:

```json
{
	"name": "Andrew Jeremy",
	"email": "andrew.jeremy@ui.ac.id",
	"password": "tugaspbp123"
}
```

## The process of data flow starting from form submission up to template rendering

### User inputs data to form

- Form passes on data as json/dictionary to backend (make a `POST/GET` request to a certain function defined in `views.py`)
- `views.py` saves data to database

### A URL Request gets a HTML response from a function in `views.py`

- `views.py` passes data from database for template rendering
- Data is passed in the form of context (json/dictionary)

## How my To Do List was implemented

### `models.py`

I made a `Task` model with

- `user = models.ForeignKey(User, on_delete=models.CASCADE)`
- `date = models.DateTimeField("Date created", default=timezone.now)`
- `title = models.CharField(max_length=50)`
- `description = models.TextField()`
- `is_finished = models.BooleanField(default=False)`

### `views.py`, `urls.py` and `templates`

- `show_todolist` with `@login_required` decorator
  - Shows tasks of the user
  - Renders `todolist.html`
  - url: `/todolist/`
- `create_task` with `@login_required` decorator
  - Creates new task from the data passed by `POST` method of form
  - Renders `create_task.html`
  - url: `/todolist/create-task/`
- `delete_task`
  - Deletes task with a certain `task_id`
  - url: `/todolist/delete_task/<int:task_id>/`
- `invert_task_status`
  - Inverts the `is_finished` field of a task with the passed `task_id`
  - url: `/todolist/invert-task-status/<int:task_id>/`
- `register`
  - Registers user with Django's `UserCreationForm`
  - Renders `register.html`
  - url: `/todolist/register/`
- `login_user`
  - Log in to django user system
  - Renders `login.html`
  - url: `/todolist/login/`
- `logout_user`
  - Log out from django user system
  - url: `/todolist/logout/`

### Making the templates

- Made HTML code to arrange the elements
- Styling the page with CSS
