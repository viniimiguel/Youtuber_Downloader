import yt_dlp

class Yt():
    def __init__(self):
        self.link = input('DIGITE O LINK QUE VOCE QUER FAZER O DOWNLOAD AQUI:  ')
        self.ydl_opts = {
            'format': 'best',  
            'outtmpl': 'output/%(title)s.%(ext)s',  
        }
        self.ydl_optss = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'output/%(title)s.%(ext)s',
        }

    def main(self):
        inpt = input('DIGITE (1) PARA BAIXAR VIDEOS, DIGITE (2) PARA BAIXAR AUDIOS:  ')
        if inpt == '1':
            self.download_video()
        elif inpt == '2':
            self.download_audio()
        else:
            print('ALGO DEU ERRADO!')
            self.main()

    def download_audio(self):
        with yt_dlp.YoutubeDL(self.ydl_optss) as ydl:
            result = ydl.extract_info(self.link, download=True)

            if 'entries' in result:
                for entry in result['entries']:
                    print('Nome:', entry['title'])
                    print('ID do vídeo:', entry['id'])
            else:
                print('Nome:', result['title'])
                print('ID do vídeo:', result['id'])

    def download_video(self):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            result = ydl.extract_info(self.link, download=True)
            
            if 'entries' in result:
                for entry in result['entries']:
                    print('Nome:', entry['title'])
                    print('ID do vídeo:', entry['id'])
            else:
                print('Nome:', result['title'])
                print('ID do vídeo:', result['id'])

youtube = Yt()
youtube.main()
