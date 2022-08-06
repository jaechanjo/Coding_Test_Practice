# 1번 풀이
# class Reverse:
#     def __init__(self, num):
#         self.num = num
#         self.result = 0
#
#     def main(self):
#         binary = self.num[0]
#         if self.num[-1] != binary:
#             self.result += 1
#         for i in range(1, len(self.num)):
#             if binary != self.num[i]:
#                 for j in range(i, len(self.num)):
#                     if binary != self.num[j]:
#                         self.num[j] = binary
#                     else:
#                         self.result += 1
#                         break
#         print(self.result)

# 2번 풀이
class Reverse:
    def __init__(self, num):
        self.num = num
        self.result = 0

    def main(self):
        binary = self.num[0]                    # 모든 원소를 첫번째로 변환
        for i in range(len(self.num)-1):
            if self.num[i] != self.num[i + 1]:
                if binary != self.num[i+1]:
                    self.result += 1
        print(self.result)

if __name__ == '__main__':
    binary = input()
    bi_list = list(map(int, list(binary)))
    number = Reverse(bi_list)
    number.main()