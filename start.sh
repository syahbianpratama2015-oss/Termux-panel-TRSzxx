#!/data/data/com.termux/files/usr/bin/bash
clear
echo -e "\033[1;31m=========================================\033[0m"
echo -e "\033[1;33m   TERMUX TERKUNCI! MASUKKAN PANEL KUNCI.\033[0m"
echo -e "\033[1;31m=========================================\033[0m"
echo ""
read -p "Kunci: " kunci

if [ "$kunci" = "./start.sh" ]; then
    clear
    cmatrix -s -C green &
    CMATRIX_PID=$!
    sleep 3
    kill $CMATRIX_PID 2>/dev/null
    clear
    python ~/sambutan.py
    ./panel.sh
else
    echo -e "\n\033[1;31m❌ KUNCI SALAH! AKSES DITOLAK.\033[0m"
    echo "Silakan ketik ./start.sh untuk masuk."
fi
