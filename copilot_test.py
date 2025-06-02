import os
import platform
import subprocess

def print_system_uptime():
    if platform.system() == "Windows":
        # Windows: use 'net stats srv' and parse the output
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                print("System Uptime (since):", line.strip().split("Statistics since")[1].strip())
                return
        print("Could not determine uptime on Windows.")
    else:
        # Unix/Linux: use 'uptime' command
        try:
            uptime = subprocess.check_output("uptime -p", shell=True, text=True).strip()
            print("System Uptime:", uptime)
        except Exception as e:
            print("Could not determine uptime:", str(e))

if __name__ == "__main__":
    print_system_uptime()
