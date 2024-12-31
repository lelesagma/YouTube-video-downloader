from yt_dlp import YoutubeDL
import os

url = input("Saisissez l'URL de la vidéo : ")
save_path = input("Saisissez le chemin de sauvegarde : ")

ydl_opts = {
    'format': 'best',  
    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Téléchargement terminé.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
