import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a structured song and its core numerical and categorical attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Represents a user's target taste attributes for engine evaluation."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """Object-oriented wrapper implementation of the recommendation pipeline logic."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Generates sorted recommendations for a specific UserProfile instance."""
        prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_acousticness": 0.80 if user.likes_acoustic else 0.20
        }
        song_dicts = [song.__dict__ for song in self.songs]
        results = recommend_songs(prefs, song_dicts, k=k)
        return [Song(**r[0]) for r in results]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a string description detailing why a specific song was suggested."""
        prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_acousticness": 0.80 if user.likes_acoustic else 0.20
        }
        _, reasons = score_song(prefs, song.__dict__)
        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV playlist asset catalog from disk and casts strings into math-ready datatypes."""
    songs = []
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"].strip().lower(),
                "mood": row["mood"].strip().lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            })
    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Evaluates a single catalog song profile against active user preference targets."""
    score = 0.0
    reasons = []

    # 1. Categorical Matching - Updated keys to match main.py exactly
    if song.get("genre") == user_prefs.get("favorite_genre", "").lower():
        score += 1.0
        reasons.append("genre match (+1.0)")
        
    if song.get("mood") == user_prefs.get("favorite_mood", "").lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # 2. Vector Error Distance Checking
    if "target_energy" in user_prefs and "energy" in song:
        energy_dist = abs(user_prefs["target_energy"] - song["energy"])
        energy_score = (1.0 - energy_dist) * 1.5
        score += energy_score
        reasons.append(f"energy proximity (+{energy_score:.2f})")

    if "target_acousticness" in user_prefs and "acousticness" in song:
        acoustic_dist = abs(user_prefs["target_acousticness"] - song["acousticness"])
        acoustic_score = (1.0 - acoustic_dist) * 2.0
        score += acoustic_score
        reasons.append(f"acoustic proximity (+{acoustic_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Evaluates, scores, ranks, and cuts off the catalog payload down to top-k choices."""
    scored_list = []
    
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_list.append((song, score, explanation))
    
    ranked_list = sorted(scored_list, key=lambda item: item[1], reverse=True)
    
    return ranked_list[:k]