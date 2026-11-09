import os
import requests
import json

try:
    with open(os.path.expanduser("~/.groq_key"), "r") as f:
        exec(f.read())
except:
    print("❌ File ~/.groq_key gak ketemu!")
    exit()

# URL dan Model yang masih aktif di Groq
URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "openai/gpt-oss-120b"

def tanya_ai(pesan):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Kamu asisten AI yang jawab pakai bahasa Indonesia santai."},
            {"role": "user", "content": pesan}
        ]
    }
    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return "❌ API Key INVALID."
        return f"❌ Error: {response.status_code} - {e}"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    os.system("clear")
    print("=== 🤖 AI UNIVERSAL (GROQ) ===")
    while True:
        pesan = input("Lu: ").strip()
        if pesan.lower() == 'keluar': break
        if not pesan: continue
        print("\n⏳ Mikir...")
        print(f"\nAI: {tanya_ai(pesan)}\n")
