import os
import platform

print("===== SERVER HEALTH CHECK =====")

print("\nOperating System:")
print(platform.system())

print("\nCPU Information:")
print(platform.processor())

print("\nDisk Usage:")
os.system("wmic logicaldisk get size,freespace,caption")

print("\nMemory Usage:")
os.system("systeminfo | findstr /C:\"Total Physical Memory\"")

print("\nPing Test:")
os.system("ping google.com")