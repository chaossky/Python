import webbrowser
import time

count = 0
sleep_time = 5  # 탭을 여는 간격 (초 단위)  
# 1. 파일에서 URL 목록 읽기
with open('urls.txt', 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# 2. 각 URL을 새 탭에서 열기
for url in urls:
    count += 1
    if (count%5)==0:
        sleep_time=10
    else:
        sleep_time=1# 최대 5개 탭 열기
    webbrowser.open_new_tab(url)
    time.sleep(sleep_time)  # 너무 빨리 열리지 않게 잠깐 대기 (필수는 아님)