import os
import time
from selenium import webdriver

def download_report():
    download_dir = "path_to_download_folder"  # Specify your download folder path
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # Replace with your ChromeDriver path

    # Navigate to the page where the file can be downloaded
    driver.get('https://example.com/report')  # Replace with the actual download page URL
    
    # Click the download button for the report
    download_button = driver.find_element_by_xpath("//button[@id='download']")
    download_button.click()

    # Wait for the download to complete (adjust the sleep time as per your needs)
    time.sleep(10)

    # Verify the file download
    files = os.listdir(download_dir)
    downloaded_file = [f for f in files if f.endswith('.pdf')]
    
    if downloaded_file:
        print(f"Report downloaded successfully: {downloaded_file[0]}")
    else:
        print("Download failed!")

    driver.quit()

if __name__ == "__main__":
    download_report()
