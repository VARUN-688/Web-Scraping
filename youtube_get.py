from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pytube import YouTube
def automation(search:str):
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.get("https://www.youtube.com")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.NAME, "search_query").send_keys(search)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "style-scope ytd-searchbox").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "style-scope ytd-video-renderer").click()
    #
    #
    # print(driver.current_url)
    video_url = driver.current_url

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution stream (you can customize based on your preference)
    video_stream_144p = yt.streams.filter(res="360p").first()

    # Get the title of the video
    video_title = yt.title

    # Print video information
    print(f"Downloading: {video_title} ({video_stream_144p.resolution})")

    # Download the video
    video_stream_144p.download()

    print("Download complete!")
    time.sleep(1000)
if __name__=="__main__":
    automation(input('enter the search-> '))
