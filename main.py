from selenium import webdriver
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

driver = webdriver.Chrome()
def imageScraper(query, num_images):
    try:
        save_path = os.path.join(os.getcwd(), "sample_data")
        os.makedirs(save_path, exist_ok=True)
        url = "https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"
        driver.get(url.format(s=query))  
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'H8Rx8c')]//img[contains(@class,'YQ4gaf')]")))
        imgResults = driver.find_elements(By.XPATH, "//div[contains(@class,'H8Rx8c')]//img[contains(@class,'YQ4gaf')]")
        for i, img_element in enumerate(imgResults[:num_images]):
            try:
                driver.execute_script("arguments[0].click();", img_element)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'YsLeY')]")))
                img_url_element = driver.find_element(By.XPATH, "//a[contains(@class,'YsLeY')]")
                child_img = img_url_element.find_element(By.XPATH, ".//img")
                img_url = child_img.get_attribute("src")
                img_name = f"{query}_{i+1}.jpg"
                img_path = os.path.join(save_path, img_name)
                response = requests.get(img_url, stream=True)
                with open(img_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                with Image.open(img_path) as img:
                    img = img.resize((224, 224), Image.Resampling.LANCZOS)
                    img.save(img_path)

                print(f"Image {i+1} downloaded successfully")
            except Exception as e:
                print(f"Image Download Failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

query = "orchid"
num_images = 10
imageScraper(query, num_images)

driver.quit()

"""
REFERENCES
https://medium.com/@nithishreddy0627/a-beginners-guide-to-image-scraping-with-python-and-selenium-38ec419be5ff
https://deepnote.com/app/dennis-dfa8/Web-Scraping-Images-5e2baaa2-d24f-4d47-a124-687639818a7f
"""