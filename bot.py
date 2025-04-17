from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

print("🟢 Bot démarré...")

# On définit le chemin manuel vers Chrome (important sur Render)
chrome_path = "/usr/bin/google-chrome"

chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

try:
    service = Service('/usr/local/bin/chromedriver')  # on force aussi le chemin de chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("🌐 Accès au site : https://rdv.permisdeconduire.gouv.fr")
    driver.get("https://rdv.permisdeconduire.gouv.fr")

    time.sleep(5)

    print("📄 Titre :", driver.title)
    driver.quit()
    print("✅ Terminé.")

except Exception as e:
    print("❌ Erreur :", e)

