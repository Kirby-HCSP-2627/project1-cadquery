# check_env.py
import sys

if not hasattr(sys, 'real_prefix') and sys.base_prefix == sys.prefix:
    print("❌ ERROR: You are NOT inside the virtual environment!")
    print("Please activate your .venv before running your assignments.")
    sys.exit(1)

try:
    import numpy # Swap with a core package your assignment requires
    print("✅ SUCCESS: Virtual environment is active and dependencies are loaded!")
except ImportError:
    print("❌ ERROR: Dependencies are missing. Did you run 'pip install -r requirements.txt'?")
    sys.exit(1)
