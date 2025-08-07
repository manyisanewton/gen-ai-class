
# 🧠 Beginner’s Toolkit with GenAI: Django Blog App

This project was built as part of the **Moringa AI Capstone** to demonstrate how GenAI tools can accelerate learning and development of a new framework. The focus was on building a full-featured **Django Blog App** from scratch while applying core concepts learned with guidance from ChatGPT.

---

## 🚀 Project Overview

This is a professional-looking blog application built using the **Django Web Framework** and styled with **Bootstrap 5**. Users can:

- View blog posts with images
- Read post details and comments
- Submit comments through a form
- Admins can manage blog posts from the Django admin interface

---

## 🛠️ Tech Stack

- **Python 3.8**
- **Django 4.2**
- **Bootstrap 5**
- **SQLite3 (default Django DB)**
- **ChatGPT (for AI-assisted development)**
- **VS Code + Terminal**

---

## 🎯 Features

- 📝 Create, read, update blog posts
- 💬 Add comments to posts
- 🖼️ Upload and display images
- 📱 Mobile responsive (thanks to Bootstrap)
- 🔐 Admin dashboard for content management

---

## 📁 Folder Structure

```bash
genai-django-blog/
├── blog/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── blog/
│           ├── post_list.html
│           ├── post_detail.html
│           └── base.html
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── media/
├── templates/
│   └── base.html
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🖥️ Screenshots

> 📸 Add the following screenshots:
- Blog homepage
- Post detail view
- Admin panel
- Comment form submission
- Folder structure and terminal

---

## 🧠 Prompts Used with ChatGPT

Here are some key prompts that guided this project:

```
1. I want to learn Django with Python, give me a 15-day roadmap with use cases.
2. How can I use Bootstrap to make my Django UI professional?
3. Help me fix this error: django.urls.exceptions.NoReverseMatch...
4. Provide a full HTML template to display blog posts using Bootstrap.
5. Guide me step-by-step to deploy on Render or GitHub.
```

---

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/genai-django-blog.git
cd genai-django-blog

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```

---

## 💡 Lessons Learned

- How Django's MVT (Model-View-Template) architecture works
- Creating and using models, views, templates, and forms
- Working with media (image uploads)
- Styling using Bootstrap
- Using AI prompts to debug and accelerate development
- Writing reusable and readable Django code

---

## 🌐 Deployment (Optional)

You can deploy this project on:
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [PythonAnywhere](https://www.pythonanywhere.com/)

Instructions can be provided if needed.

---

## 🏁 Conclusion

This project represents my journey of learning Django using GenAI tools. Every bug, template, and view was crafted under guided AI assistance. I'm proud to present this as part of my **Moringa AI Capstone**.

---

🕓 Generated on: **August 07, 2025**

Made with 💻 + 🧠 by Newton Manyisa
