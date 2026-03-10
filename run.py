#!/usr/bin/env python3
"""
Skin Cancer Detection Tool - Smart Startup Script
Always finds available port and opens browser automatically
"""

import socket
import subprocess
import webbrowser
import threading
import time
from app import app, db

def find_free_port(start_port=5000):
    """Find a free port starting from start_port"""
    for port in range(start_port, start_port + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return None

def kill_existing_processes():
    """Kill any existing Flask processes"""
    try:
        subprocess.run(['pkill', '-f', 'python.*app.py'], capture_output=True)
        subprocess.run(['pkill', '-f', 'python.*run.py'], capture_output=True)
        subprocess.run(['pkill', '-f', 'Flask'], capture_output=True)
        time.sleep(1)
    except:
        pass

def open_browser_tab(url):
    """Open URL in new browser tab after server starts"""
    def delayed_open():
        time.sleep(2)  # Wait for server to fully start
        webbrowser.open_new_tab(url)
        print(f"🌐 ✨ Opening {url} in your browser...")
    
    threading.Thread(target=delayed_open, daemon=True).start()

if __name__ == '__main__':
    print("🏥 🚀 Smart Startup - Skin Cancer Detection Tool")
    print("=" * 60)
    
    # Clean up any existing processes
    print("🧹 Cleaning up existing processes...")
    kill_existing_processes()
    
    # Find available port
    port = find_free_port(5000)
    if not port:
        print("❌ Could not find available port in range 5000-5100")
        exit(1)
    
    print(f"✅ Found available port: {port}")
    print(f"📍 Application URL: http://localhost:{port}")
    print("🔒 Login/Signup required to access the tool")
    
    # Initialize database
    print("📊 Initializing database...")
    with app.app_context():
        db.create_all()
        print("✅ Database ready!")
    
    # Display enhanced features
    print("✨ Enhanced UI Features:")
    print("  🎆 45+ Advanced animations")
    print("  🌊 Medical particle system")
    print("  🕰️ Glass morphism design")
    print("  📊 Interactive dashboard")
    print("  🌗 Dark/Light theme toggle")
    print("  📱 Mobile responsive")
    print("  🎨 Medical backgrounds")
    
    # Auto-open browser
    url = f"http://localhost:{port}"
    open_browser_tab(url)
    
    print("=" * 60)
    print(f"🚀 Starting server on {url}")
    print("🌐 Browser will open automatically in 2 seconds...")
    print("🔄 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Start the Flask application
    try:
        app.run(debug=True, port=port, host='127.0.0.1', use_reloader=False)
    except KeyboardInterrupt:
        print("\n🛑 ✨ Application stopped by user")
        print("👋 Thanks for using the Skin Cancer Detection Tool!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
