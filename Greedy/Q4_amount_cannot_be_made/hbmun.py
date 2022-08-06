class Money:
    def __init__(self, count, num):
        self.count = int(count)
        self.num = list(num)
        self.num.sort()
        self.result = 1

    def main(self):
        money = self.num[0]
        if self.num[-1] == 1:
            self.result = len(self.num) + 1
        else:
            for el in self.num[1:]:
                if self.result < money:
                    break
                self.result += 1
                money += el

        print(self.result)

if __name__ == '__main__':
    count = input()
    money = map(int, input().split())
    number = Money(count, money)
    number.main()