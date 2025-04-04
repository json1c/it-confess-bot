<h1 align="center">📜 Притчи от батюшки</h1>
<p align="center">
  <em>Бот, приносящий IT-просветление</em>
</p>

<p align="center">
  <img src="https://api.huisbn.ru/generate" alt="Пример притчи" width="400"/>
</p>

---

## ✨ О чём это

> _"Внемли, разработчик, если баг исчез сам по себе — грядёт возмездие логами."_

Это бот, который по инлайн запросу отправляет случайную IT-притчу от батюшки.  
Для всех, кто редактирует прод по пятницам и верит в реинкарнацию багов.

---

## 🔧 Установка

### 1. Установи зависимости:

```bash
pip install -r requirements.txt
```

### 2. Создай конфиг `config.toml`:

```toml
[bot]
token = "ТОКЕН_БОТА"

[api]
api_url = "https://твой-домен/generate"

[web]
listen_ip = "0.0.0.0"
listen_port = 8000

[settings]
parables_path = "assets/parables.txt"
background_path = "assets/background.png"
font_path = "assets/font.ttf"
```

### 3. Запусти бота

```bash
python -m tgbot
```

---

## 📸 Как это работает

- ✅ Ты вводишь `@bot_username` в диалоге.
- 📜 Бот случайным образом берёт притчу из файла.
- 🖼 Генерирует картинку с притчей через PIL.
- 🚀 Отправляет.

---

## 🧠 Пример притч

> **"Истинно говорю тебе: если линтер ругается — ты навлёк кару багов."**

> **"Не забывай, если деплоишь в пятницу — CI/CD распнёт тебя таймаутами."**

> **"Помни, чадо, если код не документирован — спасение лишь в рефакторинге."**

---

## 📜 Хочешь свои притчи?

Просто добавь их в `assets/parables.txt`, по одной притче на строку.  
---

## ⚙️ Используемые технологии

- 🧠 Python 3.11+
- 🤖 Aiogram 3
- 🌐 aiohttp
- 🖌 Pillow (PIL)
- 🐳 Docker-ready (если захочешь)

---

## 🤝 Контакты и участие

💬 https://t.me/json1c
---

<p align="center"><strong>И запомни навсегда:</strong><br>
<em>"Если баг исчез сам по себе — он вернётся в пятницу на проде."</em></p>
