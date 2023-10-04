import yt_dlp


ydl_opts = {
    'format': 'best',  
    'outtmpl': 'output/%(title)s.%(ext)s',  
}


video_url = 'https://www.youtube.com/watch?v=Smycv81WN6Q&list=RDSmycv81WN6Q&start_radio=1'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    result = ydl.extract_info(video_url, download=True)
    
    if 'entries' in result:
        
        for entry in result['entries']:
            print('Nome:', entry['title'])
            print('ID do vídeo:', entry['id'])
    else:
        
        print('Nome:', result['title'])
        print('ID do vídeo:', result['id'])
