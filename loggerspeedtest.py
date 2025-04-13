import speedtest
import pandas as pd
import os
import time
from datetime import datetime

# Plik do logowania wyników
LOG_FILE = "speedtest_log.csv"

# Wykonaj pomiar
def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = round(st.download() / 1_000_000, 2)  # Mbps
    upload = round(st.upload() / 1_000_000, 2)      # Mbps
    ping = round(st.results.ping, 2)                # ms
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "timestamp": timestamp,
        "download_Mbps": download,
        "upload_Mbps": upload,
        "ping_ms": ping
    }

# Zapisz wynik do pliku CSV
def save_result(data):
    df = pd.DataFrame([data])

    if not os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)

# Główna funkcja (jednorazowa lub cykliczna)
def start_logging(interval_minutes=60):
    while True:
        print("⏳ Trwa pomiar prędkości...")
        result = run_speedtest()
        save_result(result)
        print(f"✅ Zapisano: {result}")
        print(f"⏱ Kolejny pomiar za {interval_minutes} minut.\n")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    # Zmienna: co ile minut ma być wykonywany test (np. 60 = co godzinę)
    start_logging(interval_minutes=30)
