class House:
    def __init__(self, people, water):
        self.people = people
        self.water = water
        
    def __repr__(self) -> str:
        return f'{self.people}-{self.water}'

def main():
    count = 1
    while True:
        N = int(input())
        if N == 0: break
        city = []
        total_population = 0
        total_water = 0
        for _ in range(N):
            people, water = map(int, input().split())
            city.append(House(people, int(water/people)))
            total_population += people
            total_water += water
        city = sorted(city, key=lambda x: x.water)
        
        for x in range(len(city)-1):
            if (x+1) >= len(city): break
            if city[x].water == city[x+1].water:
                city[x+1].people += city[x].people
                city.remove(city[x])
        
        average = total_water / total_population
        print(f'Cidade# {count}:')
        print(' '.join(map(str, city)))
        print(f'Consumo medio: {average:.2f} m3.')
        print()
        count += 1
        
if __name__ == '__main__':
    main()