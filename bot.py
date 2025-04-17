from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

print("🟢 Bot (Firefox) démarré...")

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

try:
    driver = webdriver.Firefox(options=options)
    driver.get("https://rdv.permisdeconduire.gouv.fr")
    time.sleep(5)
    print("📄 Titre :", driver.title)
    driver.quit()
    print("✅ Terminé.")
except Exception as e:
    print("❌ Erreur :", e)





