#!/data/data/com.termux/files/usr/bin/bash

if [ -f ~/tema.conf ]; then
    source ~/tema.conf
else
    CYAN='\033[1;36m'; GREEN='\033[1;32m'; YELLOW='\033[1;33m'; RED='\033[1;31m'
fi
NC='\033[0m'

pause() { read -p "Tekan [Enter] untuk kembali..."; }

# Fungsi buat nampilin info HP
info_hp() {
    MODEL=$(getprop ro.product.model)
    ANDROID=$(getprop ro.build.version.release)
    RAM_TOTAL=$(free -m | awk '/Mem:/ {print $2}')
    RAM_FREE=$(free -m | awk '/Mem:/ {print $4}')
    echo -e "${CYAN}Device  : $MODEL${NC}"
    echo -e "${CYAN}Android : $ANDROID${NC}"
    echo -e "${CYAN}RAM     : ${RAM_FREE}MB / ${RAM_TOTAL}MB${NC}"
}

while true; do
    clear
    
    # --- GAMBAR LOGO LINUX (TUX) PAKE # KUNING ---
    echo -e "${YELLOW}                    .--."
    echo -e "${YELLOW}                   |o_o |"
    echo -e "${YELLOW}                   |:_/ |"
    echo -e "${YELLOW}                  //   \ \\"
    echo -e "${YELLOW}                 (|     | )"
    echo -e "${YELLOW}                /'\\_   _/\`\\"
    echo -e "${YELLOW}                \\___)=(___/${NC}"
    
    # --- HEADER DASHBOARD ---
    echo -e "${CYAN}====================================================================${NC}"
    echo -e "${CYAN}  ████████╗██████╗ ███████╗███████╗██╗  ██╗██╗  ██╗${NC}"
    echo -e "${CYAN}  ╚══██╔══╝██╔══██╗██╔════╝╚══███╔╝╚██╗██╔╝╚██╗██╔╝${NC}"
    echo -e "${CYAN}     ██║   ██████╔╝███████╗  ███╔╝  ╚███╔╝  ╚███╔╝ ${NC}"
    echo -e "${CYAN}     ██║   ██╔══██╗╚════██║ ███╔╝   ██╔██╗  ██╔██╗ ${NC}"
    echo -e "${CYAN}     ██║   ██║  ██║███████║███████╗██╔╝ ██╗██╔╝ ██╗${NC}"
    echo -e "${CYAN}     ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝${NC}"
    echo -e "${CYAN}====================================================================${NC}"
    
    # Nampilin info HP
    info_hp
    echo -e "${CYAN}====================================================================${NC}"
    echo -e "${YELLOW}                [ 70 FITUR ULTIMATE - HACKER DASHBOARD ]${NC}"
    echo -e "${CYAN}====================================================================${NC}"
    
    # --- MENU ---
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 1 "Nonton Anime" 2 "AI Kode Game"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 3 "Kalkulator" 4 "Ubah Tema"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 5 "Menu Shell" 6 "Update Tema"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 7 "Uji Keamanan" 8 "AI Ngajarin"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 9 "AI Ngoding" 10 "Bikin APK"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 11 "Gabung Hewan" 12 "Gabung Emoji"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 13 "Pass Gen" 14 "Lab XSS"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 15 "Belajar White" 16 "Belajar Hack"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 17 "Ular Tangga" 18 "Ular Jadul"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 19 "Ular Visual" 20 "Matrix Effect"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 21 "Download YT" 22 "Cek IP"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 23 "Scan Nmap" 24 "Cek Cuaca"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 25 "Kalku Umur" 26 "Fake Hack"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 27 "Kata Acak" 28 "Konversi Suhu"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 29 "Rata Nilai" 30 "Jam Digital"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 31 "Efek Matrix" 32 "Cek Cuaca 2"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 33 "Kata Acak 2" 34 "Prank Hack"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 35 "Jam Digital 2" 36 "Suhu 2"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 37 "Rata Nilai 2" 38 "Umur 2"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 39 "Kucing ASCII" 40 "Banner Teks"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 41 "Cek IP 2" 42 "Spam Pass"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 43 "Waktu Sholat" 44 "Download YT 2"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 45 "Scan Nmap 2" 46 "Traceroute"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 47 "DNS Lookup" 48 "Web Server"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 49 "Baca File" 50 "Bersihkan"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 51 "Scan Wi-Fi" 52 "Scan Hotspot"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 53 "Cek Pass Bocor" 54 "Ganti Tema"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 55 "Catatan (Notes)" 56 "TOOLS TRSzxx"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 57 "Cek Status Website" 58 "Belajar Matematika"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 59 "Detektor Kata Kasar" 60 "AI Ngelawak"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 61 "API Key (AI) VIP" 62 "API Key (AI) Sebulan"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 63 "Ubah Font (10 Gaya)" 64 "AI Gambar VIP"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 65 "Block Blast V3" 66 "Setel Lagu"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 67 "LEGENDARY LOUNGE" 68 "Generator Puisi Galau"
    printf "${YELLOW}%2d.${NC} %-18s ${YELLOW}%2d.${NC} %-18s\n" 69 "Game Pantun" 70 "Kamus Hukum IT"
    
    echo -e "${RED} 0.${NC} Keluar"
    echo ""
    read -p "Pilih menu [0-70]: " pil
    
    case $pil in
        1) bash ani-cli; pause;; 2) echo "Butuh API"; pause;;
        3) python kalkulator.py; pause;; 4) echo "Tema diganti!"; pause;;
        5) bash; pause;; 6) echo "Cek GitHub"; pause;;
        7) python uji_keamanan.py; pause;; 8|9) python ai_simulasi.py; pause;;
        10) echo "Butuh SDK"; pause;; 11) python gabung_hewan.py; pause;;
        12) python gabung_emoji.py; pause;; 13) python passgen.py; pause;;
        14) python lab_xss.py; pause;; 15) python whitehat.py; pause;;
        16) python hacking.py; pause;; 17) python ular_tangga.py; pause;;
        18) python snake.py; pause;; 19) python ular_visual.py; pause;;
        20) python matrix.py; pause;; 21) python downloader.py; pause;;
        22) python cek_ip.py; pause;; 23) python scan_nmap.py; pause;;
        24) python cuaca.py; pause;; 25) python umur.py; pause;;
        26) python prank.py; pause;; 27) python kata_acak.py; pause;;
        28) python suhu.py; pause;; 29) python rata_rata.py; pause;;
        30) python jam_digital.py; pause;; 31) cmatrix; pause;;
        32) python cuaca.py; pause;; 33) python kata_acak.py; pause;;
        34) python prank.py; pause;; 35) python jam_digital.py; pause;;
        36) python suhu.py; pause;; 37) python rata_rata.py; pause;;
        38) python umur.py; pause;; 39) python ascii_kucing.py; pause;;
        40) python banner.py; pause;; 41) python cek_ip.py; pause;;
        42) python spam_pass.py; pause;; 43) python sholat.py; pause;;
        44) python downloader.py; pause;; 45) python scan_nmap.py; pause;;
        46) python trace.py; pause;; 47) python dns_lookup.py; pause;;
        48) python web_server.py; pause;; 49) python baca_file.py; pause;;
        50) python bersih.py; pause;; 51) python scan_wifi.py; pause;;
        52) python scan_hotspot.py; pause;; 53) python cek_bocor.py; pause;;
        54) python ganti_tema.py; pause;; 55) python catatan.py; pause;;
        56) python tools_trszxx.py; pause;; 57) python cek_web.py; pause;;
        58) python matematika.py; pause;; 59) python sensor.py; pause;;
        60) python ai_ngelawak.py; pause;; 61) python ai_vip.py; pause;;
        62) python kuis_vip.py; pause;; 63) python font_keren.py; pause;;
        64) python ai_gambar.py; pause;; 65) python block_blast_v3.py; pause;;
        66) python setel_lagu.py; pause;; 67) python legendary_lounge.py; pause;;
        68) python puisi_galau.py; pause;; 69) python game_pantun.py; pause;;
        70) python hukum_it.py; pause;;
        0) echo -e "${CYAN}Dadah! 👋${NC}"; exit 0;;
        *) echo -e "${RED}Pilihan tidak valid!${NC}"; sleep 2;;
    esac
done
