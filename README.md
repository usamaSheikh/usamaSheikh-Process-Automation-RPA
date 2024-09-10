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
    
### Screenshots:
![image](https://github.com/user-attachments/assets/6e6eefb6-7b7e-45df-8b0f-b0a18f65152c)

