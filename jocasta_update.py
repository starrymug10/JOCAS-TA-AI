import os
import requests
import zipfile
import io

GITHUB_ZIP_URL = "https://github.com/starrymug10/JOCAS-TA-AI/archive/refs/heads/main.zip"

def update_from_github():
    print("Mengecek pembaruan dari GitHub...")
    resp = requests.get(GITHUB_ZIP_URL)
    if resp.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(resp.content))
        z.extractall("JOCAS-TA-Update")
        print("Update selesai, silakan restart aplikasi.")
    else:
        print("Gagal mengunduh update.")

if __name__ == "__main__":
    update_from_github()
