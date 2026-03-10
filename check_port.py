#!/usr/bin/env python3
"""
Port Checker Utility for Skin Cancer Detection Tool
Helps find available ports and kill processes if needed
"""

import socket
import subprocess
import sys

def check_port(port):
    """Check if a port is available"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('127.0.0.1', port))
        return result != 0

def find_processes_on_port(port):
    """Find processes using a specific port"""
    try:
        result = subprocess.run(['lsof', '-i', f':{port}'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        return None
    except Exception as e:
        print(f"Error checking port: {e}")
        return None

def kill_processes_on_port(port):
    """Kill processes using a specific port"""
    try:
        # Get PIDs using the port
        result = subprocess.run(['lsof', '-t', '-i', f':{port}'], 
                              capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid:
                    subprocess.run(['kill', '-9', pid])
                    print(f"✅ Killed process {pid}")
            return True
        return False
    except Exception as e:
        print(f"❌ Error killing processes: {e}")
        return False

def find_available_port(start_port=5000, max_port=5100):
    """Find the first available port in a range"""
    for port in range(start_port, max_port):
        if check_port(port):
            return port
    return None

def main():
    preferred_ports = [5002, 5001, 5003, 5004, 5005]
    
    print("🔍 Checking ports for Skin Cancer Detection Tool...")
    print("=" * 50)
    
    for port in preferred_ports:
        if check_port(port):
            print(f"✅ Port {port} is available")
            return port
        else:
            print(f"❌ Port {port} is in use")
            processes = find_processes_on_port(port)
            if processes:
                print(f"   Processes using port {port}:")
                print(f"   {processes.strip()}")
                
                response = input(f"   Kill processes on port {port}? (y/n): ")
                if response.lower() == 'y':
                    if kill_processes_on_port(port):
                        if check_port(port):
                            print(f"✅ Port {port} is now available")
                            return port
    
    # Find any available port
    available_port = find_available_port()
    if available_port:
        print(f"🔍 Found available port: {available_port}")
        return available_port
    else:
        print("❌ No available ports found in range 5000-5100")
        return None

if __name__ == "__main__":
    port = main()
    if port:
        print(f"\n🚀 Recommended port: {port}")
        print(f"📍 Your app URL will be: http://localhost:{port}")
    else:
        print("\n❌ Could not find an available port")
        sys.exit(1)