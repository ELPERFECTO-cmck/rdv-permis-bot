from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

print("🟢 Bot démarré...")

# 🔍 Liste des chemins possibles pour Chrome
chrome_paths = [
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/opt/google/chrome/google-chrome"
]

chrome_path = None
for path in chrome_paths:
    if os.path.exists(path):
        chrome_path = path
        break

if not chrome_path:
    print("❌ Chrome introuvable dans les chemins connus.")
    exit(1)

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


