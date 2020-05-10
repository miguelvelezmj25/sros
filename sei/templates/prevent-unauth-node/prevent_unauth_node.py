import <node_module>

try:
    <node_module>.<run_function>
    raise AssertionError("If no error is raised, the system is not configured securely")
except RuntimeError:
    print("If a RuntimeError is raised, the system is configured securely")
