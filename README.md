# Asad Mujeeb — Portfolio

A cinematic luxury dark portfolio built with **Flask**. Fully modular, responsive, and deployment-ready.

![Portfolio Preview](static/images/preview.png) <!-- Add a screenshot later -->

## ✨ Features
- Modern cinematic dark design with gold accents
- Fully responsive layout
- Interactive chatbot (powered by Anthropic Claude)
- Project filtering
- Smooth animations and scroll effects
- Contact form
- PDF Resume integration
- Easy to personalize and deploy

## 📁 Project Structure
```bash
portfolio/
├── app.py                  # Main Flask application + all data
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment (Render, Railway, etc.)
├── .env.example            # Environment variables template
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── experience.html
│   ├── certifications.html
│   └── contact.html
└── static/
    ├── css/
    │   ├── main.css
    │   └── home.css
    ├── js/
    │   └── main.js
    └── images/
        ├── Asad_Mujeeb_Resume.pdf
        └── your-photo.jpg
