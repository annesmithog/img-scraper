import os
import io
import time
import base64  
import requests
import click
from PIL import Image
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from save import make_folder
from output import info, warning

@click.command()
@click.option('--keyword', type=str, prompt='Search Keyword', help='Search Keyword')
@click.option('--count', type=int, default=300, prompt='Number of Images', help='Number of Images')
def main(keyword: str, count: int):
    # 準備
    query_url = quote(keyword)
    save_name = os.path.join('images', keyword)
    make_folder(save_name)
    info(f'Save Folder: {save_name}')
    driver = webdriver.Chrome()
    url = f'https://www.google.com/search?q={query_url}&tbm=isch'
    info(f'Target URL: {url}')
    driver.get(url)

    # 操作
    time.sleep(1)
    first_image_link = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[15]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/h3/a/div/div/div/g-img/img')
    first_image_link.click()
    ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
    
    i = 1
    for _ in range(count):
        print(f'{i}/{count}')
        try:
            # sFlh5c FyHeAf
            # sFlh5c FyHeAf iPVvYb
            driver.implicitly_wait(10)
            image_element = driver.find_element(By.CLASS_NAME, 'FyHeAf')
            image_url = image_element.get_attribute('src')

            if image_url and image_url.startswith('http'):
                image_response = requests.get(image_url)
                if image_url.endswith('.svg'):
                    image_name = f'{i}.svg'
                else:
                    image_name = f'{i}.jpg'
                image_path = os.path.join(save_name, image_name)
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_response.content)
            elif image_url and image_url.startswith('data:image/jpeg;base64'):
                image_data = image_url.split('base64,')[1]
                image = Image.open(io.BytesIO(base64.b64decode(image_data)))
                image_name = f'{i}'.jpg
                image_path = os.path.join(save_name, image_name)
                image.save(image_path)

            i += 1
        except StaleElementReferenceException as e:
            warning(f'{e.msg}')
        finally:
            ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
            time.sleep(1)

    if i > 0:
      info('DONE.')
      info(f'Save Folder: {save_name}')
    else:
        warning('FAIL.')
    
    driver.quit()

if __name__ == '__main__':
    main()
