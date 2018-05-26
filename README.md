# WatchGuard Program Test
## Program Archetecture
### Program Modules
 1. base_page: 基础公共Page Object对象，用于继承
 2. compare_page: 选择产品进行对比页面的Page Object 对象。对外提供方法如下：
    ```
    get_product_list: 获取默认指定系列的所有产品列表
    select_product_in_list1： 选择产品1
    select_product_in_list2: 选择产品2
    select_product_in_list3: 选择产品3
    click_compare: 点击对比按钮
    ```
3. compare_result_page: 产品对比结果页面的Page Object对象，包含方法：
    ```
    get_firewall_throughput: 获取所有产品的firewall_throughput值，返回字典
    ```
4. dict_sort: 排序模块，对传入的字典数据，是用do_sort方法，按照指定的方法进行排序，返回排序后的列表。提供的排序方法有：
    ```
    按流量进行排序：DictSort.do_sort("by_throughput")
    按字典Key进行排序：DictSort.do_sort("by_key")
    按字典Value进行排序：DictSort.do_so
    ```
5. store_result: 存储模块：将传入的数据是用对应的存储方法，存入对应文件。目前提供的存储方法有：
    ```
    write_to_csv(self, data_list): 将传入的列表数据，按行存入CSV指定的文件
    ```
6. product_compare: 程序主模块，调用各个页面对象、排序以及存储，完成项目任务。 具体实现：
    * 通过compare_page获取所有产品列表
    * 循环遍历比较compare_page每3个产品，并点击比较按钮
    * 通过compare_result_page获取3个产品的firewall throughput结果，并返回字典数据
    * 将所有的结果字典数据，通过dict_sort模块，按流量进行排序
    * 将排序结果，通过store_result存入csv文件
