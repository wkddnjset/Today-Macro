from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

IP_list = open("./GigaIP(유료프록시).txt", 'r').readlines()[2:]
url_page = input("접속할 페이지 URL을 입력해주세요 : ")

for idx, ip in enumerate(IP_list):
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = ip
    prox.socks_proxy = ip
    prox.ssl_proxy = ip

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(desired_capabilities=capabilities)
    time.sleep(0.5)
    driver.get(url_page)
    time.sleep(4)
    driver.close()
    time.sleep(0.5)
    print(str(idx)+"번째 작업 완료..")