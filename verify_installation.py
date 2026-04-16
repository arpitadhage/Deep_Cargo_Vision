#!/usr/bin/env python3
"""
Quick Verification Script for EfficientNet Pipeline Integration
Run this after installation to verify all components are working.
"""

import os
import sys
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_dir))

def check_file_exists(path: Path, name: str) -> bool:
    """Check if a required file exists."""
    if path.exists():
        print(f"✅ {name}: {path}")
        return True
    else:
        print(f"❌ {name} MISSING: {path}")
        return False

def check_imports() -> bool:
    """Verify all required imports work."""
    print("\n--- Checking Python Imports ---")
    imports = {
        "torch": "torch",
        "torchvision": "torchvision",
        "opencv": "cv2",
        "PIL": "PIL",
        "fastapi": "fastapi",
        "ultralytics": "ultralytics",
    }
    
    all_good = True
    for display_name, module_name in imports.items():
        try:
            __import__(module_name)
            print(f"✅ {display_name}")
        except ImportError as e:
            print(f"❌ {display_name}: {e}")
            all_good = False
    
    return all_good

def check_local_modules() -> bool:
    """Verify local backend modules."""
    print("\n--- Checking Local Modules ---")
    modules_to_check = [
        "classifier_model",
        "xray_filters",
        "risk_scoring",
        "inference_pipeline",
    ]
    
    all_good = True
    for module_name in modules_to_check:
        try:
            __import__(module_name)
            print(f"✅ {module_name}")
        except Exception as e:
            print(f"❌ {module_name}: {e}")
            all_good = False
    
    return all_good

def check_model_files() -> bool:
    """Verify model files exist."""
    print("\n--- Checking Model Files ---")
    base_dir = backend_dir.parent
    
    checks = [
        (base_dir / "model" / "yolo-baseline" / "best.pt", "YOLO-baseline"),
        (base_dir / "model" / "efficent-net" / "yolo_best.pt", "EfficientNet YOLO"),
        (base_dir / "model" / "efficent-net" / "classifier_best.pth", "EfficientNet Classifier"),
    ]
    
    all_good = True
    for path, name in checks:
        all_good &= check_file_exists(path, name)
    
    return all_good

def check_api_structure() -> bool:
    """Verify API endpoints are defined."""
    print("\n--- Checking API Structure ---")
    try:
        from main import app
        routes = [r.path for r in app.routes]
        
        required_endpoints = [
            "/predict",
            "/predict-batch",
            "/predict-efficientnet",
            "/predict-batch-efficientnet",
            "/health",
        ]
        
        all_good = True
        for endpoint in required_endpoints:
            if endpoint in routes:
                print(f"✅ {endpoint}")
            else:
                print(f"❌ {endpoint} MISSING")
                all_good = False
        
        return all_good
    except Exception as e:
        print(f"❌ Failed to load app: {e}")
        return False

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("EfficientNet Pipeline Integration — Verification Script")
    print("=" * 60)
    
    results = {
        "Imports": check_imports(),
        "Local Modules": check_local_modules(),
        "Model Files": check_model_files(),
        "API Structure": check_api_structure(),
    }
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for check_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{check_name}: {status}")
    
    if all(results.values()):
        print("\n✅ All checks passed! Ready to start the server.")
        print("\nStart server with:")
        print("  cd backend/")
        print("  python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000")
        return 0
    else:
        print("\n❌ Some checks failed. Fix the issues above before starting.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
