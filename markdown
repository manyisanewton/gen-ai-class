# Getting Started with Django – A Beginner’s Web Framework Toolkit

## 🎯 Objective

This toolkit is a beginner-friendly introduction to Django, a high-level Python web framework. The goal is to help newcomers understand how Django works and build a small web project that displays blog posts and allows user comments.

This guide was created using generative AI (ChatGPT) to prompt for setup steps, code assistance, debugging, and documentation.

By the end of this guide, users will have:

- A working Django blog app
- Learned how to set up Django with virtual environments
- Used models, views, templates, and forms
- Deployed a minimal web app locally

## 🔍 What is Django?

**Django** is a high-level, open-source Python web framework that helps developers build secure and maintainable websites quickly. It follows the **Model-View-Template (MVT)** architectural pattern and comes with many built-in features to reduce repetitive tasks.

### 🌍 Where is Django Used?

Django is used to build all kinds of web applications, including:

- Blogs and personal websites
- E-commerce platforms
- APIs and backend services
- Content management systems (CMS)
- Dashboards and internal tools

Major companies like **Instagram**, **Pinterest**, and **Mozilla** have used Django at various points in their stacks.

### 📦 Why Django?

- Fully featured — includes ORM, admin interface, authentication, and more
- Python-based — ideal if you already know Python
- Secure by default — protects against common web vulnerabilities
- Scalable and robust — used in both small projects and large-scale apps

### 💡 Real-World Example

In this project, I’ve used Django to build a **mini blog platform** where users can view posts and leave comments. This reflects real-world use cases like WordPress or Medium, but with Django’s simplicity and power.

## 💻 System Requirements

To follow this toolkit and run the Django blog project, make sure your system meets the following requirements:

### ✅ Operating System

- Linux (tested on Ubuntu 20.04+)
- macOS (tested on Monterey+)
- Windows 10+ (recommended to use WSL or Git Bash)

### 🛠 Tools & Editors

- [Python 3.8+](https://www.python.org/downloads/)
- [pip (Python package manager)](https://pip.pypa.io/)
- [Virtualenv](https://virtualenv.pypa.io/) (for managing Python environments)
- [VS Code](https://code.visualstudio.com/) (or any code editor of your choice)
- Terminal or Command Prompt

### 📦 Required Packages

All packages can be installed using `pip`.

| Package                      | Purpose                          |
| ---------------------------- | -------------------------------- |
| `Django 4.2.x`               | Python web framework             |
| `Pillow`                     | Required to handle image uploads |
| `gunicorn` _(optional)_      | For production deployment        |
| `python-dotenv` _(optional)_ | Manage environment variables     |

You can install Django and Pillow via:

```bash
pip install django pillow
```

## ⚙️ Installation & Setup Instructions

This section walks you through setting up Django in a local development environment.

> 💡 All commands are run in a terminal. Ensure Python and pip are already installed.

---

### 🔹 Step 1: Create a Project Directory

```bash
mkdir django-blog
cd django-blog
```

### 🔹 Step 2: Set Up a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate

```

A virtual environment keeps your project’s dependencies isolated.

### 🔹 Step 3: Install Required Packages

```bash
pip install django pillow

```

### 🔹 Step 4: Start a Django Project

```bash
django-admin startproject mysite .

```

### 🔹 Step 5: Start the Blog App

```bash
python manage.py startapp blog

```

### 🔹 Step 6: Register the App in settings.py

Open mysite/settings.py and add 'blog', to INSTALLED_APPS:

```bash
INSTALLED_APPS = [
    ...
    'blog',
]

```

### 🔹 Step 7: Apply Initial Migrations

```bash
python manage.py migrate


```

### 🔹 Step 8: Run the Development Server

```bash
python manage.py runserver


```

Visit: http://127.0.0.1:8000
You should see the Django welcome page 🎉

### 🔹 Step 9: Create a Superuser (for Admin Panel)

```bash
python manage.py createsuperuser


```

Follow the prompts for username, email, and password.

Then log in at:
http://127.0.0.1:8000/admin

| Step                          | Screenshot                                       | Snippet/Output |
| ----------------------------- | ------------------------------------------------ | -------------- |
| 1. Create project folder      | Terminal showing `mkdir` and `cd`                | ✔️             |
| 2. Create virtual environment | Terminal showing `python3 -m venv env`           | ✔️             |
| 3. Install Django + Pillow    | `pip install django pillow` output               | ✔️             |
| 4. Start Django project       | `django-admin startproject mysite .` folder tree | ✔️             |
| 5. Create blog app            | `startapp blog` folder tree                      | ✔️             |
| 6. Update `INSTALLED_APPS`    | Screenshot of `settings.py` edit                 | ✔️             |
| 7. Run migrations             | Terminal output of `migrate`                     | ✔️             |
| 8. Run server                 | Output showing: “Starting development server…”   | ✔️             |
| 9. Create superuser           | Screenshot of admin login + user creation        | ✔️             |

## 🧪 Minimal Working Example (Django Blog App)

This section demonstrates the basic Django blog app I built using everything I learned.

### ✅ App Features

- Display list of blog posts
- View details of a single post
- Upload and display images with posts
- Add comments to posts (with a form)
- Admin dashboard to manage posts and comments

---

### 🛠️ Models

```python
# blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

def post_list(request):
posts = Post.objects.all().order_by('-created_at')
return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
post = get_object_or_404(Post, pk=pk)
comments = post.comments.all()
form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

# blog/forms.py

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
class Meta:
model = Comment
fields = ['name', 'body']

# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
path('', views.post_list, name='post_list'),
path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
path('', views.post_list, name='post_list'),
path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

{% for post in posts %}

  <div class="post">
    <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h2>
    {% if post.image %}
      <img src="{{ post.image.url }}" alt="{{ post.title }}" style="max-width:300px;">
    {% endif %}
    <p>{{ post.body|truncatechars:200 }}</p>
  </div>
{% endfor %}

## 🤖 AI Prompt Journal

Throughout this capstone, I used **ChatGPT** (Generative AI) as a learning assistant and debugging partner while building the Django project.

Below are selected prompts and how they helped during each stage:

---

### 🔹 Day 1–3: Project Setup & Models

**Prompt:**

> What is Django and how can I use it for web development?

**Response:**  
Helped me understand Django’s architecture (MVT), and how to set up a project using `django-admin startproject` and create apps using `startapp`.

---

**Prompt:**

> How do I define a Post model and make migrations?

**Response:**  
Guided me to create `models.py`, use `makemigrations` and `migrate` to create the database tables.

---

### 🔹 Day 4–6: Admin, Views, and Templates

**Prompt:**

> How do I register a model in the Django admin panel?

**Response:**  
Helped me write `admin.site.register(Post)` and customize admin fields for better readability.

---

**Prompt:**

> TemplateDoesNotExist error when rendering post_list.html

**Response:**  
Explained how to structure `templates/`, configure `DIRS` in settings, and fix path issues.

---

### 🔹 Day 7–8: Static, Media & Forms

**Prompt:**

> How do I upload and display images with a Django model?

**Response:**  
Helped me set up `ImageField`, install `Pillow`, configure `MEDIA_URL` and `MEDIA_ROOT`, and serve images in templates.

---

**Prompt:**

> How do I create and use ModelForms for user input?

**Response:**  
Showed how to use `forms.ModelForm` for the comment system and handle POST requests in views.

---

### 🔹 Day 9+: Debugging & Fixes

**Prompt:**

> NoReverseMatch: Reverse for 'post_detail' not found

**Response:**  
Helped me check `name=` values in `urls.py` and make sure `redirect()` used the correct name.

---

**Prompt:**

> Why does Django say “.forms could not be resolved”?

**Response:**  
Helped me check import paths, confirm the file existed, and adjust `from blog.forms import CommentForm`.

---

### 💡 How AI Helped

- 📚 Explained confusing errors step-by-step
- 🧠 Helped me learn Django fundamentals like views, forms, templates
- 🛠️ Debugged real-time issues with code context
- 📄 Helped write documentation for this toolkit

---

> Using AI made the learning process faster, less frustrating, and more engaging — like having a Python expert by my side every day.

## 🐛 Common Issues & Fixes

During the development of this Django blog project, I faced several errors and bugs. Below is a list of those issues and how I resolved them using AI support and documentation.

---

### ❌ Issue 1: `django.core.exceptions.ImproperlyConfigured: Cannot use ImageField because Pillow is not installed`

**Fix:**  
Installed the Pillow package using:

```bash
pip install Pillow
```

# ❌ Issue 2: TemplateDoesNotExist: blog/post_list.html

# Fix:

#

# Created a templates/blog/post_list.html file

#

# Ensured that the TEMPLATES setting in settings.py included this:

#

# ```python

# 'DIRS': [BASE_DIR / 'templates'],

# ```

#

# Confirmed that the blog app template was placed in templates/blog/ folder.

# ❌ Issue 3: Reverse for 'post_detail' not found

# Fix:

# The name used in the redirect() function or {% url %} tag didn’t match the name in urls.py.

#

# Corrected URL path:

#

# ```python

# path('post/<int:pk>/', views.post_detail, name='post_detail'),

# ```

#

# And updated redirect() and {% url 'post_detail' post.pk %} to match.

# ❌ Issue 4: .forms could not be resolved

# Fix:

#

# Verified that forms.py existed in the blog/ folder.

#

# Fixed import typo:

#

# ```python

# from .forms import CommentForm

# ```

# ❌ Issue 5: 404 Error on /post/1/ even though post exists

# Fix:

# I realized I was trying to visit /post/1/ while my app URL was set to /blog/post/1/.

#

# Corrected by using the full path:

#

# ```text

# http://127.0.0.1:8000/blog/post/1/

# ```

# ❌ Issue 6: Media files not displaying

# Fix:

#

# Made sure I had these in settings.py:

#

# ```python

# MEDIA_URL = '/media/'

# MEDIA_ROOT = BASE_DIR / 'media'

# ```

#

# Added this to urls.py:

#

# ```python

# from django.conf import settings

# from django.conf.urls.static import static

#

# if settings.DEBUG:

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ```

#

# Confirmed that uploaded images went into the /media/post_images/ folder.

## 📚 Additional Resources

Here are the references and learning resources that supported my Django journey and helped build this beginner’s toolkit:

---

### 🔗 Official Documentation

- [Django Documentation](https://docs.djangoproject.com/en/stable/)  
  The official guide for everything Django, including models, views, forms, templates, and deployment.

- [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)  
  Helped me define fields like `CharField`, `TextField`, and `ImageField`.

- [Django Admin Site Guide](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)  
  Used to configure and customize the admin dashboard for managing posts and comments.

---

### 🛠 Tools Used

- **Python 3.8**
- **Django 4.2**
- **Pillow** – for image upload support
- **SQLite3** – Django’s default development database
- **VS Code** – code editor with Django extensions
- **ChatGPT** – generative AI assistant for learning, debugging, and documentation support

---

### 🧠 Learning Platforms

- [MDN Web Docs - Django Getting Started](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Real Python - Django Tutorials](https://realpython.com/tutorials/django/)
- [DjangoGirls Tutorial](https://tutorial.djangogirls.org/) – beginner-friendly guide

---

### 💬 Community Forums

- [Stack Overflow](https://stackoverflow.com/questions/tagged/django)
- [r/django on Reddit](https://www.reddit.com/r/django/)
- [Django Discord Server](https://discord.gg/django)

---

> These resources helped me troubleshoot errors, understand concepts, and extend features in my blog app. They are also great for anyone looking to deepen their Django skills.
