import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    from fake_useragent import UserAgent
except ImportError:
    os.system("pip install fake_useragent")
    from fake_useragent import UserAgent
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except ImportError:
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
try:
    from pytube import YouTube
except ImportError:
    os.system("pip install pytube")
    from pytube import YouTube
try:
    from PIL import Image, ImageFilter
except ImportError:
    os.system("pip install pillow")
    from PIL import Image, ImageFilter
import time
import random
import datetime

merah = "\033[91m"
hijau = "\033[92m"
kuning = "\033[93m"
biru = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
putih = "\033[97m"

bahasa = ["en-US,en;q=0.9", "id-ID,id;q=0.8", "ja-JP,ja;q=0.9", "zh-CN,zh;q=0.9", "es-ES,es;q=0.9",
          "fr-FR,fr;q=0.9", "de-DE,de;q=0.9", "pt-BR,pt;q=0.9", "ru-RU,ru;q=0.9", "ko-KR,ko;q=0.9",
          "it-IT,it;q=0.9", "vi-VN,vi;q=0.9", "ar-SA,ar;q=0.9", "tr-TR,tr;q=0.9", "pl-PL,pl;q=0.9",
          "nl-NL,nl;q=0.9", "th-TH,th;q=0.9", "sv-SE,sv;q=0.9", "da-DK,da;q=0.9", "fi-FI,fi;q=0.9",
          "cs-CZ,cs;q=0.9", "el-GR,el;q=0.9", "he-IL,he;q=0.9", "hu-HU,hu;q=0.9", "nb-NO,nb;q=0.9",
          "ro-RO,ro;q=0.9", "sk-SK,sk;q=0.9", "uk-UA,uk;q=0.9", "hr-HR,hr;q=0.9", "bg-BG,bg;q=0.9",
          "lt-LT,lt;q=0.9", "sl-SI,sl;q=0.9"]

class Main:
    def Up_Blog_Views(self):
        self.url = input("Masukkan Url (www.example.com/blog.html): ")
        if self.url.startswith("www."):
            self.url = "https://" + self.url
        elif not self.url.startswith("https://www.") or not self.url.startswith("http://www."):
            self.url = "https://www." + self.url
        else:
            self.url = self.url
        self.berapa = int(input("Masukkan jumlah view blog yang diinginkan: "))
        self.jumlah = 1
        print(" => Kamu bisa meninggalkan jendela ini tetapi jangan menutupnya!\n => tools pertama ini cocok buat picoworkers")
        for _ in range(self.berapa):
            self.time_sleep = random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
            self.now = datetime.datetime.now()
            self.random_date = self.now - datetime.timedelta(days=random.randint(0, 30))
            with open('referer.txt', 'r') as referer_file:
                self.referer_list = referer_file.readlines()
                self.headers = {
                    'User-Agent': UserAgent().random,
                    'Date': self.random_date.strftime('%a, %d %b %Y %H:%M:%S GMT'),
                    'Accept-Language': random.choice(bahasa),
                    'Connection': 'keep-alive',
                    'Accept': random.choice(['*/*', 'text/html', 'application/xml', 'application/json']),
                    'Referer': 'https://' + random.choice(self.referer_list).strip()
                }
            self.response = requests.get(self.url, headers=self.headers)
            self.status_code = self.response.status_code
            if self.status_code == 200:
                print(f"{hijau}Berhasil menaikkan view +1 [ {self.jumlah} ]")
                self.jumlah += 1
            else:
                continue
            time.sleep(self.time_sleep)




    def Insta_Followers2(self, username, password, postingan):
        self.driver = webdriver.Chrome()
        self.link = "https://takipcitime.com/login"
        self.user_name = username
        self.user_pass = password
        self.post_ig = postingan

        self.driver.get(self.link)
        self.elemen_nama = self.driver.find_element(By.NAME, "username")
        self.elemen_nama.send_keys(self.user_name)
        self.elemen_password = self.driver.find_element(By.NAME, "password")
        self.elemen_password.send_keys(self.user_pass)
        self.send_button1 = self.driver.find_element(By.XPATH, "//button[@id='login_insta' and contains(@class, 'instaclass16') and contains(@class, 'instaclass17') and contains(@class, 'instaclass18') and contains(@class, 'instaclass19') and contains(text(), 'Giriş yap')]")
        self.send_button1.click()
        self.takipci_kazan_link11 = WebDriverWait(self.driver, 999999).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/tools/send-follower' and contains(@class, 'btn btn-primary') and contains(text(), 'KULLAN')]"))
        )
        self.takipci_kazan_link11.click()
        self.username_input = self.driver.find_element(By.NAME, "username")
        self.username_input.clear()
        self.username_input.send_keys(self.user_name)
        self.find_user_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-success']")
        self.find_user_button.click()
        self.adet_input = self.driver.find_element(By.NAME, "adet")
        self.adet_input.clear()
        self.adet_input.send_keys("75")
        self.start_button = self.driver.find_element(By.ID, "formTakipSubmitButton")
        self.start_button.click()
        time.sleep(250)
        
        self.driver.quit()



    def Insta_Followers1(self):
        self.driver = webdriver.Chrome()
        self.link = "https://takipcimx.net/login"
        self.user_name = input("Masukkan username ig: ")
        self.user_pass = input("Masukkan password ig: ")
        self.post_ig = input("Masukkan url postingan ig: ")

        self.driver.get(self.link)

        self.elemen_nama = self.driver.find_element(By.NAME, "username")
        self.elemen_nama.send_keys(self.user_name)

        self.elemen_password = self.driver.find_element(By.NAME, "password")
        self.elemen_password.send_keys(self.user_pass)

        self.send_button = self.driver.find_element(By.ID, "login_insta")
        self.send_button.click()
        
        self.takipci_kazan_link = WebDriverWait(self.driver, 999999).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/tools/send-follower') and contains(text(), 'Takipçi Kazan')]"))
        )
        self.takipci_kazan_link.click()

        self.input_element1 = self.driver.find_element(By.NAME, "username")
        self.input_element1.send_keys(self.user_name)

        self.button_element1 = self.driver.find_element(By.CLASS_NAME, "btn-success")
        self.button_element1.click()

        self.input_element = self.driver.find_element(By.NAME, "adet")
        self.input_element.clear()
        self.input_element.send_keys("150")

        self.start_button = self.driver.find_element(By.ID, "formTakipSubmitButton")
        self.start_button.click()

        print("wait ...")
        time.sleep(200)

        self.dropdown_toggle = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        self.dropdown_toggle.click()
        self.driver.execute_script("arguments[0].setAttribute('aria-expanded', 'true');", self.dropdown_toggle)

        self.hesap_ayarlar_link = self.driver.find_element(By.XPATH, "//a[@href='/account/settings' and @class='menu-toggler']")
        self.hesap_ayarlar_link.click()


        self.like_button = WebDriverWait(self.driver, 99999).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-block btn-primary' and contains(@href, '/tools/send-like')]"))
        )
        self.like_button.click()

        self.input_media_url = self.driver.find_element(By.NAME, "mediaUrl")
        self.input_media_url.clear()
        self.input_media_url.send_keys(self.post_ig)

        self.submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-success']")
        self.submit_button.click()

        self.input_adet = self.driver.find_element(By.NAME, "adet")
        self.input_adet.clear()
        self.input_adet.send_keys("50")

        self.submit_button = self.driver.find_element(By.ID, "formBegeniSubmitButton")
        self.submit_button.click()

        time.sleep(200)

        self.driver.quit()
        self.Insta_Followers2(self.user_name, self.user_pass, self.post_ig)



    def download_video_from_link(self):
        try:
            self.link = input("Masukkan url video: ")
            self.yt = YouTube(self.link)
            self.title = self.yt.title.replace(" ", "_").replace(",", "_").replace("?", "_")
            self.folder_name = "youtube_downloader"
            if not os.path.exists(self.folder_name):
                os.makedirs(self.folder_name)

            self.stream = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if self.stream is None:
                raise ValueError("Tidak ada stream dengan format .mp4 yang tersedia untuk diunduh.")

            self.file_number = "crying4nxiety"
            self.stream.download(output_path=self.folder_name, filename=f"{self.title}_{self.file_number}.mp4")
            print(f"{hijau}Video '{self.title}.mp4' berhasil diunduh dengan resolusi {self.stream.resolution} dan disimpan di folder '{self.folder_name}'.")
        except Exception as e:
            print(f"{merah}Terjadi kesalahan: {e}")

    def Infinity_Image_Generator(self):
        self.folder_name1 = "Image_Generator"
        if not os.path.exists(self.folder_name1):
            os.makedirs(self.folder_name1)
        while True:
            self.normal_prompt = input("Masukkan prompt (exit untuk keluar): ")
            if self.normal_prompt.lower() == 'exit':
                break
            self.encoded_prompt = self.normal_prompt.replace(" ", "%20")
            self.seed = str(random.randint(1, 9999999))
            self.ai_image_url = f"https://image.pollinations.ai/prompt/{self.encoded_prompt};seed={self.seed}.%204%20k%20resolution.width=1440&height=3200;HD,HQ;Ultra%20Detail"
            
            self.headers = {
                'User-Agent': UserAgent().random,
                'Accept-Language': random.choice(bahasa),
                'Date': datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'),
                'Connection': 'keep-alive',
                'Referer': 'https://chat.openai.com'
            }

            self.response = requests.get(self.ai_image_url, headers=self.headers)
            self.status_code = self.response.status_code

            if self.status_code == 200:
                self.image_prompt = self.normal_prompt.replace(" ", "_")
                self.file_name = os.path.join(self.folder_name1, f"{self.image_prompt}.jpg")

                with open(self.file_name, 'wb') as file:
                    file.write(self.response.content)

                self.image = Image.open(self.file_name)
                self.image = self.image.resize((self.image.width * 4, self.image.height * 4))
                self.image = self.image.filter(ImageFilter.SHARPEN)
                self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
                self.image = self.image.filter(ImageFilter.DETAIL)
                self.image = self.image.filter(ImageFilter.SMOOTH)

                self.processed_file_name = os.path.join(self.folder_name1, f"{self.image_prompt}_processed.jpg")
                self.image.save(self.processed_file_name)

                os.remove(self.file_name)

                print(f"{hijau}Gambar '{self.image_prompt}' berhasil diunduh dan diproses.")
            else:
                print(f"{merah}Gagal mengunduh gambar. Kode status: {self.status_code}")

    def __init__(self):
        self.list_tools = """1	++>	Up Blog/Website Views
2	++>	Up Instagram Followers, Likes (need login)
3	++>	Youtube Video Downloader (Max Resolution)
4	++>	Free Image Generator Unlimited
5	++>	Web Directories Finder (coming soom)
6	++>	Admin Login Page Finder (coming soom)
7	++>	Login Page Brute Force (coming soom)
------------------------+ Crying4nxiety +---------------------------\n\t\tI made this tool when i'm sad :)\n"""
        print(self.list_tools)
        while True:
            self.pilihan_user = int(input(putih+"Pilihanmu: "))
            if self.pilihan_user == 1:
                self.Up_Blog_Views()
            elif self.pilihan_user == 2:
                self.Insta_Followers1()
            elif self.pilihan_user == 3:
                self.download_video_from_link()
            elif self.pilihan_user == 4:
                self.Infinity_Image_Generator()
            elif self.pilihan_user == 5:
                pass
            elif self.pilihan_user == 6:
                pass
            elif self.pilihan_user == 7:
                pass
            else:
                continue
if __name__ == '__main__':
    Main()