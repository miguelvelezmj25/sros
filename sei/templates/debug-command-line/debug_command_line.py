import <debugging_module>
import subprocess

try:
    <debugging_module>.<debugging_function>
    raise AssertionError("If no error is raise, the system is not configured securely")
except subprocess.CalledProcessError:
    print("If a subprocess.CalledProcessError is raised, the system is configured securely")
