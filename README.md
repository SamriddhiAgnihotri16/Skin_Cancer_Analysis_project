# 🏥 Skin Cancer Detection Tool

A modern **Flask-based web application** for preliminary **skin cancer risk assessment** using image processing techniques based on the **ABCDE Rule**. The application provides secure user authentication, an interactive dashboard, analysis history, and a professional medical-themed interface. It is designed for **educational and research purposes only** and is **not a substitute for professional medical diagnosis**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-3.1.0-black?logo=flask">
  <img src="https://img.shields.io/badge/Bootstrap-5.1.3-purple?logo=bootstrap">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite">
  <img src="https://img.shields.io/badge/Render-Deployed-success?logo=render">
</p>

<p align="center">
  <a href="https://skin-cancer-analysis-project.onrender.com">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Click%20Here-success?style=for-the-badge" alt="Live Demo">
  </a>
</p>

---

## 🌐 Live Demo

**🔗 Website:**  
https://skin-cancer-analysis-project.onrender.com

> **Note:** This application is deployed on Render's free tier. The first request may take **30–60 seconds** while the server wakes up.

---

## ✨ Features

### 🔐 Authentication & Security

- Secure User Registration & Login
- BCrypt Password Hashing
- Session-Based Authentication
- Protected User Dashboard
- Secure User Data Management

### 🔬 Skin Lesion Analysis

- Upload Skin Lesion Images
- Image Processing using Pillow (PIL)
- Preliminary Skin Cancer Risk Assessment
- Fast Image Analysis

### 📊 ABCDE Risk Assessment

- **A** – Asymmetry Analysis
- **B** – Border Irregularity Detection
- **C** – Color Variation Analysis
- **D** – Diameter Evaluation
- **E** – Evolution-Based Risk Assessment
- Risk Classification: **Low • Moderate • High**

### 📈 Dashboard

- User Analysis History
- Risk Statistics
- User Profile
- Previous Report Access

### 🎨 User Experience

- Professional Medical-Themed UI
- Responsive Design
- Interactive Animations
- Drag & Drop Image Upload
- Smooth Loading Effects
- Mobile Friendly

### 🛡️ Security

- BCrypt Password Encryption
- File Upload Validation
- SQLAlchemy ORM
- Input Validation
- Secure Session Management

---

## 🛠️ Tech Stack

### Backend

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- WTForms

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Libraries

- Pillow (PIL)
- NumPy
- BCrypt

### Database

- SQLite

### Deployment

- Render

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/SamriddhiAgnihotri16/Skin_Cancer_Analysis_project.git
```

Go to the project directory:

```bash
cd Skin_Cancer_Analysis_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Open your browser:

```
http://localhost:5000
```

---

## 📁 Project Structure

```
Skin_Cancer_Analysis_project/
│
├── app.py
├── run.py
├── requirements.txt
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
│   └── images/
├── templates/
├── instance/
├── models/
├── README.md
└── LICENSE
```

---


## 📌 Future Enhancements

- 🤖 Deep Learning (CNN) Model Integration
- 📄 PDF Report Generation
- 📧 Email Notifications
- ☁️ Cloud Image Storage
- 🌐 Multi-language Support
- 👨‍⚕️ Doctor Portal
- 📱 Progressive Web App (PWA)

---

## ⚠️ Disclaimer

This project is developed **only for educational and research purposes**.

It **does not provide medical advice** and **must not be used as a substitute for professional diagnosis or treatment**. Always consult a qualified dermatologist or healthcare professional regarding any skin-related concerns.

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Contributions, suggestions, and feedback are always welcome.

---

## 👩‍💻 Author

**Samriddhi Agnihotri**

- GitHub: https://github.com/SamriddhiAgnihotri16
- LinkedIn: https://www.linkedin.com/in/samriddhi-agnihotri-6168a3291

---

Made with ❤️ using Python, Flask, Bootstrap, and Render.