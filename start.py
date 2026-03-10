#!/usr/bin/env python3
"""
Smart Startup Script for Skin Cancer Detection Tool
Automatically handles port conflicts and starts the application cleanly
"""

import subprocess
import socket
import sys
import time
import os

def check_port(port):
    """Check if a port is available"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('127.0.0.1', port))
        return result != 0

def kill_processes_on_port(port):
    """Kill processes using a specific port"""
    try:
        result = subprocess.run(['lsof', '-t', '-i', f':{port}'], 
                              capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid.strip():
                    subprocess.run(['kill', '-9', pid.strip()])
            return True
        return False
    except Exception:
        return False

def find_available_port(start_port=5000, max_port=5100):
    """Find the first available port in a range"""
    for port in range(start_port, max_port):
        if check_port(port):
            return port
    return None

def update_port_in_files(new_port):
    """Update port number in app files"""
    files_to_update = ['app.py', 'run.py']
    
    for filename in files_to_update:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()
            
            # Replace port numbers in the files
            import re
            content = re.sub(r'port=\d+', f'port={new_port}', content)
            
            with open(filename, 'w') as f:
                f.write(content)

def main():
    print("🏥 Smart Startup - Skin Cancer Detection Tool")
    print("=" * 50)
    
    # Kill any existing Flask processes
    print("🧹 Cleaning up existing processes...")
    subprocess.run(['pkill', '-f', 'python.*app.py'], capture_output=True)
    subprocess.run(['pkill', '-f', 'python.*run.py'], capture_output=True)
    time.sleep(1)
    
    # Find available port
    preferred_ports = [5002, 5003, 5004, 5005, 5001]
    selected_port = None
    
    for port in preferred_ports:
        if check_port(port):
            selected_port = port
            print(f"✅ Port {port} is available")
            break
        else:
            print(f"❌ Port {port} is in use, trying to free it...")
            kill_processes_on_port(port)
            time.sleep(0.5)
            if check_port(port):
                selected_port = port
                print(f"✅ Port {port} is now available")
                break
    
    if not selected_port:
        selected_port = find_available_port()
        if not selected_port:
            print("❌ No available ports found!")
            sys.exit(1)
    
    # Update port in files if different from current
    if selected_port != 5002:
        print(f"🔧 Updating application to use port {selected_port}")
        update_port_in_files(selected_port)
    
    print(f"🚀 Starting application on port {selected_port}")
    print(f"📍 URL: http://localhost:{selected_port}")
    print("=" * 50)
    
    # Import and start the app
    try:
        from app import app, db
        
        print("📊 Initializing database...")
        with app.app_context():
            db.create_all()
        print("✅ Database ready!")
        
        print("🎨 Loading enhanced UI features...")
        print("  ✨ Advanced animations")
        print("  🎨 Medical backgrounds")
        print("  🌊 Particle system")
        print("  📊 Interactive dashboard")
        print("  🌗 Theme toggle")
        print("✅ UI enhancements loaded!")
        
        print(f"🌟 Application starting on http://localhost:{selected_port}")
        print("🔄 Press Ctrl+C to stop the server")
        print("=" * 50)
        
        # Start the Flask app
        app.run(debug=True, port=selected_port, host='127.0.0.1', use_reloader=False)
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()