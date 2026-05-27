import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"\nSUCCESS: {' '.join(command)}")
            print(result.stdout.strip())
        else:
            print(f"\nFAILED: {' '.join(command)}")
            print(result.stderr.strip())

    except FileNotFoundError:
        print(f"\nERROR: command not found: {command[0]}")

commands = [
    ["hostname"],
    ["whoami"],
    ["uptime"],
    ["df", "-h"],
    ["fakecommand123"]
]

for command in commands:
    run_command(command)