from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, os


class XPATH:
    def __init__(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.media_dir = os.path.join(self.base_dir, "media")
        os.makedirs(self.media_dir, exist_ok=True)
        self.options = webdriver.ChromeOptions()
        self.prefs = {
                "download.default_directory": self.media_dir,
                "download.prompt_for_download": False,
                "safebrowsing.enabled": True
            }
        self.options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(options=self.options)
        self.site()
        assert "DEMOQA" in self.driver.title, "Error: Page title is incorrect"

    def site(self):
        self.driver.get('https://demoqa.com/')

    def go_to_elements(self):
        element_go_to_elements = self.driver.find_element(By.XPATH, "//div//h5[text()='Elements']")
        assert element_go_to_elements.is_displayed(), 'Error: Element not found'
        self.driver.execute_script("arguments[0].click();", element_go_to_elements)
        time.sleep(3)
        assert "elements" in self.driver.current_url, "Error: Navigation to Elements page failed"

    def select_li(self, index):
        element_li = self.driver.find_element(By.XPATH, f"//ul//li[@id='item-{index}']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_li)
        assert element_li.is_displayed(), f"Error: List item with index {index} not found"
        element_li.click()
        time.sleep(3)

    def fill_form(self, id, value, x):
        if x < 3:
            element_input = self.driver.find_element(By.XPATH, f"//input[@id='{id}']")
            assert element_input.is_displayed(), f"Error: Input with id '{id}' not found"
            self.driver.execute_script('arguments[0].scrollIntoView(true);', element_input)
            element_input.click()
            element_input.send_keys(value)
            time.sleep(3)
        else:
            element_input = self.driver.find_element(By.XPATH, f"//textarea[@id='{id}']")
            assert element_input.is_displayed(), f"Error: Textarea with id '{id}' not found"
            self.driver.execute_script('arguments[0].scrollIntoView(true);', element_input)
            element_input.click()
            element_input.send_keys(value)
            time.sleep(3)

    def submit_form(self):
        element_submit = self.driver.find_element(By.XPATH, "//div//button[@id='submit' and text()='Submit']")
        assert element_submit.is_displayed(), "Error: Submit button not found"
        element_submit.click()
        time.sleep(3)

    def select_checkboxes(self):
        element_checkbox_main = self.driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
        assert element_checkbox_main.is_displayed(), "Error: Main checkbox not found"
        element_checkbox_main.click()
        time.sleep(2)
        element_checkbox_main_open = self.driver.execute_script(
            "return document.querySelector('button.rct-collapse')"
        )
        assert element_checkbox_main_open is not None, "Error: Collapse button not found"
        self.driver.execute_script("arguments[0].click();", element_checkbox_main_open)
        time.sleep(2)
        element_cb_doc = self.driver.find_element(By.XPATH, "//label[@for='tree-node-documents']")
        assert element_cb_doc.is_displayed(), "Error: Documents checkbox not found"
        element_cb_doc.click()
        time.sleep(3)

    def select_radiobuttons(self, id):
        element_radiobutton = self.driver.find_element(By.XPATH, f'//label[@for="{id}"]')
        assert element_radiobutton.is_displayed(), f"Error: Radio button with id '{id}' not found"
        element_radiobutton.click()
        time.sleep(2)

    def add_record(self):
        element_add = self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")
        assert element_add.is_displayed(), "Error: Add button not found"
        element_add.click()
        time.sleep(2)

    def fill_modal_form(self, id, value):
        element_input = self.driver.find_element(By.XPATH, f"//input[@id='{id}']")
        assert element_input.is_displayed(), f"Error: Modal input with id '{id}' not found"
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element_input)
        element_input.click()
        element_input.send_keys(value)
        time.sleep(2)

    def select_count_records(self, count):
        element_select = self.driver.find_element(By.XPATH, f"//select//option[@value='{count}']")
        assert element_select.is_displayed(), f"Error: Option for count '{count}' not found"
        element_select.click()
        time.sleep(2)

    def next(self):
        element_next = self.driver.find_element(By.XPATH, "//div//button[text()='Next']")
        assert element_next.is_displayed(), "Error: Next button not found"
        element_next.click()
        time.sleep(2)

    def delete_record_from_table(self, id):
        element_delete = self.driver.find_element(By.XPATH, f"//span[@id='delete-record-{id}']")
        assert element_delete.is_displayed(), f"Error: Delete button for record '{id}' not found"
        element_delete.click()
        time.sleep(2)

    def edit_record_from_table(self, id):
        element_edit = self.driver.find_element(By.XPATH, f"//span[@id='edit-record-{id}']")
        assert element_edit.is_displayed(), f"Error: Edit button for record '{id}' not found"
        element_edit.click()
        time.sleep(2)

    def clear_modal_form(self, id):
        element_input = self.driver.find_element(By.XPATH, f"//input[@id='{id}']")
        assert element_input.is_displayed(), f"Error: Modal input with id '{id}' not found"
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element_input)
        element_input.click()
        element_input.clear()
        time.sleep(2)

    def search_record(self, value):
        element_search = self.driver.find_element(By.XPATH, f"//div//input[@id='searchBox']")
        assert element_search.is_displayed(), "Error: Search box not found"
        element_search.click()
        element_search.send_keys(value)
        time.sleep(2)

    def click_button(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, f"//div//button[@id='doubleClickBtn']")
        assert element.is_displayed(), "Error: Click Me button not found"
        actions.double_click(element).perform()
        time.sleep(3)

        element = self.driver.find_element(By.XPATH, f"//div//button[@id='rightClickBtn']")
        assert element.is_displayed(), "Error: Right Click button not found"
        actions.context_click(element).perform()
        time.sleep(3)

        time.sleep(2)

    def go_to_link(self, id):
        element = self.driver.find_element(By.XPATH, f'//p//a[@id="{id}"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

        time.sleep(2)
        element_result = self.driver.find_element(By.XPATH, '//p[@id="linkResponse"]')
        assert element_result.is_displayed(), 'Error: Result text not found'
        time.sleep(2)

        time.sleep(1)
        element_result = self.driver.find_element(By.XPATH, '//p[@id="linkResponse"]')
        assert element_result.is_displayed(), 'Error: Result text not found'
        time.sleep(1)


    def click_on_link_by_text(self, text):
        element = self.driver.find_element(By.XPATH, f'//a[text()="{text}"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

        time.sleep(3)

    def select_li_codes(self, code):
        element = self.driver.find_element(By.XPATH, f'//li//a[text()="{code}"]')
        element.click()
        time.sleep(3)

    def upload_file(self, path):
        element = self.driver.find_element(By.XPATH, "//input[@id='uploadFile']")
        absolute_path = os.path.abspath(path)
        element.send_keys(absolute_path)
        time.sleep(3)

    def download_file(self):
        element = self.driver.find_element(By.XPATH, "//div//a[@id='downloadButton']")
        time.sleep(2)

    def select_li_codes(self, code):
        element = self.driver.find_element(By.XPATH, f'//li[text()="{code}"]')
        element.click()
        time.sleep(3)