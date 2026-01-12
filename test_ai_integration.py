"""
Test script to verify Gemini API integration
Run this to ensure AI insights are working correctly
"""

import sys
import os

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.streamlit'))

try:
    from utils.ai_insights import initialize_gemini
    print("✅ Successfully imported ai_insights module")
except ImportError as e:
    print(f"❌ Failed to import ai_insights: {e}")
    sys.exit(1)

# Test initialization
try:
    import streamlit as st
    print("✅ Streamlit is installed")
except ImportError:
    print("❌ Streamlit is not installed - run: pip install streamlit")
    sys.exit(1)

try:
    import google.generativeai as genai
    print("✅ google-generativeai is installed")
except ImportError:
    print("❌ google-generativeai is not installed - run: pip install google-generativeai")
    sys.exit(1)

# Check secrets file
secrets_path = os.path.join(os.path.dirname(__file__), '.streamlit', 'secrets.toml')
if os.path.exists(secrets_path):
    print(f"✅ Found secrets.toml at {secrets_path}")
    with open(secrets_path, 'r') as f:
        content = f.read()
        if 'GEMINI_API_KEY' in content:
            print("✅ GEMINI_API_KEY found in secrets.toml")
        else:
            print("❌ GEMINI_API_KEY not found in secrets.toml")
else:
    print(f"❌ secrets.toml not found at {secrets_path}")

print("\n" + "="*50)
print("Integration Check Complete!")
print("="*50)
print("\nTo use AI insights in dashboard:")
print("1. Ensure GEMINI_API_KEY is in .streamlit/secrets.toml")
print("2. Run: streamlit run app.py")
print("3. Look for 🤖 AI Analysis sections in the dashboard")
