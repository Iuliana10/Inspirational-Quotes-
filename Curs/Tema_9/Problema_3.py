#Analiza Datelor de Rating ale Filmelor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)
num_users = 1000
num_movies = 100
num_ratings = 10000

user_ids = np.random.randint(1, num_users + 1, num_ratings)
movie_ids = np.random.randint(1, num_movies + 1, num_ratings)
ratings = np.random.randint(1, 6, num_ratings)  # Evaluări între 1 și 5


data = {
    "ID Utilizator": user_ids,
    "ID Film": movie_ids,
    "Rating": ratings
}
df = pd.DataFrame(data)


average_ratings = df.groupby("ID Film")["Rating"].mean()


top_5_movies = average_ratings.sort_values(ascending=False).head(5)


rating_counts = df.groupby("ID Film")["Rating"].count()
low_rated_movies = average_ratings[(average_ratings < 3.5) & (rating_counts > 50)]


plt.figure(figsize=(14, 7))


plt.subplot(1, 3, 1)
plt.hist(df["Rating"], bins=np.arange(1, 7) - 0.5, edgecolor="black", color="skyblue")
plt.title("Distribuția Ratingurilor")
plt.xlabel("Rating")
plt.ylabel("Frecvență")


plt.subplot(1, 3, 2)
top_5_movies.plot(kind="bar", color="orange")
plt.title("Top 5 Filme cu Cel Mai Mare Rating Mediu")
plt.xlabel("ID Film")
plt.ylabel("Rating Mediu")


plt.subplot(1, 3, 3)
plt.scatter(rating_counts, average_ratings, alpha=0.7, color="green")
plt.title("Număr Evaluări vs. Rating Mediu")
plt.xlabel("Număr Evaluări")
plt.ylabel("Rating Mediu")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
