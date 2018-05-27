# -*- coding:utf-8 -*-
from selenium import webdriver
from compare_page import ProductComparePage
from compare_result_page import CompareResultPage
from dict_sort import DictSort
from store_result import StoreResult


RESULT_FILE = "./compare_result.csv"
all_throughput = {}

if __name__ == '__main__':
    throughput_one_page = {}
    result_list = []
    driver = webdriver.Firefox()
    comp_page = ProductComparePage(driver)
    products = comp_page.get_product_list()
    print(products)
    driver.quit()

    # compare all products of given series
    step_length = 3
    for i in range(0, len(products), 3):
        driver = webdriver.Firefox()
        comp_page = ProductComparePage(driver)
        comp_page.select_product_in_list1(products[i])
        if i + 1 < len(products):
            comp_page.select_product_in_list2(products[i + 1])
        if i + 2 < len(products):
            comp_page.select_product_in_list3(products[i + 2])

        comp_page.click_compare()
        result_page = CompareResultPage(driver)
        throughput_one_page = result_page.get_firewall_throughput()
        driver.quit()
        all_throughput = dict(all_throughput, **throughput_one_page)
    result_list = DictSort(all_throughput).do_sort("by_throughput")
    StoreResult("./compare_result.csv").write_to_csv(result_list)
