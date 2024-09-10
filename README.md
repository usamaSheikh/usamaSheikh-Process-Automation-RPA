# RPA Automation Project: Web Form, File Download, and Organization

## Project Overview
Automate the process of:
  1. Filling out a web form on a website. 
  2. Downloading a PDF report from the website after form submission. 
  3. Renaming and organizing the downloaded file into a specific folder structure. 

This will demonstrate automating manual processes like form filling, file downloading, renaming, and organizing into folders.

### Technologies Used:
- Python
- Selenium for browser automation
- `requests` for file handling

### Project Structure:
- `form_filler.py`: Automates filling out a web form.
- `file_downloader.py`: Automates downloading a PDF report.
- `file_organizer.py`: Renames and organizes the downloaded files.

### How to Run:
1. Clone this repository.
2. Install the required dependencies:
    ```bash
    pip install selenium requests bs4
    ```
3. Download ChromeDriver or a WebDriver for your browser and update the `executable_path` in the scripts.
4. Run each script:
    ```bash
    python form_filler.py
    python file_downloader.py
    python file_organizer.py
    ```

### Set Up the WebDriver:
  1. Download the appropriate WebDriver (e.g., ChromeDriver) for your browser.
  2. Place the WebDriver in your project directory or specify the path in the executable_path parameter in the code.
 
  Run Each Script:

  ### Run form_filler.py:
      python form_filler.py
      This will fill out a form and take a screenshot of the submission.

  ### Run file_downloader.py:
      python file_downloader.py
      This will download a PDF report from the website.

  ### Run file_organizer.py:
      python file_organizer.py
      This will rename and organize the downloaded PDF file.


### Screenshots:
![image](https://github.com/user-attachments/assets/6e6eefb6-7b7e-45df-8b0f-b0a18f65152c)

