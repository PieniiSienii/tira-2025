class TrainPrices:
    def __init__(self):
        self.routes = {}
        self.cities = []

    def add_city(self, name):
        self.cities.append(name)
        self.routes[name] = []

    def add_train(self, city1, city2, price):
        self.routes[city1].append((price, city2))
        self.routes[city2].append((price, city1))

    def find_prices(self):
        self.cities.sort()
        n = len(self.cities)
        city_index = {city: idx for idx, city in enumerate(self.cities)}

        INF = float('inf')
        matrix = [[INF]*n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0

        for city, trips in self.routes.items():
            i = city_index[city]
            for price, dest in trips:
                j = city_index[dest]
                matrix[i][j] = min(matrix[i][j], price)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

        result = [[None] + self.cities]
        for i, city in enumerate(self.cities):
            row = [city]
            for j in range(n):
                if matrix[i][j] == INF:
                    row.append(-1)
                else:
                    row.append(matrix[i][j])
            result.append(row)

        return result




if __name__ == "__main__":
    prices = TrainPrices()

    prices.add_city("Helsinki")
    prices.add_city("Turku")
    prices.add_city("Tampere")
    prices.add_city("Oulu")

    prices.add_train("Helsinki", "Tampere", 20)
    prices.add_train("Helsinki", "Turku", 10)
    prices.add_train("Tampere", "Turku", 50)

    for row in prices.find_prices():
        print(row)


    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]