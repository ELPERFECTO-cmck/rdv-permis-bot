from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import time

print("🟢 Bot (Firefox) démarré...")

# ✅ Chemin de Firefox (version ESR installée sur Debian)
firefox_path = "/usr/bin/firefox"

# Vérifie si Firefox est bien là
if not os.path.exists(firefox_path):
    print("❌ Firefox introuvable à l'emplacement prévu.")
    exit(1)

options = Options()
options.binary_location = firefox_path
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






