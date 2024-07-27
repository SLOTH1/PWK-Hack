#โครงการนี้สร้างขึ้นเพื่อศึกษาเท่านั้นไม่มีเจตนาแฮกใดๆ
import requests #ไลเบอรรี่สำหรับส่งรีเคส
import os

#ดึงข้อมูลไฟล์จากไฟล์อื่นเข้ามา
with open("school.txt", "r") as f:
     word = (f.read().split())

#เซ็ตค่าurlสำหรับส่งรีเคส
index = "http://150.95.91.122:2003/frame/0010003/2024-07-26/"

#ฟังก์ชั่น
for path in word:
     response = requests.get(index+path)
     if not response.ok:
        print(index+path, "off")
     else:
        print(index+path, "on")
        job = index+path
        with open("webon.txt", "a") as f:
                   f.write(index+path + "\n")
        with open("webon.txt", "r") as f:
             image = (f.read().split())
        image_urls = image

# ตรวจสอบเส้นทางของ SD card บนอุปกรณ์ Android
# ปกติ SD card จะถูกเมานต์ใน /storage หรือ /mnt
sdcard_path = '/storage/emulated/0'  # หรือ '/mnt/sdcard'
save_directory = os.path.join(sdcard_path, 'Download', 'SHIDO')

# ตรวจสอบว่าโฟลเดอร์มีอยู่แล้วหรือไม่ ถ้าไม่มีก็สร้างขึ้นมา
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# วนลูปเพื่อดาวน์โหลดรูปภาพแต่ละรูป
for shido, url in enumerate(image_urls):
    try:
        # ส่งคำขอ GET ไปยัง URL ของรูปภาพ
        response = requests.get(url)

        # ตรวจสอบว่าคำขอสำเร็จหรือไม่
        if response.status_code == 200:
            # สร้างชื่อไฟล์ที่ไม่ซ้ำกัน
            filename = f'shido_{shido+1}.jpg'
            # เส้นทางที่บันทึกไฟล์
            file_path = os.path.join(save_directory, filename)

            # บันทึกข้อมูลของรูปภาพลงในไฟล์
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'ดาวน์โหลดรูปภาพ {filename} สำเร็จ')
        else:
            print(f'ไม่สามารถดาวน์โหลดรูปภาพจาก {url} ได้:', response.status_code)
    except Exception as e:
        print(f'โหลดไม่ได้ {url}: {e}')
