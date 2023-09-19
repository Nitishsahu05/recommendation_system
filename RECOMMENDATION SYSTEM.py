# Define a dictionary of movie ratings by users
# Replace this with your dataset, where keys are user IDs and values are dictionaries of movie ratings.
# Each inner dictionary should have movie IDs as keys and ratings as values.
user_ratings = {
    'User1': {'Movie1': 4, 'Movie2': 5, 'Movie3': 3},
    'User2': {'Movie1': 5, 'Movie4': 4, 'Movie5': 2},
    'User3': {'Movie2': 3, 'Movie4': 5, 'Movie6': 4},
    # Add more users and their ratings as needed
}

# Define a function to calculate similarity between two users using the Jaccard similarity coefficient
def calculate_similarity(user1, user2):
    common_movies = set(user1.keys()) & set(user2.keys())
    if not common_movies:
        return 0  # No common movies, similarity is 0
    union_movies = set(user1.keys()) | set(user2.keys())
    similarity = len(common_movies) / len(union_movies)
    return similarity

# Define a function to get movie recommendations for a target user
def get_recommendations(target_user):
    recommendations = {}
    for user, ratings in user_ratings.items():
        if user == target_user:
            continue  # Skip the target user
        similarity = calculate_similarity(user_ratings[target_user], ratings)
        for movie, rating in ratings.items():
            if movie not in user_ratings[target_user]:
                if movie not in recommendations:
                    recommendations[movie] = 0
                recommendations[movie] += similarity * rating
    
    # Sort recommendations by score (higher scores first)
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

# Example: Get recommendations for 'User1'
target_user = 'User1'
recommended_movies = get_recommendations(target_user)

# Display the top N recommended movies
top_n = 5
print(f"Top {top_n} movie recommendations for {target_user}:")
for movie, score in recommended_movies[:top_n]:
    print(f"Movie: {movie}, Score: {score}")
