#-*- coding:utf-8 -*-
class DictSort:
    def __init__(self, dict):
        self.mydict = dict

    def sort_by_throughput(self, obj):
        if "Gbps" in obj[1]:
            return float(obj[1].split()[0]) * 1000 * 1000 * 1000
        if "Mbps" in obj[1]:
            return float(obj[1].split()[0]) * 1000 * 1000
        if "Kbps" in obj[1]:
            return float(obj[1].split()[0]) * 1000
        if obj[1].split()[0] == "bps":
            return float(obj[1].split()[0])
        return 0

    def sort_by_value(slef, obj):
        return obj[1]

    def sort_by_key(self, obj):
        return obj[0]

    def do_sort(self, method):
        if method == "by_throughput":
            return sorted(self.mydict.items(), key=self.sort_by_throughput)
        elif method == "by_value":
            return sorted(self.mydict.items(), key=self.sort_by_value)
        elif method == "by_key":
            return sorted(self.mydict.items(), key=self.sort_by_key)
