from selenium import webdriver


class CompareResultPage(object):
    product_model_loc = "tbody>tr>th>a"
    product_throughput_loc = "tbody>tr:nth-child(13)>td[class='row-label']"
    through_out_dict = {}

    # get firewall throughput data of product on current web page
    def get_firewall_throughput(self):
        model_eles = driver.find_elements_by_css_selector(self.product_model_loc)
        model_name = []
        through_put_eles = driver.find_elements_by_css_selector(self.product_throughput_loc)
        through_put_data = []
        # store product model name to list
        for m in model_eles:
            model_name.append(m.text)
        # drag the page to Firewall Throughput
        driver.execute_script("window.scrollTo(0,800)")
        # store through_put_data to list
        for t in through_put_eles:
            through_put_data.append(t.text)
        # store product model name and through_put_data to dictionary
        ResultPage.through_out_dict = dict(zip(model_name, through_put_data))


