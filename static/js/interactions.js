// ================================
// ADVANCED INTERACTIONS & EFFECTS
// Skin Cancer Detection Tool
// ================================

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all interactive elements
    initializeParticleSystem();
    initializeCounterAnimations();
    initializeCardEffects();
    initializeFormEffects();
    initializeMedicalIcons();
    initializeLoadingEffects();
    initializePageTransitions();
    
    // Particle System
    function initializeParticleSystem() {
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles-container';
        document.body.appendChild(particlesContainer);
        
        // Create floating medical particles
        for (let i = 0; i < 15; i++) {
            createParticle(particlesContainer, i);
        }
    }
    
    function createParticle(container, index) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Random positioning and size
        const size = Math.random() * 4 + 2; // 2-6px
        const left = Math.random() * 100; // 0-100%
        const delay = Math.random() * 6; // 0-6s delay
        
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        particle.style.left = left + '%';
        particle.style.animationDelay = delay + 's';
        particle.style.animationDuration = (Math.random() * 4 + 8) + 's'; // 8-12s
        
        container.appendChild(particle);
    }
    
    // Animated Counter for Statistics
    function initializeCounterAnimations() {
        const counters = document.querySelectorAll('.counter-animated');
        
        const observerOptions = {
            threshold: 0.5,
            rootMargin: '0px'
        };
        
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        counters.forEach(counter => {
            observer.observe(counter);
        });
    }
    
    function animateCounter(element) {
        const target = parseInt(element.innerText) || 0;
        const duration = 2000; // 2 seconds
        const start = performance.now();
        
        function updateCounter(currentTime) {
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            
            // Easing function for smooth animation
            const easeOutCubic = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(easeOutCubic * target);
            
            element.innerText = current;
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.innerText = target;
            }
        }
        
        requestAnimationFrame(updateCounter);
    }
    
    // Interactive Card Effects
    function initializeCardEffects() {
        const cards = document.querySelectorAll('.card, .interactive-card');
        
        cards.forEach(card => {
            // Add hover sound effect (optional)
            card.addEventListener('mouseenter', function() {
                this.classList.add('card-hover-effect');
            });
            
            card.addEventListener('mouseleave', function() {
                this.classList.remove('card-hover-effect');
            });
            
            // Add ripple effect on click
            card.addEventListener('click', function(e) {
                createRippleEffect(e, this);
            });
        });
    }
    
    function createRippleEffect(event, element) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.className = 'ripple-effect';
        
        // Add ripple styles
        ripple.style.position = 'absolute';
        ripple.style.borderRadius = '50%';
        ripple.style.backgroundColor = 'rgba(255, 255, 255, 0.3)';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple-animation 0.6s linear';
        ripple.style.pointerEvents = 'none';
        
        element.appendChild(ripple);
        
        // Remove ripple after animation
        setTimeout(() => {
            ripple.remove();
        }, 600);
    }
    
    // Add ripple animation keyframes
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Enhanced Form Effects
    function initializeFormEffects() {
        const formInputs = document.querySelectorAll('input, textarea, select');
        
        formInputs.forEach(input => {
            // Focus effects
            input.addEventListener('focus', function() {
                this.parentNode.classList.add('form-field-focused');
                createFocusGlow(this);
            });
            
            input.addEventListener('blur', function() {
                this.parentNode.classList.remove('form-field-focused');
                removeFocusGlow(this);
            });
            
            // Input validation feedback
            input.addEventListener('input', function() {
                validateInputRealTime(this);
            });
        });
        
        // Submit button enhancement
        const submitButtons = document.querySelectorAll('input[type="submit"], button[type="submit"]');
        submitButtons.forEach(button => {
            button.classList.add('btn-animated');
            button.innerHTML = '<span>' + button.innerHTML + '</span>';
        });
    }
    
    function createFocusGlow(element) {
        const glow = document.createElement('div');
        glow.className = 'input-glow';
        glow.style.position = 'absolute';
        glow.style.top = '0';
        glow.style.left = '0';
        glow.style.right = '0';
        glow.style.bottom = '0';
        glow.style.borderRadius = '10px';
        glow.style.boxShadow = '0 0 20px rgba(52, 152, 219, 0.5)';
        glow.style.pointerEvents = 'none';
        glow.style.zIndex = '-1';
        
        element.parentNode.style.position = 'relative';
        element.parentNode.appendChild(glow);
    }
    
    function removeFocusGlow(element) {
        const glow = element.parentNode.querySelector('.input-glow');
        if (glow) {
            glow.remove();
        }
    }
    
    function validateInputRealTime(input) {
        const isValid = input.checkValidity();
        
        if (isValid) {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        } else if (input.value.length > 0) {
            input.classList.remove('is-valid');
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-valid', 'is-invalid');
        }
    }
    
    // Medical Icons Animation
    function initializeMedicalIcons() {
        const medicalIcons = document.querySelectorAll('.fas, .fab');
        
        medicalIcons.forEach(icon => {
            icon.classList.add('medical-icon-animated');
            
            // Special animations for specific icons
            if (icon.classList.contains('fa-stethoscope')) {
                icon.classList.add('stethoscope-animated');
            }
            if (icon.classList.contains('fa-plus') || icon.classList.contains('fa-cross')) {
                icon.classList.add('medical-cross-animated');
            }
        });
    }
    
    // Loading Effects
    function initializeLoadingEffects() {
        // Enhanced loading spinner
        const loadingSpinners = document.querySelectorAll('.spinner-border');
        loadingSpinners.forEach(spinner => {
            spinner.classList.add('medical-spinner');
        });
        
        // Progress bar animations
        const progressBars = document.querySelectorAll('.progress-bar');
        progressBars.forEach(bar => {
            bar.parentNode.classList.add('progress-animated');
        });
        
        // Loading overlay for file uploads
        const fileInputs = document.querySelectorAll('input[type="file"]');
        fileInputs.forEach(input => {
            input.addEventListener('change', function() {
                showLoadingOverlay();
            });
        });
    }
    
    function showLoadingOverlay() {
        const overlay = document.createElement('div');
        overlay.id = 'loading-overlay';
        overlay.innerHTML = `
            <div class="loading-content">
                <div class="medical-spinner"></div>
                <p class="mt-3">Processing your medical image...</p>
                <p class="text-muted small">Please wait while we analyze the skin lesion</p>
            </div>
        `;
        
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(44, 62, 80, 0.9);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            color: white;
            text-align: center;
        `;
        
        document.body.appendChild(overlay);
        
        // Remove overlay after form submission (handled by backend)
        setTimeout(() => {
            if (document.getElementById('loading-overlay')) {
                overlay.remove();
            }
        }, 10000); // 10 seconds timeout
    }
    
    // Page Transitions
    function initializePageTransitions() {
        // Add entrance animations to page elements
        const pageElements = document.querySelectorAll('.card, .alert, .nav-item');
        
        pageElements.forEach((element, index) => {
            element.classList.add('page-enter');
            if (index % 2 === 1) {
                element.classList.add('page-enter-delay');
            }
            if (index % 3 === 2) {
                element.classList.add('page-enter-delay-2');
            }
        });
    }
    
    // Upload Area Enhancements
    function enhanceUploadArea() {
        const uploadAreas = document.querySelectorAll('.upload-area');
        
        uploadAreas.forEach(area => {
            area.classList.add('upload-enhanced');
            
            // File drag and drop visual feedback
            area.addEventListener('dragenter', function(e) {
                e.preventDefault();
                this.classList.add('drag-over');
                this.style.transform = 'scale(1.05)';
            });
            
            area.addEventListener('dragleave', function(e) {
                e.preventDefault();
                this.classList.remove('drag-over');
                this.style.transform = 'scale(1)';
            });
            
            area.addEventListener('drop', function(e) {
                e.preventDefault();
                this.classList.remove('drag-over');
                this.style.transform = 'scale(1)';
                
                // Add success animation
                this.style.animation = 'bounceIn 0.6s ease-out';
                setTimeout(() => {
                    this.style.animation = '';
                }, 600);
            });
        });
    }
    
    // Call upload area enhancement
    enhanceUploadArea();
    
    // Theme toggle functionality removed - now handled in dropdown menu
    
    // Medical Sound Effects (optional)
    function createSoundEffects() {
        // Create audio context for subtle medical sounds
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        function playTone(frequency, duration, type = 'sine') {
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime);
            oscillator.type = type;
            
            gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + duration);
            
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + duration);
        }
        
        // Add subtle sounds to interactions
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('btn')) {
                playTone(800, 0.1);
            }
        });
    }
    
    // Initialize sound effects (uncomment if desired)
    // createSoundEffects();
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Medical typing effect for text elements
    function typeWriter(element, text, speed = 50) {
        let i = 0;
        element.innerHTML = '';
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }
    
    // Apply typing effect to specific elements
    const typingElements = document.querySelectorAll('.typing-effect');
    typingElements.forEach(element => {
        const text = element.innerText;
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    typeWriter(entry.target, text);
                    observer.unobserve(entry.target);
                }
            });
        });
        observer.observe(element);
    });
    
    console.log('🏥 Medical UI Enhancements Loaded Successfully!');
});

// Dark theme styles
const darkThemeStyles = `
.dark-theme {
    --medical-primary: #ff6b6b;
    --medical-secondary: #4ecdc4;
    --medical-success: #45b7d1;
    --medical-warning: #f9ca24;
    --medical-danger: #ff6b6b;
    --medical-light: #2c3e50;
    --medical-dark: #34495e;
}

.dark-theme body {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #1e3c72 100%);
    color: #ecf0f1;
}

.dark-theme .card {
    background: rgba(52, 73, 94, 0.9);
    color: #ecf0f1;
}

.dark-theme .navbar {
    background: linear-gradient(90deg, rgba(52, 73, 94, 0.95) 0%, rgba(231, 76, 60, 0.95) 100%) !important;
}
`;

// Add dark theme styles to document
const darkStyleSheet = document.createElement('style');
darkStyleSheet.textContent = darkThemeStyles;
document.head.appendChild(darkStyleSheet);