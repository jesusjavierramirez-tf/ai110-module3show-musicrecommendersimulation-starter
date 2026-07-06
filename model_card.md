# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## Limitations and Bias Analysis

Our evaluation experiments exposed a clear "Filter Bubble" vulnerability rooted in categorical dominance. Because a hard string match on `favorite_genre` grants an immediate +2.0 point bonus, the system routinely creates recommendation dead-ends. 

### Core Architectural Limitations:
1. **Categorical Gatekeeping:** If a user expresses a preference for a specific genre, the engine will recommend mediocre tracks inside that genre while completely ignoring sonically perfect masterpieces from adjacent genres (e.g., passing over a serene classical ambient piece because it isn't explicitly tagged as 'lofi').
2. **Catalog Under-Representation:** Our current dataset contains heavy clusters around Lofi and Pop. Because the engine relies entirely on matching attributes, users searching for specialized structural categories (like World or IDM) will receive recommendations containing irrelevant fallback genres simply because those tracks happened to have matching energy values.
3. **The Conflicted Variable Flaw:** The scoring rule evaluates attributes independently. It lacks the safety guardrails to understand that a user demanding high-energy electronic music while requesting maximum acoustic values is a physical contradiction, resulting in compromised outputs.

---

## Evaluation and Sensitivity Analysis

### Tested Profiles & Terminal Outputs
We subjected the recommender to three high-contrast test profiles: a High-Energy Workout profile, a Melancholic Acoustic profile, and an Adversarial Edge Case ("The Conflicted Subwoofer") with conflicting target metrics (high energy but high acousticness). 

### Key Findings from the Sensitivity Experiment
We ran a data experiment where we halved the categorical Genre weight from 2.0 to 1.0 and doubled the continuous Acousticness weight from 1.0 to 2.0. 

This architectural change dramatically altered the system's output behaviors:
* **Before the change:** Categorical keywords acted as strict gatekeepers. The system suffered from a broad "filter bubble" flaw where a song matching a genre string automatically outranked sonically superior matches from other genres.
* **After the change:** The system successfully broke out of its keyword limitation. In the adversarial test, it successfully prioritized *Chamber Wind* over *Subterranean* because it weighed the underlying acoustic structure of the song heavier than a simple "Techno" or "Classical" label. This proves that continuous vector proximity provides a much tighter grip on a user's actual sonic "vibe" than broad industry categories

### Comparative Profile Matrix
* **Gym Profile vs. Acoustic Profile:** The algorithm responded accurately to explicit structural constraints. The Gym profile surfaced exclusively synthetic, high-tempo, non-acoustic tracks like *Gym Hero* and *Sunrise City*. Conversely, the Acoustic profile completely flipped the catalog orientation, favoring organic instrumentation like *Gravel Road* and tracking down ultra-low energy thresholds.
* **The Conflicted Subwoofer Test (Adversarial Baseline):** Testing a user demanding a high-energy `techno` track with maximum `acousticness` highlighted a major system blindspot. Under standard settings, the engine prioritized the text match (*Subterranean*) despite its acoustic level being a near-zero 0.03. 

### Insights from the Sensitivity Experiment
By executing a sensitivity adjustment (halving the importance of categorical genres to 1.0 point and doubling acoustic vectors to 2.0 points), we successfully decoupled the engine from rigid keyword constraints. This change proved that a balance of mathematical features provides a more accurate representation of a musical "vibe" than broad, text-based genre definitions alone.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
