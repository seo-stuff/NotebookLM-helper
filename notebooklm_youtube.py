from yt_dlp import YoutubeDL
from typing import Tuple, List, Union

def get_videos(url: str, source_type: str) -> Tuple[Union[List[str], str], int]:
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'playlistend': 9999,
        'ignoreerrors': True,
        'playlist_items': '1:9999'
    }
    
    base_url = url.split('/videos')[0].split('/streams')[0].rstrip('/')
    if source_type == "1":
        url = f"{base_url}/videos"
    elif source_type == "2":
        url = f"{base_url}/streams"
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(url, download=False)
            if not result:
                return [], 0
                
            videos = []
            total_videos = 0
            
            if 'entries' in result:
                entries = [entry for entry in result['entries'] if entry]
                total_videos = len(entries)
                
                if total_videos == 0:
                    return [], 0
                    
                for entry in entries:
                    if 'view_count' in entry:
                        video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                        videos.append((video_url, entry.get('view_count', 0)))
                
                if videos:
                    videos.sort(key=lambda x: x[1], reverse=True)
                    videos = [url for url, _ in videos]
            else:
                if 'id' in result:
                    video_url = f"https://www.youtube.com/watch?v={result['id']}"
                    videos.append(video_url)
                    total_videos = 1
                    
            return videos, total_videos
            
        except Exception as e:
            print(f"\nОшибка при получении данных: {str(e)}")
            return [], 0

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
    url = input("Введите URL YouTube канала: ")
    
    print("\nВыберите источник данных:")
    print("[1] Из видео")
    print("[2] Из трансляций")
    source_type = input("Ваш выбор: ")
    
    while source_type not in ["1", "2"]:
        print("\nНекорректный выбор!")
        source_type = input("Выберите 1 или 2: ")
    
    videos, total_videos = get_videos(url, source_type)
    
    if not videos:
        print("\nВидео не найдены!")
        input("\nНажмите Enter для завершения...")
        exit()
        
    print(f"\nВсего найдено: {total_videos}")
    print(f"Добавлено в файл: {len(videos)}")
    print("\nСписок URL:")
    
    for video in videos:
        print(video)
            
    js_code = generate_js_code(videos)
    with open('youtube_automation.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
        
    input("\nНажмите Enter для завершения...")