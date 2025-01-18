const config = {
  delay: 750
};

const urls = [
  'url1',
  'url2'
];

async function addUrl(url) {
  const addSourceButton = document.querySelector('button[mattooltip="Добавить источник"]');
  if (!addSourceButton) throw new Error('Кнопка "Добавить источник" не найдена');
  addSourceButton.click();
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
  
  const siteLink = Array.from(document.querySelectorAll('a, span')).find(el => 
    el.textContent === 'Сайт'
  );
  
  if (!siteLink) throw new Error('Ссылка "Сайт" не найдена');
  siteLink.click();
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
  
  const urlInput = document.querySelector('.mat-mdc-form-field input');
  if (!urlInput) throw new Error('Поле ввода URL не найдено');
  urlInput.value = url;
  urlInput.dispatchEvent(new Event('input', { bubbles: true }));
  urlInput.dispatchEvent(new Event('change', { bubbles: true }));
  urlInput.dispatchEvent(new Event('blur', { bubbles: true }));
  
  await new Promise(resolve => setTimeout(resolve, config.delay));
  
  const submitButton = document.querySelector('.mat-mdc-form-field ~ button');
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
});
