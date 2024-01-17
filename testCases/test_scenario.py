from pageObjects.FirstScenario import FirstScenario
from pageObjects.SecondScenario import SecondScenario
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class Test_001_First_scenario:
    sbisURL = "https://sbis.ru/"
    sbisContactsURL = "https://sbis.ru/contacts/"
    tensorURL = "https://tensor.ru/"
    tensorAboutURL = "https://tensor.ru/about"

    logger = LogGen.loggen()

    def test_homePageTitle(self):
        self.logger.info("*************** Test_001_FirstScenario ***************")
        self.logger.info("*************** Verifying Home Page Title test ***************")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisURL)
        act_title = self.driver.title
        if act_title == "СБИС — экосистема для бизнеса: учет, управление и коммуникации":
            self.logger.info("*************** Home page title test is passed ***************")
            self.driver.close()
            assert True
        else:
            self.driver.close()
            self.driver.get_screenshot_as_file('./Screenshots/test_homePageTitleNotExists.png')
            self.logger.info("*************** Home page title test is failed ***************")
            assert False


    def test_contactsPage(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisURL)
        self.fs = FirstScenario(self.driver, By, NoSuchElementException)
        self.logger.info("*************** Verifying Contacts Link Exists test ***************")
        if self.fs.containContacnts():
            self.logger.info("*************** Contacts Link Exists ***************")
        else:
            self.logger.info("*************** Contacts Link Not Exists ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_contactsPage_contactLinkNotExist.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Click Contacts Link test ***************")
        if self.fs.clickContacts():
            self.logger.info("*************** Click Contacts is passed ***************")
        else:
            self.logger.info("*************** Click Contacts is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_contactsPage_contactLinkNotClick.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying Contacts Page Title test ***************")
        act_title = self.driver.title
        if re.search("^СБИС Контакты — ", act_title) != None:
            self.logger.info("*************** Contacts page title test is passed ***************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************** Contacts page title test is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_contactsPage_homePageTitleNotExists.png')
            self.driver.close()
            assert False

    def test_tensorPage(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisContactsURL)
        self.fs = FirstScenario(self.driver, By, NoSuchElementException)
        self.logger.info("*************** Verifying Banner Tensor test ***************")
        if self.fs.containBannerTensor():
            self.logger.info("*************** Verifying Banner Tensor passed ***************")
        else:
            self.logger.info("*************** Verifying Banner Tensor failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPage_bannerTensorNotExists.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Click Banner Tensor test ***************")

        if len(self.driver.window_handles) != 1:
            self.logger.info("*************** Amount pages must be one ***************")
            assert False


        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle

        if self.fs.clickBannerTensor():
            self.logger.info("*************** Click Banner Tensor is passed ***************")
        else:
            self.logger.info("*************** Click Banner Tensor is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPage_bannerTensorNotClick.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying Tensor Page Title test ***************")

        try:
            wait.until(EC.number_of_windows_to_be(2))
        except:
            self.logger.info("*************** Amount pages must be two ***************")
            assert False

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        try:
            wait.until(EC.title_is("Тензор — IT-компания"))
            self.logger.info("*************** Tensor Page title test is passed ***************")
            self.driver.close()
            assert True
        except:
            self.driver.close()
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPage_PageTitleNotExists.png')
            self.logger.info("*************** Tensor Page title test is failed ***************")
            assert False

    def test_tensorPageAboutCompany(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.tensorURL)
        self.fs = FirstScenario(self.driver, By, NoSuchElementException)
        self.logger.info("*************** Verifying Block Power in people test ***************")
        if self.fs.containBlockPowerInPeople():
            self.logger.info("*************** Block Power in people passed ***************")
        else:
            self.logger.info("*************** Block Power in people failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPageAboutCompanyBlockPowerInPeople.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying Details link test ***************")
        if self.fs.containBlockPowerInPeopleChildDetails():
            self.logger.info("*************** Details link passed ***************")
        else:
            self.logger.info("*************** Details link failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPageAboutCompanyBlockPowerInPeopleChildDetails.png')
            self.driver.close()
            assert False

        if self.fs.clickBlockPowerInPeopleChildDetails():
            self.logger.info("*************** Click Details link is passed ***************")
        else:
            self.logger.info("*************** Click Details link is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPageAboutCompanyBlockPowerInPeopleChildDetailsClick.png')
            self.driver.close()
            assert False

        print("*************** Verifying Page About Company Title test ***************")
        act_title = self.driver.title
        if act_title == "О компании | Тензор — IT-компания":
            self.logger.info("*************** Page About Company title test is passed ***************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************** Page About Company test is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPageAboutCompanyTitle.png')
            self.driver.close()
            assert False

    def test_tensorPageAboutCompanyImagesSize(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.tensorAboutURL)
        self.fs = FirstScenario(self.driver, By, NoSuchElementException)

        self.logger.info("*************** Verifying Page Tensor About contain images test ***************")
        if self.fs.containElementsImagesAboutPage():
            self.logger.info("*************** Page Tensor About contain images passed ***************")
        else:
            self.logger.info("*************** Page Tensor About contain images failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_tensorPageAboutCompanyImagesContains.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying Image List Exist test ***************")

        elements = self.fs.weElementsImagesAboutPage

        if type(elements) is not list:
            self.logger.info("*************** Image List Exist test failed. Type is " + type(elements) + " ***************")
            self.driver.get_screenshot_as_file(
                './Screenshots/test_tensorPageAboutCompanyImagesNotList.png')
            self.driver.close()
            assert False
        else:
            self.logger.info("*************** Image List Exist test passed. Size is " + str(len(elements)) + " ***************")


        self.logger.info("*************** Verifying Image Size test ***************")
        height = width = None
        for index, element in enumerate(elements):

            print(index)
            print(element.tag_name)
            print(element)
            # assert 0
            print(element.size)
            elementHeight = element.size["height"]
            try:
                elementWidth = element.size["width"]
            except:
                self.logger.info("*************** error to get Width from dict ***************")
                assert False

            self.logger.info("*************** image " + str(index + 1) + ": height is " + str(elementHeight) + " and width is " + str(elementWidth))
            if index != 0:
                if height != elementHeight or width != elementWidth:
                    self.logger.info("*************** Image Size test failed. Image " + str(index + 1) + " ***************")
                    self.driver.get_screenshot_as_file(
                        './Screenshots/test_tensorPageAboutCompanyImagesContains' + str(index + 1) + '.png')
                    self.driver.close()
                    assert False
            else:
                height = elementHeight
                width = elementWidth


        self.logger.info("*************** Image Size test passed ***************")


class Test_002_First_scenario:
    sbisURL = "https://sbis.ru/"
    sbisContactsURL = "https://sbis.ru/contacts/"
    tensorURL = "https://tensor.ru/"
    tensorAboutURL = "https://tensor.ru/about"

    logger = LogGen.loggen()

    def test_homePageTitle(self):
        self.logger.info("*************** Test_002_SecondScenario ***************")
        self.logger.info("*************** Verifying Home Page Title test ***************")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisURL)
        act_title = self.driver.title
        if act_title == "СБИС — экосистема для бизнеса: учет, управление и коммуникации":
            self.logger.info("*************** Home page title test is passed ***************")
            self.driver.close()
            assert True
        else:
            self.driver.close()
            self.driver.get_screenshot_as_file('./Screenshots/test_homePageTitleNotExists.png')
            self.logger.info("*************** Home page title test is failed ***************")
            assert False

    def test_contactsPage(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisURL)
        self.ss = SecondScenario(self.driver, By, NoSuchElementException)
        self.logger.info("*************** Verifying Contacts Link Exists test ***************")
        if self.ss.containContacnts():
            self.logger.info("*************** Contacts Link Exists ***************")
        else:
            self.logger.info("*************** Contacts Link Not Exists ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_contactsPage_contactLinkNotExist.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Click Contacts Link test ***************")
        if self.ss.clickContacts():
            self.logger.info("*************** Click Contacts is passed ***************")
        else:
            self.logger.info("*************** Click Contacts is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_contactsPage_contactLinkNotClick.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying Contacts Page Title test ***************")
        act_title = self.driver.title
        if re.search("^СБИС Контакты — ", act_title) != None:
            self.logger.info("*************** Contacts page title test is passed ***************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************** Contacts page title test is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_contactsPage_homePageTitleNotExists.png')
            self.driver.close()
            assert False

    def test_toAnotherRegionChange(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisContactsURL)
        self.ss = SecondScenario(self.driver, By, NoSuchElementException)

        self.logger.info("*************** Verifying Element Region Exists test ***************")
        region_element = self.ss.containRegion()
        if region_element != None:
            self.logger.info("***************  Element Region Exists passed ***************")
        else:
            self.logger.info("***************  Element Region Exists failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionChangeRegionElementExistsFailed.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying My Region test ***************")
        if region_element.text == "Владимирская обл.":
            self.logger.info("*************** Verifying My Region passed ***************")
        else:
            self.logger.info("*************** Verifying My Region failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionChangeMyRegionFailed.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Verifying List Partners Exists test ***************")
        list_of_partners = self.ss.containListOfPartners()
        if list_of_partners != None:
            self.logger.info("*************** List Partners passed ***************")
        else:
            self.logger.info("*************** List Partners failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionChangeListPartnersFailed.png')
            self.driver.close()
            assert False

    def test_toAnotherRegionChange(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.sbisContactsURL)
        self.ss = SecondScenario(self.driver, By, NoSuchElementException)

        region_element = self.ss.containRegion()
        myRegionBeforeClick = region_element.text
        list_of_partners = self.ss.containListOfPartners()
        listOfPartnersBeforeClick = list_of_partners.text

        titleBeforeClick = self.driver.title

        self.logger.info("*************** Click Region Link test ***************")
        if self.ss.clickLinkRegion():
            self.logger.info("*************** Click Region is passed ***************")
        else:
            self.logger.info("*************** Click Region is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionChangeChangeToAnotherRegionClickFailed.png')
            self.driver.close()
            assert False


        self.logger.info("*************** Verifying Kamchatka Region Exist and Click Kamchatka Region Link test ***************")
        if self.ss.clickLinkKamchatKrai():
            self.logger.info("*************** Kamchatka Region Exist and Click Kamchatka Region is passed ***************")
        else:
            self.logger.info("*************** Kamchatka Region Exist and Click Kamchatka Region is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionChangeRegionClickFailed.png')
            self.driver.close()
            assert False

        self.logger.info("*************** URL Changed test ***************")
        if self.ss.waitTitleChangeToKamchatKrai():
            self.logger.info("*************** URL Changed is passed ***************")
        else:
            self.logger.info("*************** URL Changed is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionURLChangedFailed.png')
            self.driver.close()
            assert False

        region_element = self.ss.containRegion()
        myRegionAfterClick = region_element.text
        list_of_partners = self.ss.containListOfPartners()
        listOfPartnersAfterClick = list_of_partners.text
        titleAfterClick = self.driver.title


        self.logger.info("*************** Title Changed test ***************")
        if titleAfterClick != titleBeforeClick:
            self.logger.info("*************** Title Changed is passed. Now Title is " + titleAfterClick + " ***************")
        else:
            self.logger.info("*************** Title Changed is failed. Now Title is " + titleAfterClick + " ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionTitleChangedFailed.png')
            self.driver.close()
            assert False

        self.logger.info("*************** List of Partners Changed test ***************")
        if listOfPartnersAfterClick != listOfPartnersBeforeClick:
            self.logger.info("*************** List of Partners Changed is passed ***************")
        else:
            self.logger.info("*************** List of Partners Changed is failed ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionListOfPartnersChangedFailed.png')
            self.driver.close()
            assert False

        self.logger.info("*************** Region Changed test ***************")
        if myRegionBeforeClick != myRegionAfterClick:
            self.logger.info("*************** Region Changed is passed. Result now is " + myRegionAfterClick + ". Was " + myRegionBeforeClick + " ***************")
        else:
            self.logger.info("*************** Region Changed is failed. Result now is " + myRegionAfterClick + ". Was " + myRegionBeforeClick + " ***************")
            self.driver.get_screenshot_as_file('./Screenshots/test_toAnotherRegionChanged.png')
            self.driver.close()
            assert False


