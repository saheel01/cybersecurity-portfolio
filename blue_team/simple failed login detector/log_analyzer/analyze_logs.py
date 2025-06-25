count = 0
with open("sample_log.txt", "r") as file:
    logs = file.readlines()

for line in logs:
    if "failed" in line:
        print("alert", line.strip())
        count += 1
print("failed attempts:", count)