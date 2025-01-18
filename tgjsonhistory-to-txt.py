import json

input_file = "result.json"
output_file = "telegram_history.txt"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

with open(output_file, "w", encoding="utf-8") as txt_file:
    if "messages" in data:
        for message in data["messages"]:
            if message.get("type") == "message" and "text" in message:
                text = message["text"]
                if isinstance(text, list):
                    text = "".join([part if isinstance(part, str) else part.get("text", "") for part in text])
                txt_file.write(text + "\n")
    else:
        print("Файл не содержит сообщений.")

print(f"Конвертация завершена. Результаты сохранены в {output_file}.")
