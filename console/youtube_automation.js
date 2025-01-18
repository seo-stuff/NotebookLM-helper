const config = {
  delay: 750
};

const urls = [
  'https://www.youtube.com/watch?v=jS6wCljn4qA',
  'https://www.youtube.com/watch?v=QPY0u1XcDqQ',
  'https://www.youtube.com/watch?v=URiMMJAOJU8',
  'https://www.youtube.com/watch?v=WjRAXXrMVLI',
  'https://www.youtube.com/watch?v=92FqWJv1fmg',
  'https://www.youtube.com/watch?v=KouWpchwYpg',
  'https://www.youtube.com/watch?v=8B459Kf03hE',
  'https://www.youtube.com/watch?v=nRQGrnegR88',
  'https://www.youtube.com/watch?v=odt0H21Ej0o',
  'https://www.youtube.com/watch?v=ovX4FJ1HCKc',
  'https://www.youtube.com/watch?v=iKeDYE6FX28',
  'https://www.youtube.com/watch?v=h9B6WAARxVI',
  'https://www.youtube.com/watch?v=tuWiqCET1eQ',
  'https://www.youtube.com/watch?v=TxRA14Mat_w',
  'https://www.youtube.com/watch?v=teUU0ZjI1TQ',
  'https://www.youtube.com/watch?v=wVC18er-ktQ',
  'https://www.youtube.com/watch?v=Q49TDFh9qSM',
  'https://www.youtube.com/watch?v=B5lUMCx_rl4',
  'https://www.youtube.com/watch?v=-nZHBvyMUNI',
  'https://www.youtube.com/watch?v=V3UilzEGi2k',
  'https://www.youtube.com/watch?v=uo0Gd2W0Atk',
  'https://www.youtube.com/watch?v=U7y145BpHxM',
  'https://www.youtube.com/watch?v=Pkeu5Ujj2-Y',
  'https://www.youtube.com/watch?v=ed_JbjMLodE',
  'https://www.youtube.com/watch?v=ioaobc80t-Q',
  'https://www.youtube.com/watch?v=ZSUnqYRh6J0',
  'https://www.youtube.com/watch?v=z2RClOVSOoE',
  'https://www.youtube.com/watch?v=EMGlJEkre5s',
  'https://www.youtube.com/watch?v=V9yFoUSUW6o',
  'https://www.youtube.com/watch?v=RBjbDJIyv6U',
  'https://www.youtube.com/watch?v=55MJNHEPY2Y',
  'https://www.youtube.com/watch?v=pP7fFp2wi1w',
  'https://www.youtube.com/watch?v=ImRDUZCcE_U',
  'https://www.youtube.com/watch?v=pGaMqysYu2s',
  'https://www.youtube.com/watch?v=kIKlXPDkPnE',
  'https://www.youtube.com/watch?v=UCynbMXSIM0',
  'https://www.youtube.com/watch?v=h6r7wR-bx9A',
  'https://www.youtube.com/watch?v=1fYKMQixqWg',
  'https://www.youtube.com/watch?v=UUxOIxnSuiI',
  'https://www.youtube.com/watch?v=keVvDvWiBvA',
  'https://www.youtube.com/watch?v=PkrydnaafGo',
  'https://www.youtube.com/watch?v=sh-Z6Nwpzlc',
  'https://www.youtube.com/watch?v=abMqOTXdK88',
  'https://www.youtube.com/watch?v=_cBkGs2bzcM',
  'https://www.youtube.com/watch?v=s4qs7EJ33PE',
  'https://www.youtube.com/watch?v=rvNnf0k7N50',
  'https://www.youtube.com/watch?v=jvZyxAMHgY8',
  'https://www.youtube.com/watch?v=lVq1jjLn678',
  'https://www.youtube.com/watch?v=sFjqbqLrcO8',
  'https://www.youtube.com/watch?v=DrHjCd39IFE',
  'https://www.youtube.com/watch?v=LCJoy8PLt1M',
  'https://www.youtube.com/watch?v=VRsywcHiHbY',
  'https://www.youtube.com/watch?v=1UOzSle3GWU',
  'https://www.youtube.com/watch?v=1WpENGJanM8',
  'https://www.youtube.com/watch?v=txkyZ53hSqw',
  'https://www.youtube.com/watch?v=-sb5bF8L3l0',
  'https://www.youtube.com/watch?v=uotLxPUFtnc',
  'https://www.youtube.com/watch?v=dDUb4B3_75M',
  'https://www.youtube.com/watch?v=ZMJDsQcvbv0',
  'https://www.youtube.com/watch?v=LZ9cuv1WsUg',
  'https://www.youtube.com/watch?v=eeL9NxAWhwI',
  'https://www.youtube.com/watch?v=2g7jKg8mafk',
  'https://www.youtube.com/watch?v=F5JHugSjuIc',
  'https://www.youtube.com/watch?v=JPtu3ATGAPE',
  'https://www.youtube.com/watch?v=Ac1VJ_9BXFc',
  'https://www.youtube.com/watch?v=CZJTcHSnwTY',
  'https://www.youtube.com/watch?v=9bYM7d5xs24',
  'https://www.youtube.com/watch?v=fwVYN5dKdpA',
  'https://www.youtube.com/watch?v=qwu_CImhjnA',
  'https://www.youtube.com/watch?v=ZLi0dfr0TIA',
  'https://www.youtube.com/watch?v=EWOKgkf-CEY',
  'https://www.youtube.com/watch?v=AIpRpBb1KsI',
  'https://www.youtube.com/watch?v=lmjiIJ5Ge98',
  'https://www.youtube.com/watch?v=AdoULHKSQZw',
  'https://www.youtube.com/watch?v=2raqtB8mUQE',
  'https://www.youtube.com/watch?v=m9Tp3ZpBKbM',
  'https://www.youtube.com/watch?v=ok65iCc-Tn4',
  'https://www.youtube.com/watch?v=JDpx0Kgc9rA',
  'https://www.youtube.com/watch?v=Ias7AKJYJTo',
  'https://www.youtube.com/watch?v=wgZdv1vPZhk',
  'https://www.youtube.com/watch?v=2qzmIRvHux8',
  'https://www.youtube.com/watch?v=Em16KXw4aiE',
  'https://www.youtube.com/watch?v=AV_REayuGnI'
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
      const shouldContinue = confirm(`Произошла ошибка: ${error.message}
Продолжить со следующего URL?`);
      if (!shouldContinue) break;
    }
  }
  console.log('Процесс завершен');
}

processUrls().catch(error => {
  console.error('Критическая ошибка:', error);
});