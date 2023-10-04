import yt_dlp

class Yt():
    def __init__(self):
        self.link = input('DIGITE O LINK QUE VOCE QUER FAZER O DOWNLOAD AQUI:  ')
        self.ydl_opts = {
            'format': 'best',  
            'outtmpl': 'output/%(title)s.%(ext)s',  
        }

    def main(self):
        inpt = input('DIGITE (1) PARA BAIXAR VIDEOS:  ')
        if inpt == '1':
            self.download_video()
        else:
            print('ALGO DEU ERRADO!')
            self.main()

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