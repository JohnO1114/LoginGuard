from collections import Counter

with open("login.log", "r") as file:
    logs = file.readlines()


failed_ips = Counter()
successes = 0
failures = 0

valid_attempt = 0

for log in logs:
    log = log.strip()

    if not log:
        continue

    parts = log.split()

    if len(parts) != 4:
        print(f"Skipping invalid log entry: {log}")
        continue

    time, username, status, ip = parts

    valid_attempt += 1

    if status == "FAILED":
        failures += 1
        failed_ips[ip] += 1
    elif status == "SUCCESS":
        successes += 1
    else:
        print(f"Skipping unknown status: {status}")










print("=== LoginGuard Security Report ===")
print(f"Total login attempts: {len(logs)}")
print(f"Successful logins: {successes}")
print(f"Failed logins: {failures}")

print("\nSuspicious activity:")

alerts_found = False

for ip, count in failed_ips.items():
    if count >= 3:
        print(f"ALERT: {ip} had {count} failed login attempts")
        alerts_found = True

if not alerts_found:
    print("No repeated failed-login alerts detected.")

print("\nReport complete.")






