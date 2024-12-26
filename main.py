import asyncio
from torrentp import TorrentDownloader
from customtkinter import *



torrent_file = TorrentDownloader("magnet:?xt=urn:btih:5a222f72078f6ed82ad5a49789c92ffc681223e5&dn=Deadpool.%26.Wolverine.2024.1080P-Dual-Lat&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce", '.')

def start_dowload():
    asyncio.run(torrent_file.start_download())

def pause_dowload():
    # Detiene la descarga temporalmente
    torrent_file.pause_download()

    # Restaura la descarga
    # torrent_file.resume_download()

    # Detiene la descarga por completo
    # torrent_file.stop_download()

app = CTk()
app.geometry("400x150")

dowload_button = CTkButton(app, text="Iniciar descarga", command=start_dowload)
pause_button = CTkButton(app, text="Pausar Descarga", command=pause_dowload, fg_color="red")

dowload_button.pack(padx=20, pady=20)
pause_button.pack(padx=20, pady=20)




if __name__ == "__main__":

    app.mainloop()
    
    
    