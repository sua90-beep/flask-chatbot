# ChatBot Flask Project

פרויקט Web מבוסס Flask עם שכבות Backend ו-Frontend, שמנהל שיחות ושולח הודעות ל-OpenAI.

## Tech Stack

- Python 3
- Flask
- SQLAlchemy
- MySQL (דרך connection string)
- OpenAI API

## Project Structure

- src/app.py: נקודת הכניסה לאפליקציה
- src/backend/controllers: נתיבי HTTP
- src/backend/services: לוגיקה עסקית
- src/backend/models: מודלים למסד נתונים
- src/backend/middleware: טיפול בשגיאות
- src/Frontend/templates: תבניות HTML
- src/Frontend/static: CSS/JS/Images
- src/utils: קונפיגורציה וחיבור למסד

## Prerequisites

- Python מותקן במחשב
- סביבת עבודה עם הרשאות להריץ venv
- מסד נתונים נגיש לפי CONNECTION_STRING
- OpenAI API Key פעיל

## Installation

1. ליצור ולהפעיל סביבת venv:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

2. להתקין תלויות:

```powershell
pip install -r requirements.txt
```

## Environment Variables

יש ליצור קובץ .env בשורש הפרויקט ולהגדיר:

```env
CONNECTION_STRING=mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>
SERVER_SIDE_SESSION_SECRET_KEY=your_secret_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Run

```powershell
flask --app src/app.py run --debug
```

האפליקציה תעלה בדרך כלל בכתובת:

- http://127.0.0.1:5000

## Main Routes

- GET /home: דף הבית (שיחה חדשה)
- POST /home/send: שליחת הודעה
- GET /home/conversation: הצגת השיחה הנוכחית
- GET /home/new: התחלת שיחה חדשה
- GET /about: דף מידע

## Notes

- ברענון דף אחרי שליחה לא מתבצעת שליחה כפולה (Post-Redirect-Get).
- אם השרת עולה אבל דפים לא נטענים, יש לוודא שמבנה התיקיות של Frontend נשמר כפי שהוא בפרויקט.
