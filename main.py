import os

def start_analysis():
    print("Aqlli TalkBack ishga tushirildi...")
    # Bu yerda biz skrinshot olamiz
    os.system("screencap -p /sdcard/screen.png")
    print("Ekran tasviri olindi. AI tahlil qilishga tayyor.")

if __name__ == "__main__":
    start_analysis()
