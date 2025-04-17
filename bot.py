from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import subprocess
import os
import time

print("🟢 Bot démarré...")

# 🔍 Tente de détecter le chemin de Chrome automatiquement
def find_chrome_binary():
    try:
        path = subprocess.check_output(['which', 'google-chrome'], stderr=subprocess.DEVNULL).decode().strip()
        if os.path.exists(path):
            return path
    except Exception:
        pass

    try:
        path = subprocess.check_output(['which', 'google-chrome-stable'], stderr=subprocess.DEVNULL).decode().strip()
        if os.path.exists(path):
            return path
    except Exception:
        pass

    try:
        path = subprocess.check_output(['which', 'chrome'], stderr=subprocess.DEVNULL).decode().strip()
        if os.path.exists(path):
            return path
    except Exception:
        pass

    return None

chrome_path = find_chrome_binary()

if not chrome_path:
    print("❌ Chrome introuvable automatiquement.")
    exit(1)
else:
    print(f"✅ Chrome détecté à : {chrome_path}")

chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

try:
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("🌐 Accès au site : https://rdv.permisdeconduire.gouv.fr")
    driver.get("https://rdv.permisdeconduire.gouv.fr")

    time.sleep(5)

    print("📄 Titre :", driver.title)
    driver.quit()
    print("✅ Terminé.")

except Exception as e:
    print("❌ Erreur :", e)



