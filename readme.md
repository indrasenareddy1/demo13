copilot_test.py
What does it do?
copilot_test.py is a simple script that prints the system's uptime (how long the system has been running):

On Windows, it parses the output of the net stats srv command to display when the system was last started.
On Unix/Linux/Mac, it uses the uptime -p command to print the system's uptime in a readable format.
How to run
Make sure you have Python 3 installed on your system.
Open a terminal (Command Prompt on Windows, or Terminal on Unix/Linux/Mac).
Navigate to the directory containing copilot_test.py.
Run the script with:
bash
python copilot_test.py
You will see output indicating how long your system has been running.
