# Automation Script
import os
import shutil
import time

# 1. Creating a Directory
os.makedirs("example_directory", exist_ok=True)

# 2. Renaming a File
os.rename("old_file.txt", "new_file.txt")

# 3. Copying a File
shutil.copy("source.txt", "destination.txt")

# 4. Moving a File
shutil.move("file_to_move.txt", "new_location/")

# 5. Deleting a File
os.remove("file_to_delete.txt")

# 6. Listing Files in a Directory
files = os.listdir(".")
print("Files in current directory:", files)

# 7. Current Working Directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# 8. Getting Environment Variables
home_directory = os.environ.get("HOME")
print("Home Directory:", home_directory)

# 9. Sleep Function
print("Waiting for 3 seconds...")
time.sleep(3)
print("Done waiting!")

# 10. Creating a Backup
shutil.copytree("example_directory", "example_directory_backup")

# 11. Writing to a File
with open("output.txt", "w") as file:
    file.write("Hello, this is an automated script!")

# 12. Reading from a File
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# 13. Finding Files with a Specific Extension
for file in os.listdir("."):
    if file.endswith(".txt"):
        print("Text file found:", file)

# 14. Monitoring File Changes
import time

path_to_watch = "example_directory"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while True:
    time.sleep(10)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: print("Added: ", ", ".join(added))
    if removed: print("Removed: ", ", ".join(removed))
    before = after

# 15. Automating Email Sending (using smtplib)
import smtplib

def send_email(subject, body, to):
    from_email = "your_email@example.com"
    password = "your_password"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to, message)

send_email("Test Subject", "This is a test email.", "recipient@example.com")

# 16. Downloading Files
import requests

url = "https://example.com/file.txt"
response = requests.get(url)
with open("downloaded_file.txt", "wb") as file:
    file.write(response.content)

# 17. Automating Web Browsing (using Selenium)
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
time.sleep(5)  # Wait for the page to load
driver.quit()

# 18. Scheduling Tasks (using schedule library)
import schedule

def job():
    print("Job is running...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# 19. Generating Random Numbers
import random

random_number = random.randint(1, 100)
print("Random number:", random_number)

# 20. Converting Excel Files to CSV (using pandas)
import pandas as pd

df = pd.read_excel("data.xlsx")
df.to_csv("data.csv", index=False)
