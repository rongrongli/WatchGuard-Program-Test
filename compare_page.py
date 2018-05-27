from basepage import BasePage


class ProductComparePage(BasePage):
    # product compare url
    compare_url = "https://www.watchguard.com/wgrd-products/appliances-compare"
    # select product
    product_select1_loc = "#p1"
    product_select2_loc = "#p2"
    product_select3_loc = "#p3"
    # compare button
    compare_button_loc = "input[value='Compare Appliances']"
    # compare series
    series_list = [
        "WatchGuard® Firebox M Series",
        "WatchGuard Firebox T Series"]

    product_list = []

    def __init__(self, driver):
        super(ProductComparePage, self).__init__(driver)
        self.driver.get(self.compare_url)

    # select one product under select_button
    def select_product(self, select_button, product_name):
        product_xpath = '//option[text()="' + product_name + '"]'
        select_list = self.driver.find_element_by_css_selector(select_button)
        select_list.find_element_by_xpath("." + product_xpath).click()

    # select one product under select 1
    def select_product_in_list1(self, product_name):
        self.select_product(self.product_select1_loc, product_name)

    # select one product under select 2
    def select_product_in_list2(self, product_name):
        self.select_product(self.product_select2_loc, product_name)

    # select one product under select 3
    def select_product_in_list3(self, product_name):
        self.select_product(self.product_select3_loc, product_name)

    # click compare appliances button
    def click_compare(self):
        self.driver.find_element_by_css_selector(
            self.compare_button_loc).click()
        return self.driver.current_url

    # get all products of the given series and store into list
    def get_product_list(self):
        for s in self.series_list:
            select1 = self.driver.find_element_by_css_selector(
                self.product_select1_loc)
            options = select1.find_elements_by_css_selector(
                'optgroup[label="' + s + '"]>option')
            for option in options:
                self.product_list.append(option.text)
        return self.product_list
