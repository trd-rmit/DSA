total_test_cases = int(input())

for _ in range(total_test_cases):
    total_movies, chef_time = map(int, input().split())
    max_rating = 0
    for _ in range(total_movies):
        movie_duration, rating = map(int, input().split())
        if chef_time >= movie_duration and rating > max_rating:
            max_rating = rating
    print(max_rating)
