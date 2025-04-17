from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("🟢 Bot démarré...")

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    driver = webdriver.Chrome(options=options)
    driver.get("https://rdv.permisdeconduire.gouv.fr")
    time.sleep(5)
    print("📄 Titre :", driver.title)
    driver.quit()
    print("✅ Terminé.")
except Exception as e:
    print("❌ Erreur :", e)
