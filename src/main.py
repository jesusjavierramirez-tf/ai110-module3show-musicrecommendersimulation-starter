"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    test_profiles = {
        "High-Energy Workout Fanatic": {
            "favorite_genre": "pop",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_valence": 0.80,
            "target_acousticness": 0.05
        },
        "Melancholic Acoustic Introspective": {
            "favorite_genre": "country",
            "favorite_mood": "melancholic",
            "target_energy": 0.30,
            "target_valence": 0.25,
            "target_acousticness": 0.90
        },
        "Adversarial Edge Case (The Conflicted Subwoofer)": {
            "favorite_genre": "techno",
            "favorite_mood": "serene",
            "target_energy": 0.90,
            "target_valence": 0.30,
            "target_acousticness": 0.95 
        }
    }

    for profile_name, user_prefs in test_profiles.items():
        print("-" * 50)
        print(f"RUNNING EVALUATION FOR: {profile_name}")
        print("-" * 50)

        recommendations = recommend_songs(user_prefs, songs, k=3)

        print("\nTop recommendations:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} (by {song['artist']}) - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()
        print("\n")


if __name__ == "__main__":
    main()
