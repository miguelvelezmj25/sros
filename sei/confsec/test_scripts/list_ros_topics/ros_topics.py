import subprocess

def main():
    output = subprocess.check_output(["ros2", "topic", "list"])
    print(output)

if __name__ == '__main__':
    main()