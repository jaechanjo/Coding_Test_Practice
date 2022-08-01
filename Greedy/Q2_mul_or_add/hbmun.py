class Cal:
    def __init__(self, num):
        self.num = num
        self.result = 0

    def main(self):
        pre_num = self.num[0]
        for i in range(1, len(self.num)):
            next_num = self.num[i]
            if pre_num == 0 or next_num == 0\
                    or pre_num == 1 or next_num == 1:
                self.result = pre_num + next_num
            else:
                self.result = pre_num * next_num
            pre_num = self.result
        print(self.result)

if __name__ == '__main__':
    content = input()
    str_list = list(map(int, list(content)))
    number = Cal(str_list)
    number.main()
