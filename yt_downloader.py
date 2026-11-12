import yt_dlp
import os

def download_yt_video(url):
    # Path folder Downloads
    download_path = r'C:\Users\ACER\Downloads\%(title)s.%(ext)s'
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'noplaylist': True,
        'outtmpl': download_path,
        'merge_output_format': 'mp4',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n[SISTEM] Sedang mengunduh...")
            ydl.download([url])
        print(f"\n[SUKSES] Video tersimpan di folder Downloads.")
    except Exception as e:
        print(f"\n[ERROR] Terjadi masalah: {e}")

def main():
    print("=== YouTube Video Downloader (MP4) ===")
    
    while True:
        video_url = input("\nMasukkan URL YouTube (atau ketik 'n' untuk keluar): ")
        
        # Cek jika user ingin keluar
        if video_url.lower() == 'n':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
            
        if not video_url.strip():
            print("URL tidak boleh kosong!")
            continue

        download_yt_video(video_url)
        
        # Pilihan untuk lanjut atau tidak setelah download selesai
        pilihan = input("\nIngin download video lain? (y/n): ")
        if pilihan.lower() != 'y':
            print("Program ditutup.")
            break

if __name__ == "__main__":
    main()