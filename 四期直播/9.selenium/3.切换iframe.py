from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.binary_location = r"D:\SoftWare\Google\Chrome\Application\chrome.exe"
web = Chrome(options=options)
web.get("http://www.wbdy.tv/play/69328_1_1.html")
iframe = web.find_element(By.XPATH, '//iframe[@id="mplay"]')
web.switch_to.frame(iframe)  # 切入到iframe中
# 然后才可以提取iframe中的内容
video = web.find_element(By.XPATH, '//video')
src = video.get_property("src")
print(src)
web.switch_to.parent_frame()  # 切换到上层frame




