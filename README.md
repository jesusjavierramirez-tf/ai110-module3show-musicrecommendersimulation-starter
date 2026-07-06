# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Our recommendation system uses a content-based filtering approach that combines categorical matching weights with continuous feature vector distance calculations. The system evaluates every track in our catalog individually against a target User Profile to predict alignment.

### System Components & Data Structures
* **Song Features:** Extracted directly from our catalog attributes (`genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`).
* **UserProfile Data:** A dictionary tracking explicit user preferences along with mathematical targets for acoustic density and energy output.

### Our Recommendation Algorithm Recipe
Every single song is evaluated using the following point-accumulation rules:
1. **Genre Affinity (+2.0 pts):** Added if the track matches the user's explicit `favorite_genre`.
2. **Mood Affinity (+1.0 pts):** Added if the track matches the user's explicit `favorite_mood`.
3. **Energy Proximity (Up to 1.5 pts):** Calculated as `(1.0 - abs(target_energy - song_energy)) * 1.5`.
4. **Acoustic Proximity (Up to 1.0 pts):** Calculated as `(1.0 - abs(target_acousticness - song_acousticness)) * 1.0`.

### Ranking Rule
Once the iteration loop completes scoring every song, the system sorts the tracks in descending numerical order. The top $K$ items (e.g., Top 3) are sliced and displayed as the final recommendation list.

### Potential Bias Risks
* **Genre Dominance:** Because a genre match yields 2.0 fixed points, an energetic pop song might accidentally outrank a deeply relaxing jazz song even if the user profile explicitly requests low-energy, high-acoustic chill music. 
* **Cold Start & Cold Catalog:** The system assumes our features perfectly capture the mood. If a song is mislabeled in the CSV, or if a user has a fluid taste shift that doesn't map to these exact metrics, the recommendations will stagnate.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```text
Loaded songs: 17

Top recommendations:

Library Rain - Score: 5.44
Because: genre match (+2.0), mood match (+1.0), energy proximity (+1.50), acoustic proximity (+0.94)

Midnight Coding - Score: 5.30
Because: genre match (+2.0), mood match (+1.0), energy proximity (+1.40), acoustic proximity (+0.91)

Focus Flow - Score: 4.40
Because: genre match (+2.0), energy proximity (+1.42), acoustic proximity (+0.98)

Spacewalk Thoughts - Score: 3.27
Because: mood match (+1.0), energy proximity (+1.40), acoustic proximity (+0.88)

Coffee Shop Stories - Score: 2.38
Because: energy proximity (+1.47), acoustic proximity (+0.91)
```
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



