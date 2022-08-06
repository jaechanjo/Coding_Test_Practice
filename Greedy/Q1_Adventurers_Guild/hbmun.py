
class Guild:
    def __init__(self, person, fear):
        self.person = person
        self.fear = list(fear)
        self.fear.sort(reverse=True)
        self.result = 0

    def main(self):
        team = self.fear[0]
        for i in range(self.person):
            team -= 1
            if team == 0:
                self.result += 1
                if i+1 < self.person:
                    team = self.fear[i+1]
        print(self.result)

if __name__ == '__main__':
    person_num = int(input())
    fear_list = map(int, input().split())
    adventure = Guild(person_num, fear_list)
    adventure.main()