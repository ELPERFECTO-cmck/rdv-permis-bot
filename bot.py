from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("💡 Le script a bien démarré")

chrome_path = "chrome_path = "/usr/bin/google-chrome"
  # 💥 chemin correct dans l'image officielle

chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rdv.permisdeconduire.gouv.fr")

    time.sleep(5)

    print("📄 Titre :", driver.title)
    driver.quit()
    print("✅ Terminé.")
except Exception as e:
    print("❌ Erreur :", e)




