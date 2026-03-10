# app.py - Main Flask application
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os
import base64
import io
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo
import bcrypt

app = Flask(__name__, template_folder='Template')
app.secret_key = 'skin-cancer-detection-tool-2024-secret-key'  # Change this in production

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skin_cancer_detection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

# Analysis History Model
class AnalysisHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    risk_level = db.Column(db.String(50), nullable=False)
    risk_score = db.Column(db.Integer, nullable=False)
    analysis_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('analyses', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[InputRequired(), 
                                             EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

def allowed_file(filename):
    """Check if uploaded file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image_analysis(image_path):
    """Analyze skin lesion image using PIL"""
    try:
        # Load image with PIL
        original_image = Image.open(image_path)
        
        # Convert to RGB if necessary
        if original_image.mode != 'RGB':
            rgb_image = original_image.convert('RGB')
        else:
            rgb_image = original_image.copy()
        
        # Image processing using PIL
        
        # 1. Enhance contrast
        enhancer = ImageEnhance.Contrast(rgb_image)
        contrast_enhanced = enhancer.enhance(1.2)
        
        # 2. Apply Gaussian blur for noise reduction
        blurred = contrast_enhanced.filter(ImageFilter.GaussianBlur(radius=1))
        
        # 3. Convert to numpy array for analysis
        img_array = np.array(blurred)
        
        # 4. Basic color analysis
        avg_color = np.mean(img_array, axis=(0, 1))
        color_std = np.std(img_array, axis=(0, 1))
        
        # 5. Asymmetry detection
        height, width = img_array.shape[:2]
        left_half = img_array[:, :width//2]
        right_half = np.fliplr(img_array[:, width//2:])
        
        # Resize halves to same size for comparison
        if left_half.shape[1] != right_half.shape[1]:
            min_width = min(left_half.shape[1], right_half.shape[1])
            left_half = left_half[:, :min_width]
            right_half = right_half[:, :min_width]
        
        asymmetry_score = np.mean(np.abs(left_half.astype(float) - right_half.astype(float)))
        
        # 6. Color variation analysis
        color_variation = np.mean(color_std)
        
        # 7. Edge detection for border irregularity
        gray = rgb_image.convert('L')
        edges = gray.filter(ImageFilter.FIND_EDGES)
        edge_array = np.array(edges)
        border_irregularity = np.std(edge_array)
        
        # Calculate risk score
        risk_assessment = calculate_risk_score({
            'asymmetry_score': asymmetry_score,
            'color_variation': color_variation,
            'border_irregularity': border_irregularity
        })
        
        return {
            'success': True,
            'image_size': rgb_image.size,
            'avg_color': avg_color.tolist(),
            'color_variation': float(color_variation),
            'asymmetry_score': float(asymmetry_score),
            'border_irregularity': float(border_irregularity),
            'risk_assessment': risk_assessment,
            'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def calculate_risk_score(analysis_data):
    """Calculate risk score based on image analysis"""
    score = 0
    risk_factors = []
    
    # Asymmetry check
    if analysis_data['asymmetry_score'] > 50:
        score += 3
        risk_factors.append("High asymmetry detected")
    elif analysis_data['asymmetry_score'] > 30:
        score += 1
        risk_factors.append("Moderate asymmetry")
    
    # Color variation check
    if analysis_data['color_variation'] > 40:
        score += 2
        risk_factors.append("Significant color variation")
    elif analysis_data['color_variation'] > 25:
        score += 1
        risk_factors.append("Some color variation")
    
    # Border irregularity check
    if analysis_data['border_irregularity'] > 30:
        score += 2
        risk_factors.append("Irregular borders detected")
    elif analysis_data['border_irregularity'] > 20:
        score += 1
        risk_factors.append("Some border irregularity")
    
    # Determine risk level
    if score >= 5:
        risk_level = "HIGH"
        recommendation = "Strongly recommend immediate dermatologist consultation"
        color_class = "danger"
    elif score >= 3:
        risk_level = "MODERATE"
        recommendation = "Consider scheduling dermatologist appointment"
        color_class = "warning"
    else:
        risk_level = "LOW"
        recommendation = "Continue regular self-examinations"
        color_class = "success"
    
    return {
        'score': score,
        'max_score': 7,
        'level': risk_level,
        'factors': risk_factors,
        'recommendation': recommendation,
        'color_class': color_class
    }

@app.route('/')
def index():
    """Landing page - redirects to login for authentication first"""
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/welcome')
@login_required
def welcome():
    """Welcome landing page - shown after successful login"""
    return render_template('welcome.html')

@app.route('/home')
@login_required
def home():
    """Home page for authenticated users"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('welcome'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Registration page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return render_template('signup.html', form=form)
        
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered. Please use a different email.', 'error')
            return render_template('signup.html', form=form)
        
        # Create new user
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )
        new_user.set_password(form.password.data)
        
        db.session.add(new_user)
        db.session.commit()
        
        # Auto-login the new user and redirect to welcome
        login_user(new_user)
        flash('Registration successful! Welcome to the Skin Cancer Detection Tool!', 'success')
        return redirect(url_for('welcome'))
    
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard with analysis history"""
    analyses = AnalysisHistory.query.filter_by(user_id=current_user.id).order_by(AnalysisHistory.analysis_date.desc()).limit(10).all()
    return render_template('dashboard.html', analyses=analyses)

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """Handle file upload and analysis"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('home'))
    
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            # Save uploaded file
            file.save(filepath)
            
            # Analyze the image
            analysis_result = process_image_analysis(filepath)
            
            if analysis_result['success']:
                # Get file info
                file_size = os.path.getsize(filepath) / 1024  # KB
                
                # Save analysis to history
                analysis_history = AnalysisHistory(
                    user_id=current_user.id,
                    filename=filename,
                    risk_level=analysis_result['risk_assessment']['level'],
                    risk_score=analysis_result['risk_assessment']['score']
                )
                db.session.add(analysis_history)
                db.session.commit()
                
                return render_template('results.html', 
                                     filename=filename,
                                     file_size=file_size,
                                     analysis=analysis_result)
            else:
                flash(f'Analysis failed: {analysis_result["error"]}')
                # Clean up file
                if os.path.exists(filepath):
                    os.remove(filepath)
                return redirect(url_for('index'))
                
        except Exception as e:
            flash(f'Upload failed: {str(e)}')
            # Clean up file if it was saved
            if os.path.exists(filepath):
                os.remove(filepath)
            return redirect(url_for('index'))
    
    else:
        flash('Invalid file type. Please upload PNG, JPG, JPEG, GIF, BMP, or TIFF files.')
        return redirect(url_for('index'))

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """API endpoint for image analysis"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'})
    
    file = request.files['file']
    
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file'})
    
    try:
        # Save to temporary location
        filename = f"temp_{uuid.uuid4()}_{secure_filename(file.filename)}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Analyze
        result = process_image_analysis(filepath)
        
        # Clean up temporary file
        os.remove(filepath)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/diagnose')
@login_required
def diagnose():
    """Diagnose page - main analysis tool"""
    return render_template('index.html')

@app.route('/cancer-types')
def cancer_types():
    """Cancer Types information page"""
    return render_template('cancer_types.html')

@app.route('/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('profile.html', user=current_user)

@app.route('/settings')
@login_required
def settings():
    """User settings page"""
    return render_template('settings.html')

@app.route('/history')
@login_required
def history():
    """User diagnosis history"""
    analyses = AnalysisHistory.query.filter_by(user_id=current_user.id).order_by(AnalysisHistory.analysis_date.desc()).all()
    return render_template('history.html', analyses=analyses)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    flash('Page not found.')
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    flash('An internal server error occurred. Please try again.')
    return redirect(url_for('index'))

@app.errorhandler(413)
def file_too_large(e):
    """Handle file too large errors"""
    flash('File too large. Please upload a file smaller than 16MB.')
    return redirect(url_for('index'))

def find_free_port(start_port=5000):
    """Find a free port starting from start_port"""
    import socket
    import subprocess
    
    for port in range(start_port, start_port + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(('127.0.0.1', port)) != 0:
                # Port is available
                return port
    return None

def kill_existing_flask_processes():
    """Kill any existing Flask processes to free up ports"""
    import subprocess
    try:
        # Kill any existing Flask processes
        subprocess.run(['pkill', '-f', 'python.*app.py'], capture_output=True)
        subprocess.run(['pkill', '-f', 'Flask'], capture_output=True)
        import time
        time.sleep(1)
    except:
        pass

def open_browser(url):
    """Open the URL in a new browser tab"""
    import webbrowser
    import threading
    import time
    
    def delayed_open():
        time.sleep(1.5)  # Wait for server to start
        webbrowser.open_new_tab(url)
        print(f"🌐 Opening {url} in your browser...")
    
    # Open browser in a separate thread
    threading.Thread(target=delayed_open, daemon=True).start()

if __name__ == '__main__':
    print("🏥 Starting Skin Cancer Detection Tool...")
    print("🧹 Cleaning up any existing processes...")
    
    # Kill existing processes
    kill_existing_flask_processes()
    
    # Find available port
    port = find_free_port(5000)
    if not port:
        print("❌ Could not find available port")
        exit(1)
    
    print(f"✅ Found available port: {port}")
    print(f"📍 URL: http://localhost:{port}")
    
    # Initialize database
    with app.app_context():
        db.create_all()
        print("✅ Database initialized!")
    
    print("🎨 Enhanced UI Features Loaded:")
    print("  ✨ Advanced animations & effects")
    print("  🌊 Medical particle system")
    print("  🎨 Glass morphism design")
    print("  📊 Interactive dashboard")
    print("  🌗 Dark/Light theme toggle")
    print("  📱 Mobile responsive design")
    
    # Open browser automatically
    url = f"http://localhost:{port}"
    open_browser(url)
    
    print(f"🚀 Server starting on {url}")
    print("🔄 Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        app.run(debug=True, port=port, host='127.0.0.1', use_reloader=False)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
