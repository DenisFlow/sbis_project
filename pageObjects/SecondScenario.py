from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecondScenario:
    link_contacts_xpath = "//a[text()='Контакты']"
    contacts_region_xpath = "//div[@class='sbisru-Contacts']//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"
    list_of_partners_xpath = "//div[@class='ws-flexbox sbisru-Contacts-City__flex']//div[@name='itemsContainer']"
    link_kamchat_krai_xpath = "//ul[@class='sbis_ru-Region-Panel__list']//li//span[@title='Камчатский край']"
    url_kamchat_krai_string = "41-kamchatskij-kraj"
    # span_choice_your_region = "//div[@class='sbis_ru-Region-Panel__header-text']//span"

    weLinkContacts = None
    weDivListOfPartners = None
    weSpanRegion = None
    weLinkKamchatKrai = None

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

    def containRegion(self):
        try:
            self.weSpanRegion = self.driver.find_element(self.By.XPATH, self.contacts_region_xpath)
        except self.NoSuchElementException:
            return None
        else:
            return self.weSpanRegion


    def clickLinkRegion(self):
        if (self.weSpanRegion != None):
            self.weSpanRegion.click()
            return True
        else:
            if not self.containRegion():
                return False
            else:
                self.weSpanRegion.click()
                return True

    def containListOfPartners(self):
        try:
            self.weDivListOfPartners = self.driver.find_element(self.By.XPATH, self.list_of_partners_xpath)
        except self.NoSuchElementException:
            return None
        else:
            return self.weDivListOfPartners

    def containKamchatKrai(self):
        try:
            delay = 3  # seconds
            try:
                WebDriverWait(self.driver, delay).until(EC.presence_of_all_elements_located((self.By.XPATH, self.link_kamchat_krai_xpath)))
                print("Page is ready!")
                self.weLinkKamchatKrai = self.driver.find_element(self.By.XPATH, self.link_kamchat_krai_xpath)
            except TimeoutException:
                print("Loading took too much time!")
                return False
        except self.NoSuchElementException:
            return False
        else:
            return True

        
    def clickLinkKamchatKrai(self):
        if (self.weLinkKamchatKrai != None):
            self.weLinkKamchatKrai.click()
            return True
        else:
            if not self.containKamchatKrai():
                return False
            else:
                self.weLinkKamchatKrai.click()
                return True

    def waitTitleChangeToKamchatKrai(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.url_contains(self.url_kamchat_krai_string))
            print("Page is ready!")
            return True
        except TimeoutException:
            print("Loading took too much time!")
            return False
