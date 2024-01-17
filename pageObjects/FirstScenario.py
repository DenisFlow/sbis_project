from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class FirstScenario:
    link_contacts_xpath = "//a[text()='Контакты']"
    link_banner_xpath = "//img[contains(@alt, 'Разработчик системы СБИС — компания «Тензор»')]/.."
    banner_power_in_people_xpath = "//p[text()='Сила в людях']/.."
    banner_power_in_people_child_details_xpath = banner_power_in_people_xpath + "//a[text()='Подробнее']"
    tensor_about_page_images_class_name = "tensor_ru-About__block3-image-wrapper"
    tensor_about_page_images_xpath = "//div[@class='tensor_ru-About__block3-image-wrapper']//img"
    # tensor_about_page_images_xpath = "//div[@class='tensor_ru-About__block3-image-wrapper']//img[@loading='eager']"

    weLinkContacts = None
    weBannerTensor = None
    weBlockPowerInPeople = None
    weBlockPowerInPeopleChildDetails = None
    weElementsImagesAboutPage = None

    def __init__(self, driver, bBy, exNoSuchElementException):
        self.driver = driver
        self.By = bBy
        self.NoSuchElementException = exNoSuchElementException

    def containContacnts(self):
        try:
            self.weLinkContacts =  self.driver.find_element(self.By.XPATH, self.link_contacts_xpath)
        except self.NoSuchElementException:
            return False
        else:
            return True

    def clickContacts(self):
        if (self.weLinkContacts != None):
            self.weLinkContacts.click()
            return True
        else:
            if not self.containContacnts():
                return False
            else:
                self.weLinkContacts.click()
                return True

    def containBannerTensor(self):
        try:
            self.weBannerTensor = self.driver.find_element(self.By.XPATH, self.link_banner_xpath)
        except self.NoSuchElementException:
            return False
        else:
            return True

    def clickBannerTensor(self):
        if (self.weBannerTensor != None):
            self.driver.execute_script("arguments[0].click();", self.weBannerTensor)
            return True
        else:
            if not self.containBannerTensor():
                return False
            else:
                self.driver.execute_script("arguments[0].click();", self.weBannerTensor)
                return True

    def containBlockPowerInPeople(self):
        try:
            self.weBlockPowerInPeople = self.driver.find_element(self.By.XPATH, self.banner_power_in_people_xpath)
        except self.NoSuchElementException:
            return False
        else:
            return True

    def containBlockPowerInPeopleChildDetails(self):
        try:
            self.weBlockPowerInPeopleChildDetails = self.driver.find_element(self.By.XPATH, self.banner_power_in_people_child_details_xpath)
        except self.NoSuchElementException:
            return False
        else:
            return True

    def clickBlockPowerInPeopleChildDetails(self):
        if (self.weBlockPowerInPeopleChildDetails != None):
            self.driver.execute_script("arguments[0].click();", self.weBlockPowerInPeopleChildDetails)
            return True
        else:
            if not self.containBlockPowerInPeopleChildDetails():
                return False
            else:
                self.driver.execute_script("arguments[0].click();", self.weBlockPowerInPeopleChildDetails)
                return True

    def containElementsImagesAboutPage(self):
        try:
            delay = 3  # seconds
            try:
                # myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_all_elements_located((self.By.XPATH, self.tensor_about_page_images_class_name)))
                WebDriverWait(self.driver, delay).until(EC.presence_of_all_elements_located((self.By.CLASS_NAME, self.tensor_about_page_images_class_name)))
                print("Page is ready!")
                # self.weElementsImagesAboutPage = self.driver.find_elements(self.By.XPATH, self.tensor_about_page_images_class_name)
                self.weElementsImagesAboutPage = self.driver.find_elements(self.By.XPATH, self.tensor_about_page_images_xpath)
            except TimeoutException:
                print("Loading took too much time!")
                return False
        except self.NoSuchElementException:
            return False
        else:
            return True