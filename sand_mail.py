import smtplib
import sys
from email.message import EmailMessage

# 1. Получаем данные из Git Bash (аргументы, которые мы передали в хуке)
# sys.argv[0] - это имя самого скрипта
# sys.argv[1] - это REPO_NAME
# sys.argv[2] - это MSG (сообщение коммита)
repo_name = sys.argv[1] if len(sys.argv) > 1 else "Unknown Repo"
commit_msg = sys.argv[2] if len(sys.argv) > 2 else "No message"

# 2. Настройки почты (замени на свои данные)
MY_EMAIL = "vladkryshtop@gmail.com"
# Сюда вставь 16-значный "Пароль приложения" от Google (без пробелов)
MY_PASSWORD = "gehb hyrv yfnx sjag"
RECEIVER_EMAIL = "vladkryshtop@gmail.com" # Можно отправить самому себе

# 3. Формируем письмо
msg = EmailMessage()
msg.set_content(f"В репозитории '{repo_name}' сделан новый коммит.\nТекст сообщения: {commit_msg}")
msg['Subject'] = f"Git Notification: {repo_name}"
msg['From'] = MY_EMAIL
msg['To'] = RECEIVER_EMAIL

# 4. Отправка через сервер Gmail
# Зачем: SMTP_SSL создает защищенное соединение на порту 465
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(MY_EMAIL, MY_PASSWORD)
        smtp.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
