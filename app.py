
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from __init__ import create_app
except ImportError:
    # If relative import fails, try importing as a module
    import __init__
    create_app = __init__.create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
