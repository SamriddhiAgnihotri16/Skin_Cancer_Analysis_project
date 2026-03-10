# 🏥 Skin Cancer Detection Tool

A comprehensive web-based application for skin cancer detection using advanced image processing techniques and machine learning. This tool provides preliminary screening results with a professional medical-themed interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple.svg)

## ✨ Key Features

### 🔐 **User Authentication System**
- **Secure Login/Signup**: Professional medical-themed authentication pages
- **Password Security**: BCrypt hashing with strength validation
- **Session Management**: Secure user sessions with Flask-Login
- **User Dashboard**: Personal analysis history and statistics

### 🔬 **Advanced Image Analysis**
- **Multi-Factor Analysis**: Asymmetry, Color Variation, Border Irregularity
- **ABCDE Rule Implementation**: Following dermatological standards
- **Risk Assessment**: Comprehensive scoring system (LOW/MODERATE/HIGH)
- **Real-time Processing**: Instant analysis with PIL and NumPy

### 🎨 **Medical-Themed UI/UX**
- **Professional Design**: Medical-grade interface with appropriate color schemes
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Interactive Elements**: Drag-and-drop upload, progress indicators
- **Accessibility**: Screen reader friendly with proper ARIA labels

### 📊 **Dashboard & Analytics**
- **Analysis History**: Complete record of all performed analyses
- **Risk Statistics**: Visual representation of risk assessments
- **Personal Profile**: User account management
- **Quick Actions**: Fast access to new analysis and past results

### 🛡️ **Medical Compliance**
- **Disclaimer Integration**: Clear medical disclaimers throughout
- **Professional Standards**: Following medical software guidelines
- **Data Privacy**: Secure storage of user data and analysis results

## 🚀 Quick Start

### Prerequisites
```bash
# Check Python version (3.7+ required)
python --version

# Check pip
pip --version
```

### Installation

1. **Clone or download** the project to your local machine

2. **Install Dependencies** (if not already installed):
   ```bash
   pip install Flask Flask-Login Flask-SQLAlchemy Flask-WTF WTForms bcrypt Pillow numpy
   ```

3. **Run the Application**:
   ```bash
   # Option 1: Use the startup script
   python run.py
   
   # Option 2: Run directly
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5002
   ```

## 💡 How to Use

### 1. **Create Account**
- Click "Sign Up" on the landing page
- Enter your email, username, and secure password
- Complete registration and log in

### 2. **Upload Skin Image**
- Go to the Analysis page
- Click the upload area or drag & drop an image
- Supported formats: PNG, JPG, JPEG, GIF, BMP, TIFF
- Maximum file size: 16MB

### 3. **Review Results**
- Get instant analysis with risk assessment
- View technical details and recommendations
- Check your dashboard for analysis history

### 4. **Professional Consultation**
- **Always consult a dermatologist** for proper diagnosis
- Use results as screening tool only
- Schedule medical appointment for concerning results

## 🛠️ Technical Stack

### Backend
- **Flask 3.1.0**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **WTForms**: Form validation
- **PIL/Pillow**: Image processing
- **NumPy**: Numerical computations
- **BCrypt**: Password hashing

### Frontend
- **Bootstrap 5.1.3**: Responsive UI framework
- **Font Awesome 6.0**: Medical icons and UI elements
- **Custom CSS**: Medical-themed styling
- **JavaScript**: Interactive features and AJAX

### Database
- **SQLite**: Local database storage
- **User Management**: Secure user accounts
- **Analysis History**: Complete analysis records

## 📁 Project Structure

```
DEMO1/
├── app.py                 # Main Flask application
├── run.py                 # Startup script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── Template/             # Jinja2 templates
│   ├── base.html         # Base template with medical theme
│   ├── login.html        # Login page
│   ├── signup.html       # Registration page
│   ├── index.html        # Main analysis page
│   ├── dashboard.html    # User dashboard
│   ├── results.html      # Analysis results
│   └── about.html        # About page
├── static/               # Static files
│   └── uploads/          # Uploaded images
└── instance/             # Database files
    └── skin_cancer_detection.db
```

## 🔬 Analysis Algorithm

The tool implements a comprehensive analysis based on the **ABCDE rule** of dermatology:

### **A - Asymmetry**
- Compares left and right halves of the lesion
- Calculates asymmetry score using image comparison
- Higher scores indicate greater asymmetry

### **B - Border Irregularity**
- Uses edge detection algorithms
- Analyzes border smoothness and regularity
- Detects irregular or scalloped borders

### **C - Color Variation**
- Examines color distribution across the lesion
- Analyzes RGB color variations
- Detects multiple colors within single lesion

### **Risk Scoring System**
- **LOW (0-2 points)**: Continue regular self-examinations
- **MODERATE (3-4 points)**: Consider dermatologist appointment
- **HIGH (5+ points)**: Strongly recommend immediate consultation

## ⚠️ Medical Disclaimer

> **IMPORTANT**: This tool is for educational and screening purposes only.
> - NOT a substitute for professional medical diagnosis
> - Cannot detect all types of skin cancer
> - Always consult a qualified dermatologist for proper evaluation
> - Early detection and professional medical care are crucial
> - If you have concerns about skin changes, seek medical attention immediately

## 🔒 Security Features

- **Password Hashing**: BCrypt with salt
- **Session Security**: Secure session management
- **Input Validation**: Server-side validation for all forms
- **File Upload Security**: Type and size validation
- **SQL Injection Protection**: SQLAlchemy ORM
- **XSS Protection**: Template auto-escaping

## 🎯 Future Enhancements

- [ ] AI/ML model integration for improved accuracy
- [ ] Multi-language support
- [ ] Export analysis reports (PDF)
- [ ] Integration with medical databases
- [ ] Advanced user roles (patients, doctors)
- [ ] Telemedicine consultation features
- [ ] Mobile app development

## 📞 Support

For issues, questions, or contributions:
1. Check the console for error messages
2. Ensure all dependencies are installed
3. Verify port 5001 is available
4. Check file permissions for uploads directory

## 📄 License

This project is for educational purposes. Please ensure compliance with medical software regulations if used in clinical settings.

---

**Made with ❤️ for advancing dermatological screening and early cancer detection**

# Skin Cancer Detection Tool

A web-based skin cancer detection tool using advanced image processing techniques powered by Python's PIL (Pillow) library to analyze skin lesions and provide preliminary screening results.

## ⚠️ Medical Disclaimer

**This tool is for educational and screening purposes only. It is not a substitute for professional medical diagnosis. Always consult a dermatologist for proper evaluation and diagnosis of skin concerns.**

## Features

- **Image Analysis**: Advanced image processing using PIL/Pillow
- **Risk Assessment**: ABCDE rule-based analysis (Asymmetry, Border, Color, Diameter, Evolution)
- **Technical Metrics**: Detailed analysis including asymmetry score, color variation, and border irregularity
- **User-friendly Interface**: Modern Bootstrap-based web interface
- **Drag & Drop Upload**: Easy file upload with preview
- **Multiple Formats**: Supports PNG, JPG, JPEG, GIF, BMP, TIFF

## Analysis Features

The tool examines several key characteristics:

- **Asymmetry Analysis**: Compares left and right halves of the lesion
- **Color Variation**: Analyzes color distribution and variation
- **Border Irregularity**: Uses edge detection to assess border characteristics
- **Color Enhancement**: Improves image contrast for better analysis

## Technology Stack

- **Backend**: Flask (Python)
- **Image Processing**: PIL/Pillow
- **Numerical Computing**: NumPy
- **Frontend**: Bootstrap 5, Font Awesome
- **File Handling**: Werkzeug

## Installation

1. **Clone or download the project**
   ```bash
   cd "MINI PROJECT"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

## Requirements

- Python 3.7+
- Flask 2.3.3
- Pillow 10.0.1
- NumPy 1.24.3
- Werkzeug 2.3.7

## Usage

1. **Upload Image**: Click the upload area or drag and drop an image file
2. **Supported Formats**: PNG, JPG, JPEG, GIF, BMP, TIFF (max 16MB)
3. **Analysis**: The tool will automatically process the image
4. **Results**: Review the risk assessment and technical analysis

### Tips for Best Results

- Use good lighting
- Focus clearly on the lesion
- Avoid shadows and reflections
- Include some surrounding skin for context

## Project Structure

```
MINI PROJECT/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── Template/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   └── results.html      # Results page
└── static/
    └── uploads/          # Uploaded images directory
```

## API Endpoints

- `GET /` - Home page
- `POST /upload` - File upload and analysis
- `POST /api/analyze` - API endpoint for analysis
- `GET /about` - About page

## Risk Assessment

The tool provides three risk levels:

- **LOW**: Score 0-2, Continue regular self-examinations
- **MODERATE**: Score 3-4, Consider scheduling dermatologist appointment
- **HIGH**: Score 5+, Strongly recommend immediate dermatologist consultation

## Contributing

This is an educational project. For improvements or suggestions, please ensure all changes maintain the educational nature and medical disclaimers.

## License

This project is for educational purposes only.

## Contact

For questions about this educational tool, please consult the documentation or relevant educational resources.

---

**Remember**: Early detection and professional medical care are crucial. If you have concerns about any skin changes, seek medical attention immediately.# SKIN-CANCER
