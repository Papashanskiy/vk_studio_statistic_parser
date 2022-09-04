from selenium.common import exceptions as selenium_exceptions
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time
from environ import Env

env = Env()
Env.read_env('../.env')


def log_click(log, pas, driver):
    campo_log = driver.find_element(By.XPATH, '//*[@id="index_email"]')
    time.sleep(1)
    campo_log.click()
    campo_log.send_keys(log)
    time.sleep(2)

    campo_log.send_keys(Keys.ENTER)

    time.sleep(2)

    compo_use_password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[7]/div/button[2]/span')
    compo_use_password.click()
    time.sleep(2)


    campo_password = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input')
    time.sleep(1)
    campo_password.click()
    campo_password.send_keys(pas)
    time.sleep(1)
    campo_password.send_keys(Keys.ENTER)
    time.sleep(2)


def get_single_artist_info(driver):
    artist = {}

    artist['title'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/div/h2/span').text
    artist['description'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/div/span').text
    artist['now_listening'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[1]/div[2]/div[2]/h2').text
    artist['listeners'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[2]/div[2]/div[2]/h2').text
    artist['listeners_plus'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[2]/div[2]/div[2]/span').text
    artist['added'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[3]/div[2]/div[2]/h2').text
    artist['added_plus'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[3]/div[2]/div[2]/span').text
    artist['shared'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[4]/div[2]/div[2]/h2').text
    artist['shared_plus'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[4]/div[2]/div[2]/span').text
    artist['listeners'] = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[3]/div[4]/div[2]/div[2]/span').text

    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/section[1]/div/header/span/div/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/section[1]/div/header/span/div/section/div[2]/div/div/div/div[1]/div/div').click()

    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[2]/section/div/header/span/div/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[2]/section/div/header/span/div/section/div[2]/div/div/div/div[1]/div/div/span').click()

    artist['attachments'] = {}
    artist['attachments']['count_users'] = driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[2]/section/div/div/div[1]/div/h2')

    artist['attachments']['most_mentioned_tracks_and_releases'] = []
    attach_list = []
    try:
        for i in range(1, 11):
            attach_list.append(driver(By.XPATH, f'/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[2]/section/div/div/a[{i}]'))
    except selenium_exceptions.NoSuchElementException as e:
        pass

    for attach in attach_list:
        info = {}
        info['track_name'] = attach.find_element(By.CLASS_NAME, 'OverviewMentions__title').text
        info['artist_name'] = attach.find_element(By.CLASS_NAME, 'OverviewMentions__trackArtist').text
        info['attach_count'] = attach.find_element(By.XPATH, './/h3').text
        artist['attachments']['most_mentioned_tracks_and_releases'].append(info)    # todo separate tracks and releases

    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[1]/div[1]/section/div/header/span/div/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[1]/div[1]/section/div/header/span/div/section/div[2]/div/div/div/div[1]/div/div/span').click()

    popular_tracks = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[1]/div[1]/section/div/div/div')
    popular_tracks_list = popular_tracks.find_elements(By.XPATH, './/a')
    artist['popular_tracks'] = []
    for popular_track in popular_tracks_list:
        track_info = {}
        track_info['title'] = popular_track.text
        track_info['count'] = popular_track.find_element(By.XPATH, './/h3')
        artist['popular_tracks'].append(track_info)


    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[1]/div[2]/section/div/header/span/div/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[1]/div[2]/section/div/header/span/div/section/div[2]/div/div/div/div[1]/div/div/span').click()

    popular_tracks = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[1]/div[2]/section/div/div/div')
    popular_tracks_list = popular_tracks.find_elements(By.XPATH, './/a')
    artist['popular_tracks'] = []
    for popular_track in popular_tracks_list:
        track_info = {}
        track_info['title'] = popular_track.find_element(By.XPATH, './/span[1]').text
        track_info['count'] = popular_track.find_element(By.XPATH, './/h3').text
        artist['popular_tracks'].append(track_info)


    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[2]/div[1]/section/div/header/span/div/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[2]/div[1]/section/div/header/span/div/section/div[2]/div/div/div/div[1]/div/div/span').click()

    popular_tracks = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[2]/div[1]/section/div/div/div')
    popular_tracks_list = popular_tracks.find_elements(By.XPATH, './/a')
    artist['popular_tracks'] = []
    for popular_track in popular_tracks_list:
        track_info = {}
        track_info['title'] = popular_track.text
        track_info['count'] = popular_track.find_element(By.XPATH, './/h3').text
        artist['popular_tracks'].append(track_info)


    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[2]/div[1]/section/div/header/span/div/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[2]/div[1]/section/div/header/span/div/section/div[2]/div/div/div/div[1]/div/div/span').click()

    popular_tracks = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[1]/div[2]/div[1]/section/div/div/div')
    popular_tracks_list = popular_tracks.find_elements(By.XPATH, './/a')
    artist['popular_tracks'] = []
    for popular_track in popular_tracks_list:
        track_info = {}
        track_info['title'] = popular_track.text
        track_info['count'] = popular_track.find_element(By.XPATH, './/h3').text
        artist['popular_tracks'].append(track_info)



    print(1)



def get_artists_info(driver):
    driver.get('https://vk.com/studio')
    time.sleep(2)
    artists_list = []
    try:
        for i in range(1, 1000):
            artists_list.append(driver.find_element(
                'xpath', f'/html/body/div[7]/div/div/div/div[2]/div/div/div/div/section/div/div[2]/div[{i}]'))
    except selenium_exceptions.NoSuchElementException as e:
        pass




if __name__ == '__main__':

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://vk.com/')

    log = env('VK_LOGIN')
    password = env('VK_PASSWORD')
    log_click(log, password, driver)

    driver.get('https://vk.com/studio')
    time.sleep(0.5)

    # artists_list = []

    a_list = []
    try:
        for i in range(1, 1000):
            artist = driver.find_element(By.XPATH, f'/html/body/div[7]/div/div/div/div[2]/div/div/div/div/section/div/div[2]/div[{i}]')
            a_list.append(artist)
    except:
        pass


    print(a_list)

    time.sleep(0.5)

    # artists_list.text.split('\n')
