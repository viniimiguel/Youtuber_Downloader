from pytube import YouTube
import moviepy.editor as mp


class Yt():
    def __init__(self):
        self.link = input('COLE AQUI O LINK QUE VOCE DESEJA BAIXAR: ')
        self.yt = YouTube(self.link)
    
    def main(self):
        escolha = input("Digite 'audio' para baixar apenas o áudio ou 'video' para baixar apenas o vídeo: ")
        if escolha == 'audio':
            self.baixa_audio()
        elif escolha == 'video':
            self.baixa_video()
        else:
            print("Escolha inválida")

    def baixa_video(self):
        video_stream = self.yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        video_stream.download()
    
    def baixa_audio(self):
        audio_stream = self.yt.streams.filter(only_audio=True).first()
        audio_stream.download()
     


yout = Yt()
yout.main()
