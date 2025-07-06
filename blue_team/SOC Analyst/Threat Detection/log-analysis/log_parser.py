# i am importing the pthon built in 're' module so we can use regular expressions
# regex helps to search ip adress username and more.
import re
#so now i am gonna make a function names ' detect_failed_logins'
# we will take filepath as a parameter
def detect_failed_logins(filepath):
    # we will open the file and read the lines using 'with' statement
    with open(filepath,"r") as file:
        # now time to use readline() to real all the lines
        lines = file.readlines()
    # using list comprehension to filter lines that contain "failed"
    failed_logins = [line for line in lines if "failed password" in line.lower()]


    print(f"toal failed logins: {len(failed_logins)}")

    print("\nSample failed login attempts:\n")
    for line in failed_logins[:10]:  # Only show the first 10 for readability
        print(line.strip())

detect_failed_logins("sample_auth.log")