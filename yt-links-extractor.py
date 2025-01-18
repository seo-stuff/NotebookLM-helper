from yt_dlp import YoutubeDL

def get_videos(url):
    ydl_opts = {
        'extract_flat': True,
        'quiet': True
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(url, download=False)
            videos = []
            
            if 'entries' in result:
                for entry in result['entries']:
                    video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                    videos.append(video_url)
            else:
                video_url = f"https://www.youtube.com/watch?v={result['id']}"
                videos.append(video_url)
                    
            return videos
        except Exception as e:
            return f"Error: {str(e)}"

def print_author_info():
    print("Автор - Иван Зимин")
    print("YT канал - Иван Зимин | SEO (@seo_stuff)")
    print("Telegram канал - Иван Зимин | SEO (@heymoneymaker)")
    print("-" * 50)

if __name__ == "__main__":
    print_author_info()
    url = input("Введите URL YouTube канала или плейлиста: ")
    videos = get_videos(url)
    
    with open('youtube_links.txt', 'w', encoding='utf-8') as f:
        for video in videos:
            f.write(f"{video}\n")
            print(video)
