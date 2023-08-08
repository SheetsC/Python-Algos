class Solution:
    def divis_by_seven(self, arr: list):
        sevens_list = []
        for char in arr:
            if char % 7 == 0:
                sevens_list.append(char)
        print(sevens_list)
    def find_odd1out(self, arrA: list, arrB: list):
        odd1out_list = []
        for char in arrA:
            if char not in arrB:
                odd1out_list.append(char)
        print(odd1out_list)