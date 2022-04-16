from logging import exception
import requests
import io
import hashlib
import os
from selenium import webdriver
from PIL import Image
from scraping_images import fetch_image_urls

def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content
    
    except Exception:
        pass

    # except Exception as e:
    #     print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception:
        pass
    # except Exception as e:
    #     print(f"ERROR - Could not save {url} - {e}")

def search_and_download(search_term:str,driver_path:str,target_path='./images',number_images=5):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
        
    for elem in res:
        persist_image(target_folder,elem)


terms = ['dog', 'cat']

DRIVER_PATH = r'C:\Users\Carlos Anaya\Desktop\NN_Image_Classifier\chromedriver.exe'

# for value in terms:
search_and_download(search_term="cat",driver_path=DRIVER_PATH,target_path='./images/cat', number_images=400)