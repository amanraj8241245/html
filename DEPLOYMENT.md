# 🚀 Render पर Deploy करने की Guide

## ✅ जो कुछ की गई तैयारी:

1. **Flask Web Server** (`server.py`) - HTTP endpoint के साथ
2. **Procfile** - Render को बताता है कैसे शुरू करें
3. **render.yaml** - Automatic environment setup के लिए
4. **requirements.txt** - सभी Python dependencies updated
5. **.gitignore** - GitHub upload सही रहे

---

## 📋 Render पर Deploy करने के Steps:

### Step 1: GitHub पर Code Push करें
```bash
git add .
git commit -m "Add Render deployment files"
git push origin main
```

### Step 2: Render.com पर जाएं
- Website: https://render.com  
- Sign up या Login करें GitHub से

### Step 3: New Web Service बनाएं
1. Dashboard में **"New +"** बटन दबाएं
2. **"Web Service"** select करें
3. अपना GitHub repo connect करें (`amanraj8241245/html`)

### Step 4: Configuration सेट करें

| Setting | Value |
|---------|-------|
| **Name** | `html-converter-bot` |
| **Environment** | `Python 3.11` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn --bind 0.0.0.0:$PORT server:flask_app` |
| **Plan Type** | `Free` ✅ |

### Step 5: Environment Variables सेट करें

Dashboard में **"Environment"** tab में ये variables add करें:

```
API_ID=<your_telegram_api_id>
API_HASH=<your_telegram_api_hash>
BOT_TOKEN=<your_telegram_bot_token>
LOG_CHANNEL=<your_log_channel_id> (or 0)
PYTHON_VERSION=3.11
```

> **कहां से मिलेगा:**
> - `API_ID` & `API_HASH`: https://my.telegram.org/apps
> - `BOT_TOKEN`: @BotFather से `/newbot` command से

### Step 6: Deploy करें
1. Settings confirm करें
2. **"Create Web Service"** बटन दबाएं
3. Deploy होने दीजिए (2-3 मिनट लगेगा)

---

## ✨ आपका Bot अब Live है!

### Render देगा:
- **URL**: कुछ ऐसा: `https://html-converter-bot.onrender.com`
- **Endpoints**:
  - `GET /` → Health Check
  - `GET /status` → Bot Status

### Test करें:
```bash
curl https://html-converter-bot.onrender.com/
# Response: {"status": "healthy", "bot_running": true, ...}
```

---

## 📌 महत्वपूर्ण नोट्स:

✅ **Free Tier में काम करेगा:**
- 750 free dyno hours मिलते हैं हर महीने
- Automatic sleep नहीं होगा क्योंकि bot active है

❌ **Render Free की Limitations:**
- Bot 24/7 run नहीं रहेगा (Render suspend करता है)
- Solution: Paid plan लें या UptimeRobot से ping करें

---

## 🔧 अगर कोई Issue आए:

### Deploy fail हो रहा है?
- Render Dashboard में **"Logs"** देखें
- Check करें सभी env variables सही हैं

### Bot काम नहीं कर रहा?
```bash
# Local यहां test करें:
python server.py

# फिर आपका bot काम करेगा
```

### अगर `.session` file issue आए:
- Files already `.gitignore` में हैं
- Render पर automatically handle होगा

---

## 🎉 Success!

अब आपका **HTML↔TXT Converter Bot** Render पर live है! 

**Telegram पर test करें** → `/start` भेजें bot को 🤖

---

*Created for Render Free Tier Deployment*
