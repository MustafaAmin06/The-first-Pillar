import sys
import importlib.util
import subprocess

print('executable:', sys.executable)
print('version:', sys.version.splitlines()[0])
print('flet importable:', importlib.util.find_spec('flet') is not None)

# Show pip info if available
try:
    out = subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'flet'], stderr=subprocess.STDOUT, text=True)
    print('\npip show flet:\n' + out)
except subprocess.CalledProcessError as e:
    print('\n`pip show flet` failed:', e)
except FileNotFoundError:
    print('\n`pip` module not available')
