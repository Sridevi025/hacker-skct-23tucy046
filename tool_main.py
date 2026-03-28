# student_name: Sridevi
# roll_number: 12345
# project_name: SandboxBuilder
# date: 2026-03-28

import os

target = input("Enter target IP: ")

print("Scanning target:", target)
os.system(f"nmap -sV {target}")
