from ai_universal import tanya_ai
import os

def main():
    os.system("clear")
    print("=== 🤖 AI UNIVERSAL (GROQ) ===")
    print("Ketik 'keluar' untuk berhenti.\n")
    while True:
        pesan = input("Lu: ").strip()
        if pesan.lower() == 'keluar': break
        if not pesan: continue
        print("\n⏳ AI lagi mikir...")
        print(f"\nAI: {tanya_ai(pesan)}\n")

if __name__ == "__main__":
    main()
