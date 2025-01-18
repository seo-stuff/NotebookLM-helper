from yt_dlp import YoutubeDL

def get_videos(url):
    ydl_opts = {
        'extract_flat': 'in_playlist',
        'quiet': True,
        'playlistend': 9999,
        'ignoreerrors': True,
        'playlist_items': '1:9999'
    }
    
    if not '/videos' in url:
        url = f"{url}/videos"
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(url, download=False)
            videos = []
            
            if 'entries' in result:
                for entry in result['entries']:
                    if entry:
                        video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                        videos.append(video_url)
            else:
                video_url = f"https://www.youtube.com/watch?v={result['id']}"
                videos.append(video_url)
                    
            return videos
        except Exception as e:
            return f"Error: {str(e)}"

def generate_js_code(videos):
    js_code = """const config = {
  delay: 750
};

const urls = [
%s
];

async function addUrl(url) {
  const addSourceButton = document.querySelector('button[mattooltip="Добавить источник"]');
  if (!addSourceButton) throw new Error('Кнопка "Добавить источник" не найдена');
  addSourceButton.click();
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
  
  const youtubeButton = Array.from(document.querySelectorAll('.mdc-evolution-chip__text-label')).find(el => 
    el.textContent.trim() === 'YouTube'
  );
  
  if (!youtubeButton) throw new Error('Кнопка "YouTube" не найдена');
  youtubeButton.click();
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
  
  const urlInput = document.querySelector('input[formcontrolname="newUrl"]');
  if (!urlInput) throw new Error('Поле ввода URL не найдено');
  urlInput.value = url;
  urlInput.dispatchEvent(new Event('input', { bubbles: true }));
  urlInput.dispatchEvent(new Event('change', { bubbles: true }));
  urlInput.dispatchEvent(new Event('blur', { bubbles: true }));
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
  
  const submitButton = document.querySelector('button[type="submit"][mat-flat-button]');
  if (!submitButton) throw new Error('Кнопка "Добавить" не найдена');
  submitButton.removeAttribute('disabled');
  submitButton.click();
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
}

async function processUrls() {
  console.log(`Начинаем добавление ${urls.length} URL...`);
  
  for (let i = 0; i < urls.length; i++) {
    console.log(`Добавляем URL ${i + 1} из ${urls.length}: ${urls[i]}`);
    try {
      await addUrl(urls[i]);
    } catch (error) {
      console.error(`Ошибка при добавлении URL ${urls[i]}:`, error);
      const shouldContinue = confirm(`Произошла ошибка: ${error.message}\nПродолжить со следующего URL?`);
      if (!shouldContinue) break;
    }
  }
  console.log('Процесс завершен');
}

processUrls().catch(error => {
  console.error('Критическая ошибка:', error);
});"""
    
    urls_formatted = ',\n'.join(f"  '{url}'" for url in videos)
    return js_code % urls_formatted

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
            
    js_code = generate_js_code(videos)
    with open('youtube_automation.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
