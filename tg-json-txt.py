import json
import re

def extract_message_text(message):
    if message.get('type') == 'service':
        return ""
    
    text = message.get('text', '')
    
    if isinstance(text, str):
        return text
    elif isinstance(text, list):
        result_text = ""
        for item in text:
            if isinstance(item, dict) and 'text' in item:
                result_text += item['text']
            elif isinstance(item, str):
                result_text += item
        return result_text
    
    return ""

def extract_sender_name(message):
    # Извлекаем имя отправителя из поля 'from'
    sender_name = message.get('from', 'Unknown')
    return sender_name

def sanitize_filename(filename):
    # Удаляем или заменяем недопустимые символы в имени файла
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = filename.strip()
    if len(filename) > 100:  # Ограничиваем длину
        filename = filename[:100]
    return filename

with open('result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Получаем название чата
chat_name = "extracted_messages"  # Значение по умолчанию

if 'name' in data:
    chat_name = sanitize_filename(data['name'])
elif 'chats' in data and 'list' in data['chats']:
    # Если есть несколько чатов, используем название первого
    if data['chats']['list'] and 'name' in data['chats']['list'][0]:
        chat_name = sanitize_filename(data['chats']['list'][0]['name'])

messages_with_names = []

if 'chats' in data and 'list' in data['chats']:
    for chat in data['chats']['list']:
        if 'messages' in chat:
            for message in chat['messages']:
                text = extract_message_text(message)
                if text and text.strip():
                    sender_name = extract_sender_name(message)
                    formatted_message = f"{sender_name}: {text.strip()}"
                    messages_with_names.append(formatted_message)
elif 'messages' in data:
    for message in data['messages']:
        text = extract_message_text(message)
        if text and text.strip():
            sender_name = extract_sender_name(message)
            formatted_message = f"{sender_name}: {text.strip()}"
            messages_with_names.append(formatted_message)

# Объединяем сообщения от одного пользователя подряд
merged_messages = []
if messages_with_names:
    current_sender = None
    current_message_parts = []
    
    for msg in messages_with_names:
        # Разделяем на имя и текст
        parts = msg.split(': ', 1)
        if len(parts) == 2:
            sender, text = parts
            
            if sender == current_sender:
                # Добавляем текст к текущему сообщению
                current_message_parts.append(text)
            else:
                # Сохраняем предыдущее сообщение, если оно есть
                if current_sender is not None:
                    combined_text = '\n'.join(current_message_parts)
                    merged_messages.append(f"{current_sender}: {combined_text}")
                
                # Начинаем новое сообщение
                current_sender = sender
                current_message_parts = [text]
    
    # Добавляем последнее сообщение
    if current_sender is not None:
        combined_text = '\n'.join(current_message_parts)
        merged_messages.append(f"{current_sender}: {combined_text}")

# Убираем дубликаты
unique_messages = []
seen = set()

for msg in merged_messages:
    if msg not in seen:
        unique_messages.append(msg)
        seen.add(msg)

# Разбиваем на файлы по 3МБ
file_number = 1
current_size = 0
max_size = 3 * 1024 * 1024
current_file = None

try:
    current_file = open(f'{chat_name}_{file_number}.txt', 'w', encoding='utf-8')

    for message in unique_messages:
        line = "*\n" + message + '\n'
        line_size = len(line.encode('utf-8'))

        if current_size + line_size > max_size and current_size > 0:
            current_file.close()
            file_number += 1
            current_file = open(f'{chat_name}_{file_number}.txt', 'w', encoding='utf-8')
            current_size = 0

        current_file.write(line)
        current_size += line_size
finally:
    if current_file:
        current_file.close()

print(f"Название чата: {chat_name}")
print(f"Обработано {len(unique_messages)} уникальных сообщений")
print(f"Создано файлов: {file_number}")
