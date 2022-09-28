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
