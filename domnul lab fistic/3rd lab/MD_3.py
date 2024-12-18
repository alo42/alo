import heapq


def read_friendship_matrix(file_path):
    matrix = []
    names = []
    with open(file_path, 'r',encoding="utf-8") as file:
        lines = file.readlines()

        if len(lines) > 1:
            names = [name.strip() for name in lines[0].strip().split('|')]

            for line in lines[1:]:
                values = line.split('|')[1]
                number_strings = values.split()
                numbers = [int(num) for num in number_strings]

                try:
                    row = [int(value) for value in numbers]
                    matrix.append(row)
                except ValueError as e:
                    print(f"Error parsing line: {line}, Error: {e}")
        else:
            print("File is empty or does not contain a valid friendship matrix.")

    return matrix, names



def display_friendship_matrix(matrix, names):
    
    print("Friendship Matrix:")
    print('\t' + '\t'.join(names))
    for i, row in enumerate(matrix):
        print(i," : ",names[i] + '\t' + '\t'.join(map(str, row)))

def mostFriends(matrix,names):
    pos = []
    max = 0
    for i in range(len(matrix)):
        summ = sum(matrix[i])
        if summ > max:
            max = summ
            pos = [i]
        elif summ == max :
            pos.append(i)

    print("Most friends: ")
    for po in pos:
        print(" ",names[po])


def sortByFriends(matrix,names):
    result  = []
    for i in range(len(matrix)):
        summ = sum(matrix[i])
        result.append((names[i], summ))

    result.sort(key=lambda x: x[1], reverse=True)

    for item in result:
        print(item[0], item[1])


def dijkstra(matrix, start):
    num_nodes = len(matrix)
    distances = {node: float('inf') for node in range(num_nodes)}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in range(num_nodes):
            weight = matrix[current_node][neighbor]
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances


def compute_ratings(matrix):
    num_people = len(matrix)
    ratings = {}

    for person in range(num_people):
        distances = dijkstra(matrix, person)
        total_points = sum([ distance-1 for distance in distances.values()])
        ratings[person] = total_points

    return ratings


def influentialPeople(ratings,names):
    with open("C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\influence.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    ratings_2 = {}
    
    for i, line in enumerate(lines):
        name, rating_str = line.split(" : ")
        rating_value = float(rating_str.strip())
        ratings_2[name] = rating_value * 0.5 * ratings[i]

    sorted_ratings = dict(sorted(ratings_2.items(), key=lambda item: item[1]))

    for i, (name, rating) in enumerate(sorted_ratings.items()):
        print(f"rating[{name}] = {sorted_ratings[name]}")

    return ratings_2

def interests(names):
    with open("C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\interests.txt", "r",encoding="utf-8") as file:
        lines = file.readlines()

    interests = []
    for i, line in enumerate(lines):
        interests.append(line.strip())
    print("Target interests: ")
    acc_interests = []
    for i,interest in enumerate(interests):
        if interest.upper() in "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats.".upper():
            print(interest)
            acc_interests.append(interest)
            #print(names[i])
    return acc_interests


def promote(names,ratings,interestss):
    interests2 = []
    with open("C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\people_interests.txt", "r",encoding="utf-8") as file:
        for line in file:
            interest_data = line.split(':')[1].split()
            interests2.append(interest_data)

    last_rating = []

    for i,person_interests in enumerate(interests2):
        conn = 0
        for inter in person_interests:
            if inter in interestss:
                conn+=1
        if conn > 0 : last_rating.append((names[i],ratings[names[i]] * 0.2 * conn))
        else: last_rating.append((names[i],ratings[names[i]] * 0.2 * 1))


    print("We should contact:")
    last_rating.sort(key=lambda x: x[1], reverse=True)

    for i, rating in enumerate(last_rating[:5]):
        print(f" {i+1}. {rating}")


file_path = 'C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\matrix.txt'
friendship_matrix, names = read_friendship_matrix(file_path)


print("Problem 3.1\n")
mostFriends(friendship_matrix,names)
print("\n*********************\n")

print("Problem 3.2 \n")
sortByFriends(friendship_matrix,names)
print("\n*********************\n")


print("Problem 3.3 \n")
ratings = compute_ratings(friendship_matrix)

for person, rating in ratings.items():
    print(f"Person {names[person]}: Rating {rating}")
print("\n*********************\n")

print("Problem 3.4 \n")
ratings_2 = influentialPeople(ratings,names)
print("\n*********************\n")

print("Problem 3.5 \n")
interests = interests(names)
print("\n*********************\n")

print("Problem 3.6 \n")
promote(names,ratings_2,interests)
print("\n*********************\n")