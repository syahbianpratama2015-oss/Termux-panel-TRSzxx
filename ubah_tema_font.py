import os
import random

def main():
    os.system("clear")
    print("=== 🔠 UBAH GAYA PROMPT TERMUX ===")
    print("1. Gaya Hacker (Hijau Neon)")
    print("2. Gaya Cyberpunk (Ungu/Pink)")
    print("3. Gaya Matrix (Hijau Terang)")
    print("4. Gaya Minimalis (Putih)")
    print("5. Gaya Glitch (Warna Acak)")
    print("0. Batal")
    
    pilih = input("\nPilih gaya [0-5]: ")
    if pilih == '0': return

    # Hapus PS1 dan PROMPT_COMMAND lama dari .bashrc
    os.system("sed -i '/PS1=/d' ~/.bashrc")
    os.system("sed -i '/PROMPT_COMMAND=/d' ~/.bashrc")
    os.system("sed -i '/glitch_prompt/d' ~/.bashrc")

    if pilih == '1':
        prompt = r"PS1='\[\033[1;32m\]┌──(\[\033[1;37m\]TRSzxx\[\033[1;32m\])─[\[\033[1;36m\]\t\[\033[1;32m\]]\n└─\$ \[\033[0m\]'"
        print("✅ Gaya Hacker dipasang!")
    elif pilih == '2':
        prompt = r"PS1='\[\033[1;35m\]╭─\[\033[1;36m\]TRSzxx\[\033[1;35m\]─[\[\033[1;33m\]\t\[\033[1;35m\]]\n╰─➤ \[\033[0m\]'"
        print("✅ Gaya Cyberpunk dipasang!")
    elif pilih == '3':
        prompt = r"PS1='\[\033[1;32m\][\[\033[1;37m\]MATRIX\[\033[1;32m\]]─[\[\033[1;32m\]\t\[\033[1;32m\]]\n└─> \[\033[0m\]'"
        print("✅ Gaya Matrix dipasang!")
    elif pilih == '4':
        prompt = r"PS1='\[\033[1;37m\]\u@TRSzxx \[\033[1;34m\]\w \[\033[1;37m\]\$ \[\033[0m\]'"
        print("✅ Gaya Minimalis dipasang!")
    elif pilih == '5':
        # Logika Glitch dimasukin ke .bashrc
        glitch_code = """
glitch_prompt() {
    WARNA=("\\033[1;32m" "\\033[1;36m" "\\033[1;35m" "\\033[1;33m" "\\033[1;31m")
    W=${WARNA[$((RANDOM % 5))]}
    PS1="\\[\\033[1;36m\\][TRSzxx]\\[\\033[0m\\]─[${W}\\t\\[\\033[0m\\]]\\n└─\\$ \\[\\033[0m\\]"
}
PROMPT_COMMAND="glitch_prompt"
"""
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(glitch_code)
        print("✅ Gaya Glitch dipasang!")
        prompt = ""
    else:
        print("❌ Pilihan salah!")
        return

    if prompt:
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(prompt + "\n")
            
    print("\n💡 Ketik 'source ~/.bashrc' atau buka Termux baru buat liat hasilnya.")

if __name__ == "__main__":
    main()
