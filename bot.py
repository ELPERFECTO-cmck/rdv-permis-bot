from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

print("🟢 Bot démarré...")

# Chemin alternatif vers Chrome
chrome_path = "/usr/bin/google-chrome-stable"

# Vérification de l'existence
if not os.path.exists(chrome_path):
    print("❌ Chrome n'est pas installé à l'emplacement prévu.")
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


