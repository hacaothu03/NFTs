from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Khởi tạo trình duyệt Selenium
driver = webdriver.Chrome()  # Bạn cần cài đặt Chrome WebDriver trước

# URL của trang cointelegraph.com với các bài viết liên quan đến NFTs hoặc blockchain
url = "https://cointelegraph.com/search?query=nft"

# Mở trang web bằng trình duyệt
driver.get(url)

# Chờ một khoảng thời gian để trang web tải đầy đủ nội dung động (tùy vào tốc độ internet)
time.sleep(5)

# Lấy thông tin từ các bài viết
article_data_list = []

# Tìm các phần tử bài viết
articles = driver.find_elements(By.CLASS_NAME, "post-item")

for article in articles:
    title = article.find_element(By.CLASS_NAME, "header").text.strip()
    author = article.find_element(By.CLASS_NAME, "author").text.strip()
    date = article.find_element(By.CLASS_NAME, "date").text.strip()
    tags = [tag.text.strip() for tag in article.find_elements(By.CLASS_NAME, "post-preview-tags-tag")]

    # Lưu thông tin từ bài viết vào một dictionary
    article_data = {
        "title": title,
        "author": author,
        "date": date,
        "tags": tags
    }

    article_data_list.append(article_data)

# Đóng trình duyệt
driver.quit()

# Lưu trữ dữ liệu vào tệp JSON
with open('cointelegraph_articles.json', 'w', encoding='utf-8') as json_file:
    json.dump(article_data_list, json_file, ensure_ascii=False, indent=4)

# Lưu trữ dữ liệu vào tệp CSV (tùy chọn)
import csv
with open('cointelegraph_articles.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'author', 'date', 'tag'])
    for article_data in article_data_list:
        writer.writerow([article_data['title'], article_data['author'], article_data['date'], ', '.join(article_data['tags'])])
