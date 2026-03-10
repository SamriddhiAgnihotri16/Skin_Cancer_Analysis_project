#!/usr/bin/env python3
"""
🚀 ONE-CLICK LAUNCHER
Skin Cancer Detection Tool
Always works - Finds free port & opens browser automatically!
"""

print("🏥 🚀 LAUNCHING SKIN CANCER DETECTION TOOL")
print("🔧 Auto-port detection & browser opening enabled")
print("=" * 60)

# Import and run the enhanced app
try:
    exec(open('app.py').read())
except Exception as e:
    print(f"❌ Launch error: {e}")
    print("📝 Make sure you're in the right directory!")
    input("Press Enter to exit...")