import os
import sys
import time

def signal_yuborish(chastota, davomiyligi):
    # Termux-da qisqa tovushli signal (beep) chiqarish
    os.system(f"termux-media-player play --hz {chastota} --duration {davomiyligi}")

def oflayn_tahlil():
    print("[Oflayn Tizim] Skrinshot olinmoqda...")
    # Telefon ekranini rasmga olish
    os.system("screencap -p /sdcard/screen.png")
    
    # Kelgusi qadamda yuklanadigan TFLite model shu yerda rasmdagi o'yin elementlarini tahlil qiladi
    # Hozircha tizim ishlashini tekshirish uchun test signali beramiz
    print("[Oflayn Tizim] Ob'ekt topildi. Signal yuborilmoqda...")
    signal_yuborish(880, 150) # 880Hz chastotali qisqa signal

if __name__ == "__main__":
    oflayn_tahlil()

git add main.py && git commit -m "Oflayn kod yangilandi" && git push origin master || git push origin main


cat << 'EOF' > .github/workflows/ai_tahlil.yml
name: Tayyor APK Ilovani Qurish

on:
  push:
    branches:
      - main
      - master

jobs:
  build_apk:
    runs-on: ubuntu-latest
    steps:
      - name: Kodni yuklash
        uses: actions/checkout@v4

      - name: Python va Buildozer muhitini sozlash
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Android SDK va Kerakli paketlarni o'rnatish
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip install buildozer cython

      - name: Boshlang'ich ilova sozlamasini yaratish
        run: |
          buildozer init
          # Sozlamalarda ilova nomini va kerakli kutubxonalarni avtomatik kiritamiz
          sed -i 's/title = My Application/title = Aqlli TalkBack/g' buildozer.spec
          sed -i 's/package.name = myapp/package.name = aqllitalkback/g' buildozer.spec
          sed -i 's/requirements = python3,kivy/requirements = python3,kivy,tensorflow-lite/g' buildozer.spec

      - name: APK faylini qurish (Compile)
        run: |
          buildozer android debug

      - name: Tayyor APK faylini yuklab olish uchun saqlash
        uses: actions/upload-artifact@v4
        with:
          name: Aqlli_TalkBack_Ilova
          path: bin/*.apk
