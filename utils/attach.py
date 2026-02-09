import allure
from allure_commons.types import AttachmentType


def add_screenshot(driver):
    png = driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_console_logs(driver):
    log = "".join(f'{text}\n' for text in driver.execute("getLog", {'type': 'browser'})['value'])
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_page_source(driver):
    html = driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

def add_video(driver):
    video_url = "https://selenoid.autotests.cloud/video/" + driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + driver.session_id, AttachmentType.HTML, '.html')