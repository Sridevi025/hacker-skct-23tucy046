# student_name: Sridevi
# roll_number: 23tucy046
# project_name: SandboxBuilder
# date: 2026-03-28
# update1
# update 7
import os

target = input("Enter target IP: ")

print("Scanning target:", target)
os.system(f"nmap -sV {target}")
