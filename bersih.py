import os
print("🧹 Membersihkan cache Termux...")
os.system("apt clean && rm -rf ~/.cache/*")
print("✅ Termux bersih dan ringan!")
