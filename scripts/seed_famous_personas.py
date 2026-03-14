#!/usr/bin/env python3
"""
Seed script: 7 famous historical personas + 70 questions authored by @vece + answers.

Personas: Einstein, Kahlo, da Vinci, Socrates, Curie, Jobs, Hepburn.
Each persona answers their own 10 questions (persona_choice = option index 0/1/2).

Run from the backend project root:
    python scripts/seed_famous_personas.py

Prerequisites: @vece user must exist. Run seed_vece_user.py first if needed.
Idempotent: safe to run multiple times (ON CONFLICT DO NOTHING everywhere).
"""

import os
import sys
from pathlib import Path

# ── Load .env (same as seed_vece_user.py) ─────────────────────────────────────
project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ[k.strip()] = v.strip().strip('"').strip("'")

import psycopg2  # noqa: E402

# Same bcrypt hash as seed_vece_user.py → password = "testpass123"
PASSWORD_HASH = "$2b$12$pAzELgYyuJfxGI1KeU038uQzBk5KyNFeX08eBabOPL0aUkRyWIPjS"
ACTIVE_TILL = "2035-12-31 00:00:00"

# ── Persona definitions ───────────────────────────────────────────────────────
PERSONAS = [
    dict(
        name="Albert", surname="Einstein", username="einstein",
        email="einstein@vece.ai", birthday="1879-03-14", gender="Male",
        country_kw="Germany",
        description="Theoretical physicist who developed the theory of relativity.",
    ),
    dict(
        name="Frida", surname="Kahlo", username="kahlo",
        email="kahlo@vece.ai", birthday="1907-07-06", gender="Female",
        country_kw="Mexico",
        description="Mexican painter known for her deeply symbolic self-portraits.",
    ),
    dict(
        name="Leonardo", surname="da Vinci", username="davinci",
        email="davinci@vece.ai", birthday="1452-04-15", gender="Male",
        country_kw="Italy",
        description="Renaissance polymath — painter, scientist, engineer, and visionary.",
    ),
    dict(
        name="Socrates", surname="of Athens", username="socrates",
        email="socrates@vece.ai", birthday="0001-01-01", gender="Male",
        country_kw="Greece",
        description="Ancient Greek philosopher and the founder of Western philosophy.",
    ),
    dict(
        name="Marie", surname="Curie", username="curie",
        email="curie@vece.ai", birthday="1867-11-07", gender="Female",
        country_kw="Poland",
        description="Pioneering scientist and the first woman to win two Nobel Prizes.",
    ),
    dict(
        name="Steve", surname="Jobs", username="jobs",
        email="jobs@vece.ai", birthday="1955-02-24", gender="Male",
        country_kw="United States",
        description="Co-founder of Apple and pioneer of the personal computer revolution.",
    ),
    dict(
        name="Audrey", surname="Hepburn", username="hepburn",
        email="hepburn@vece.ai", birthday="1929-05-04", gender="Female",
        country_kw="Belgium",
        description="Iconic actress and humanitarian ambassador for UNICEF.",
    ),
]

# ── Questions (10 per persona) ────────────────────────────────────────────────
QUESTIONS = {
    "einstein": [
        dict(
            text="Is imagination more important than knowledge?",
            hashtags=["Creativity", "Knowledge"], persona_choice=0,
            options=[
                "Yes, knowledge is limited; imagination circles the world",
                "No, without hard facts, imagination is just a dream",
                "They are equally balanced in a genius",
            ],
        ),
        dict(
            text="Do you believe the universe is inherently logical or chaotic?",
            hashtags=["Physics", "Logic"], persona_choice=0,
            options=[
                "Logical: God does not play dice with the universe",
                "Chaotic: It's all a beautiful, random mess",
                "We can never know the true nature of the universe",
            ],
        ),
        dict(
            text="Is a scientist responsible for how their discoveries are used?",
            hashtags=["Ethics", "Science"], persona_choice=0,
            options=[
                "Yes, moral responsibility cannot be delegated",
                "No, science is neutral; the use is political",
                "Only if the danger was obvious from the start",
            ],
        ),
        dict(
            text="In a world of nations, do you consider yourself a Citizen of the World?",
            hashtags=["Globalization", "Identity"], persona_choice=0,
            options=[
                "Yes, nationalism is an infantile disease",
                "No, my roots and country define me",
                "I feel loyal only to those I love",
            ],
        ),
        dict(
            text="Should our homes be built as machines for living or works of art?",
            hashtags=["Architecture", "Logic"], persona_choice=2,
            options=[
                "Purely functional machines",
                "Purely aesthetic art",
                "A perfect geometric harmony of both",
            ],
        ),
        dict(
            text="Is religion without science blind, or is science without religion lame?",
            hashtags=["Religion", "Science"], persona_choice=2,
            options=[
                "Religion is enough",
                "Science is enough",
                "They must coexist to understand reality",
            ],
        ),
        dict(
            text="Can war ever truly be justified in the name of peace?",
            hashtags=["War", "Peace"], persona_choice=1,
            options=[
                "Yes, as a last resort against evil",
                "No, war is a failure of human intelligence",
                "Only in self-defense",
            ],
        ),
        dict(
            text="The most beautiful thing we can experience is the mysterious. Agree?",
            hashtags=["Existentialism", "Science"], persona_choice=0,
            options=[
                "Yes, mystery is the source of all true art and science",
                "No, I prefer clarity and total understanding",
                "Mystery is just something we haven't explained yet",
            ],
        ),
        dict(
            text="A person who never made a mistake never tried anything new. How do you feel about failure?",
            hashtags=["Ambition", "Psychology"], persona_choice=0,
            options=[
                "Failure is the best proof of progress",
                "Failure should be avoided at all costs",
                "Failure is okay, but only once",
            ],
        ),
        dict(
            text="Should education focus on memorizing facts or training the mind to think?",
            hashtags=["Education", "CriticalThinking"], persona_choice=1,
            options=[
                "Memorizing facts builds the foundation",
                "Training the mind is the only goal",
                "A balance of both is needed",
            ],
        ),
    ],
    "kahlo": [
        dict(
            text="I paint self-portraits because I am so often alone. Is art a form of therapy?",
            hashtags=["Art", "MentalHealth"], persona_choice=0,
            options=[
                "Yes, it's the only way to process deep pain",
                "No, art should be about the outside world",
                "Art is a business first",
            ],
        ),
        dict(
            text="My emotions are my fuel. Should you let your feelings lead your life?",
            hashtags=["Emotions", "Psychology"], persona_choice=0,
            options=[
                "Yes, follow your heart regardless of the cost",
                "No, logic must always be in control",
                "Emotions are dangerous; they need to be suppressed",
            ],
        ),
        dict(
            text="Is identity something we are born with or something we paint ourselves?",
            hashtags=["Identity", "Culture"], persona_choice=2,
            options=[
                "We are born with it",
                "We create it entirely",
                "It is a mix of heritage and personal choice",
            ],
        ),
        dict(
            text="I drank to drown my sorrows, but the damn things learned to swim. How do you handle grief?",
            hashtags=["Grief", "Psychology"], persona_choice=2,
            options=[
                "I try to ignore it",
                "I seek professional help",
                "I live through it and express it through work",
            ],
        ),
        dict(
            text="Is passion more important in a relationship than stability?",
            hashtags=["Romance", "Relationships"], persona_choice=0,
            options=[
                "Yes, without fire, a relationship is dead",
                "No, stability is the only thing that lasts",
                "Both are equally important",
            ],
        ),
        dict(
            text="Feet, what do I need them for if I have wings to fly? How important is physical health to your spirit?",
            hashtags=["BodyPositivity", "Resilience"], persona_choice=0,
            options=[
                "The spirit is independent of the body",
                "Body and soul are one; health is everything",
                "Physical limits are just another challenge",
            ],
        ),
        dict(
            text="Should your art reflect your political struggle?",
            hashtags=["Politics", "Art"], persona_choice=0,
            options=[
                "Yes, art is a weapon for change",
                "No, art should be purely aesthetic",
                "Only if the artist feels like it",
            ],
        ),
        dict(
            text="I used to think I was the strangest person in the world. Do you embrace your weirdness?",
            hashtags=["Identity", "Introversion"], persona_choice=0,
            options=[
                "Yes, my uniqueness is my greatest strength",
                "No, I try to fit in to be successful",
                "I am not weird; I am just myself",
            ],
        ),
        dict(
            text="Would you want to live forever if your pain lived too?",
            hashtags=["Longevity", "Ethics"], persona_choice=1,
            options=[
                "Yes, life is always better than death",
                "No, a natural end is necessary",
                "Only if I could be physically perfect",
            ],
        ),
        dict(
            text="Is what you wear a costume or a confession?",
            hashtags=["Fashion", "Identity"], persona_choice=1,
            options=[
                "A costume to hide behind",
                "A confession of who I am inside",
                "Just something to cover my body",
            ],
        ),
    ],
    "davinci": [
        dict(
            text="Is technology just another way to imitate nature?",
            hashtags=["Technology", "Nature"], persona_choice=0,
            options=[
                "Yes, nature is the ultimate engineer",
                "No, technology should surpass nature",
                "Technology and nature are enemies",
            ],
        ),
        dict(
            text="Should a person be a specialist or a polymath, master of many things?",
            hashtags=["Knowledge", "Career"], persona_choice=1,
            options=[
                "Specialization is for efficiency",
                "Being a polymath is the only way to see the truth",
                "Focus on one thing, but dabble in others",
            ],
        ),
        dict(
            text="Is Logic the only way to prove beauty?",
            hashtags=["Logic", "Art"], persona_choice=2,
            options=[
                "Yes, geometry is the soul of beauty",
                "No, beauty is purely emotional",
                "Beauty is a mathematical harmony we feel",
            ],
        ),
        dict(
            text="Would you trust a robot to perform surgery on you?",
            hashtags=["Robotics", "Health"], persona_choice=0,
            options=[
                "Yes, mechanical precision is better than human hand",
                "No, machines lack human intuition",
                "Only if a human is watching",
            ],
        ),
        dict(
            text="Is it better to observe the world in silence or to participate in the noise?",
            hashtags=["Introversion", "CriticalThinking"], persona_choice=0,
            options=[
                "Observe: the eye sees more when the mouth is shut",
                "Participate: you only learn through action",
                "A mix of both",
            ],
        ),
        dict(
            text="Should the ideal city prioritize air, light, and cleanliness over density?",
            hashtags=["Urbanism", "Architecture"], persona_choice=0,
            options=[
                "Yes, the health of the people is the design's goal",
                "No, density and commerce are more important",
                "It depends on the location",
            ],
        ),
        dict(
            text="Is the future something we discover or something we invent?",
            hashtags=["Future", "Innovation"], persona_choice=1,
            options=[
                "We discover what is already possible",
                "We invent it through our imagination",
                "It is written by fate",
            ],
        ),
        dict(
            text="What is the ultimate tool for understanding the world?",
            hashtags=["Science", "Research"], persona_choice=1,
            options=[
                "Books and theories",
                "Direct observation and drawing",
                "Spiritual revelation",
            ],
        ),
        dict(
            text="Is Ethics about the rules we follow or the results we produce?",
            hashtags=["Ethics", "Logic"], persona_choice=2,
            options=[
                "The rules",
                "The results",
                "The wisdom of the action",
            ],
        ),
        dict(
            text="Should design follow function, or should they be one and the same?",
            hashtags=["Design", "IndustrialDesign"], persona_choice=1,
            options=[
                "Function first",
                "They are a single, inseparable unity",
                "Beauty first",
            ],
        ),
    ],
    "socrates": [
        dict(
            text="I know that I know nothing. Is doubt the beginning of wisdom?",
            hashtags=["CriticalThinking", "Philosophy"], persona_choice=0,
            options=[
                "Yes, only by admitting ignorance can we learn",
                "No, confidence in our knowledge is necessary for action",
                "Doubt is a waste of time",
            ],
        ),
        dict(
            text="Is the unexamined life not worth living?",
            hashtags=["Education", "SelfImprovement"], persona_choice=0,
            options=[
                "Yes, self-reflection is the highest human duty",
                "No, sometimes it's better to just live and enjoy",
                "Over-analysis leads to unhappiness",
            ],
        ),
        dict(
            text="Should you follow the laws of your city even if they are unjust?",
            hashtags=["Ethics", "Law"], persona_choice=0,
            options=[
                "Yes, the social contract is sacred",
                "No, justice is higher than the law",
                "I would try to escape",
            ],
        ),
        dict(
            text="Is it better to suffer an injustice than to commit one?",
            hashtags=["Justice", "Ethics"], persona_choice=0,
            options=[
                "Yes, doing wrong hurts the soul of the doer",
                "No, survival and winning come first",
                "An eye for an eye is more fair",
            ],
        ),
        dict(
            text="Should a true friend tell you the harsh truth or protect your feelings?",
            hashtags=["Friendship", "Honesty"], persona_choice=0,
            options=[
                "The truth, no matter how much it hurts",
                "Protect feelings; kindness is more important",
                "It depends on the situation",
            ],
        ),
        dict(
            text="Is Democracy the best system, or should only the wise lead?",
            hashtags=["Politics", "Democracy"], persona_choice=1,
            options=[
                "Power to the people, always",
                "Power to the experts and the wise",
                "A mix of both",
            ],
        ),
        dict(
            text="Is physical beauty a sign of inner goodness?",
            hashtags=["Identity", "Ethics"], persona_choice=1,
            options=[
                "Yes, beauty reflects the soul",
                "No, they are completely unrelated",
                "Often, beauty is a trap",
            ],
        ),
        dict(
            text="Does Virtue lead to Happiness, or is Happiness the goal itself?",
            hashtags=["Religion", "Happiness"], persona_choice=0,
            options=[
                "Virtue is the only path to real happiness",
                "Happiness is the goal, virtue is just a tool",
                "Neither exists in a perfect form",
            ],
        ),
        dict(
            text="Should every belief be open to public questioning?",
            hashtags=["FreeSpeech", "Censorship"], persona_choice=0,
            options=[
                "Yes, nothing is too sacred to be questioned",
                "No, some things must remain beyond doubt for stability",
                "Only if the questioning is respectful",
            ],
        ),
        dict(
            text="Can virtue be taught in a school?",
            hashtags=["Dreams", "Education"], persona_choice=2,
            options=[
                "Yes, through books and lectures",
                "No, it is an innate gift",
                "It can only be learned through dialogue and experience",
            ],
        ),
    ],
    "curie": [
        dict(
            text="Is pure scientific research more important than its practical application?",
            hashtags=["Science", "Research"], persona_choice=0,
            options=[
                "Yes, knowledge for its own sake is the goal",
                "No, science must solve human problems first",
                "Both are inseparable",
            ],
        ),
        dict(
            text="Would you risk your life for a discovery that helps millions?",
            hashtags=["Discipline", "Altruism"], persona_choice=0,
            options=[
                "Yes, the goal is larger than the individual",
                "No, no discovery is worth a human life",
                "Only if I had no family to care for",
            ],
        ),
        dict(
            text="Should women still fight for gender equality in science today?",
            hashtags=["GenderEquality", "Education"], persona_choice=0,
            options=[
                "Yes, we are still far from true meritocracy",
                "No, the battle is already won",
                "Science should be gender-blind",
            ],
        ),
        dict(
            text="In a lab, is persistence more valuable than genius?",
            hashtags=["Discipline", "Psychology"], persona_choice=0,
            options=[
                "Yes, 99% of science is hard work",
                "No, without a spark of genius, work is wasted",
                "Teamwork is more important than either",
            ],
        ),
        dict(
            text="Should a scientist be a public influencer or stay in the shadows?",
            hashtags=["Introversion", "Science"], persona_choice=1,
            options=[
                "Public: to inspire and educate",
                "Shadows: to focus on the work without distraction",
                "Only if they need funding",
            ],
        ),
        dict(
            text="Is money the biggest distraction for a researcher?",
            hashtags=["Finance", "Career"], persona_choice=0,
            options=[
                "Yes, pursuing profit kills pure science",
                "No, money is the tool that makes science possible",
                "It's a necessary evil",
            ],
        ),
        dict(
            text="Is it possible to have a perfect work-life balance while changing the world?",
            hashtags=["WorkLifeBalance", "FamilyDynamics"], persona_choice=1,
            options=[
                "Yes, if you are organized",
                "No, greatness requires sacrifice of personal life",
                "It's a myth we should stop chasing",
            ],
        ),
        dict(
            text="Should we fear the unknown, or just try to understand it?",
            hashtags=["Weather", "CriticalThinking"], persona_choice=1,
            options=[
                "We should fear and respect its power",
                "We should only seek to understand and control it",
                "We should live in harmony with it",
            ],
        ),
        dict(
            text="Are ethics in science slowing down scientific progress too much?",
            hashtags=["DigitalEthics", "Biohacking"], persona_choice=1,
            options=[
                "Yes, we need more freedom to experiment",
                "No, ethics are more important than speed",
                "We need faster ethical reviews",
            ],
        ),
        dict(
            text="Does a simple life make for a better thinker?",
            hashtags=["Minimalism", "PersonalityTypes"], persona_choice=0,
            options=[
                "Yes, mental clutter follows physical clutter",
                "No, abundance stimulates the mind",
                "It doesn't make a difference",
            ],
        ),
    ],
    "jobs": [
        dict(
            text="Should we give customers what they want, or tell them what they need?",
            hashtags=["Marketing", "Design"], persona_choice=1,
            options=[
                "Give them what they want; the customer is king",
                "Show them the future they haven't imagined yet",
                "A mix of both",
            ],
        ),
        dict(
            text="Is Simplicity the ultimate sophistication?",
            hashtags=["InteriorDesign", "Minimalism"], persona_choice=0,
            options=[
                "Yes, removing the unnecessary is the goal",
                "No, more features mean more value",
                "Simple is good, but complex is more powerful",
            ],
        ),
        dict(
            text="Is startup culture better than big corporate structure?",
            hashtags=["Startups", "CorporateCulture"], persona_choice=0,
            options=[
                "Yes, small teams of A-players change the world",
                "No, big companies have the resources to scale",
                "Big companies should act like startups",
            ],
        ),
        dict(
            text="Is a smartphone a tool or an extension of the person?",
            hashtags=["Smartphones", "Identity"], persona_choice=1,
            options=[
                "Just a tool we can put down",
                "An extension of our mind and soul",
                "A dangerous addiction",
            ],
        ),
        dict(
            text="Is Intuition more powerful than intellect?",
            hashtags=["Intuition", "Logic"], persona_choice=0,
            options=[
                "Yes, follow your gut above all else",
                "No, logic and data are more reliable",
                "Use data to verify your intuition",
            ],
        ),
        dict(
            text="Is being unreasonable a requirement for greatness?",
            hashtags=["Ambition", "PersonalityTypes"], persona_choice=0,
            options=[
                "Yes, reasonable people adapt to the world",
                "No, collaboration requires compromise",
                "It's a flaw, not a virtue",
            ],
        ),
        dict(
            text="Is technology the new Art of the 21st century?",
            hashtags=["Art", "Technology"], persona_choice=0,
            options=[
                "Yes, code and design are the new canvas",
                "No, art is human; tech is just cold metal",
                "They are merging into one thing",
            ],
        ),
        dict(
            text="Remembering you are going to die is the best way to stop thinking you have something to lose. Agree?",
            hashtags=["Death", "Existentialism"], persona_choice=0,
            options=[
                "Yes, it's the ultimate motivator",
                "No, it's a depressing thought that slows me down",
                "I prefer to focus only on living",
            ],
        ),
        dict(
            text="Should a CEO be a recognizable personal brand?",
            hashtags=["PersonalBranding", "Leadership"], persona_choice=0,
            options=[
                "Yes, the face of the company is its soul",
                "No, they should stay quiet and focus on operations",
                "Only if it helps the business",
            ],
        ),
        dict(
            text="Is AI the ultimate Bicycle for the Mind?",
            hashtags=["ArtificialIntelligence", "Future"], persona_choice=0,
            options=[
                "Yes, it will augment human creativity forever",
                "No, it will replace human thought",
                "It's just another tool like the calculator",
            ],
        ),
    ],
    "hepburn": [
        dict(
            text="Is kindness the most important human quality?",
            hashtags=["Empathy", "Ethics"], persona_choice=0,
            options=[
                "Yes, it costs nothing but changes everything",
                "No, intelligence and strength are more vital",
                "Kindness is good, but can be a weakness",
            ],
        ),
        dict(
            text="Is true happiness found in helping others?",
            hashtags=["Happiness", "Philanthropy"], persona_choice=0,
            options=[
                "Yes, giving is the highest form of living",
                "No, happiness is found in personal achievement",
                "Happiness is found in love and romance",
            ],
        ),
        dict(
            text="Should fashion be about elegance or about shocking people?",
            hashtags=["Fashion", "Style"], persona_choice=0,
            options=[
                "Elegance and timelessness",
                "Expression and shock value",
                "Comfort and utility",
            ],
        ),
        dict(
            text="Is Minimalism in possessions a key to a peaceful mind?",
            hashtags=["Minimalism", "Home"], persona_choice=0,
            options=[
                "Yes, you only need a few beautiful things",
                "No, I like a home full of memories",
                "I am a maximalist",
            ],
        ),
        dict(
            text="Should you trust people until they give you a reason not to?",
            hashtags=["Friendship", "Trust"], persona_choice=0,
            options=[
                "Yes, start with an open heart",
                "No, people must earn your trust slowly",
                "Trust no one but your family",
            ],
        ),
        dict(
            text="Is travel about the luxury or about the people you meet?",
            hashtags=["Travel", "HumanRights"], persona_choice=1,
            options=[
                "The luxury and relaxation",
                "The connection with different cultures",
                "The adventure and risk",
            ],
        ),
        dict(
            text="Should movies always have a happy ending?",
            hashtags=["Movies", "Emotions"], persona_choice=2,
            options=[
                "Yes, life is hard enough",
                "No, they should reflect real tragedy",
                "They should leave you with hope, regardless",
            ],
        ),
        dict(
            text="Is it possible to forgive an absolute betrayal?",
            hashtags=["Grief", "Forgiveness"], persona_choice=0,
            options=[
                "Yes, holding a grudge is like drinking poison",
                "No, some things can never be undone",
                "Only if the person changes completely",
            ],
        ),
        dict(
            text="Should celebrities use their fame for activism?",
            hashtags=["Activism", "Philanthropy"], persona_choice=0,
            options=[
                "Yes, fame is a responsibility",
                "No, they should just entertain us",
                "Only for causes they truly understand",
            ],
        ),
        dict(
            text="Does true Ambition mean being the best at your job or being the best person?",
            hashtags=["Ambition", "SelfImprovement"], persona_choice=1,
            options=[
                "Being the top in my field",
                "Being a kind and helpful human being",
                "Finding a balance",
            ],
        ),
    ],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_or_create_hashtag(cur, name: str) -> int:
    cur.execute("SELECT id FROM hashtags WHERE name = %s", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO hashtags (name) VALUES (%s) RETURNING id", (name,))
    return cur.fetchone()[0]


def get_country_id(cur, keyword: str) -> int:
    cur.execute(
        "SELECT id FROM countries WHERE name ILIKE %s OR full_name ILIKE %s LIMIT 1",
        (f"%{keyword}%", f"%{keyword}%"),
    )
    row = cur.fetchone()
    if row:
        return row[0]
    # Fallback: first country in DB
    cur.execute("SELECT id FROM countries LIMIT 1")
    return cur.fetchone()[0]


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    host = os.getenv("POSTGRES_HOST")
    port = 5432 if host and "pooler" in host else int(os.getenv("POSTGRES_PORT", "5432"))
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )
    conn.autocommit = False
    cur = conn.cursor()

    # ── 1. Find @vece (question author) ───────────────────────────────────────
    cur.execute("SELECT id FROM users WHERE username = 'vece'")
    row = cur.fetchone()
    if not row:
        print("ERROR: @vece user not found. Run seed_vece_user.py first.")
        conn.close()
        return 1
    author_id = row[0]
    print(f"Using @vece (id={author_id}) as question author")

    # ── 2. Create personas ────────────────────────────────────────────────────
    persona_ids: dict[str, int] = {}
    for p in PERSONAS:
        country_id = get_country_id(cur, p["country_kw"])
        cur.execute(
            """
            INSERT INTO users (
                name, surname, username, email, password_hash, birthday,
                country_id, gender, is_verified, is_active, description, role
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, TRUE, TRUE, %s, 'user')
            ON CONFLICT (username) DO NOTHING
            """,
            (
                p["name"], p["surname"], p["username"], p["email"],
                PASSWORD_HASH, p["birthday"], country_id,
                p["gender"], p["description"],
            ),
        )
        cur.execute("SELECT id FROM users WHERE username = %s", (p["username"],))
        uid = cur.fetchone()[0]
        persona_ids[p["username"]] = uid

        # user_settings
        cur.execute(
            """
            INSERT INTO user_settings (user_id, show_name_option, show_question_results)
            VALUES (%s, 'Name', 'All')
            ON CONFLICT (user_id) DO NOTHING
            """,
            (uid,),
        )
        print(f"  persona @{p['username']} → user_id={uid}")

    conn.commit()
    print(f"\nPersonas ready: {list(persona_ids.keys())}\n")

    # ── 3. Create questions, options, hashtag links, answers ──────────────────
    total_q_created = 0
    total_a_created = 0

    for username, questions in QUESTIONS.items():
        persona_uid = persona_ids[username]
        print(f"Processing @{username} (user_id={persona_uid})…")

        for q in questions:
            # Check if question already exists (idempotency)
            cur.execute(
                "SELECT id FROM questions WHERE text = %s AND author_id = %s",
                (q["text"], author_id),
            )
            existing = cur.fetchone()

            if existing:
                qid = existing[0]
            else:
                # Insert question
                cur.execute(
                    """
                    INSERT INTO questions (
                        author_id, text, max_options, active_till,
                        allow_user_options, created_at, total_answers
                    )
                    VALUES (%s, %s, 1, %s, FALSE, NOW(), 0)
                    RETURNING id
                    """,
                    (author_id, q["text"], ACTIVE_TILL),
                )
                qid = cur.fetchone()[0]
                total_q_created += 1

                # Insert options
                for pos, opt_text in enumerate(q["options"]):
                    cur.execute(
                        """
                        INSERT INTO question_options (
                            question_id, text, position, by_question_author,
                            created_at, count, percentage
                        )
                        VALUES (%s, %s, %s, TRUE, NOW(), 0, 0.0)
                        """,
                        (qid, opt_text, pos),
                    )

                # Link hashtags
                for tag_name in q["hashtags"]:
                    htag_id = get_or_create_hashtag(cur, tag_name)
                    cur.execute(
                        """
                        INSERT INTO question_hashtag_links (question_id, hashtag_id)
                        VALUES (%s, %s)
                        ON CONFLICT (question_id, hashtag_id) DO NOTHING
                        """,
                        (qid, htag_id),
                    )

            # Fetch option_ids for this question (works for new and existing)
            cur.execute(
                "SELECT position, id FROM question_options WHERE question_id = %s ORDER BY position",
                (qid,),
            )
            option_ids: dict[int, int] = {row[0]: row[1] for row in cur.fetchall()}

            # Insert answer (skip if already answered by this persona)
            cur.execute(
                "SELECT id FROM answers WHERE question_id = %s AND user_id = %s",
                (qid, persona_uid),
            )
            if cur.fetchone():
                continue  # already answered

            cur.execute(
                """
                INSERT INTO answers (question_id, user_id, created_at)
                VALUES (%s, %s, NOW())
                RETURNING id
                """,
                (qid, persona_uid),
            )
            answer_id = cur.fetchone()[0]
            total_a_created += 1

            # Link answer → chosen option
            chosen_opt_id = option_ids[q["persona_choice"]]
            cur.execute(
                "INSERT INTO answer_options (answer_id, option_id) VALUES (%s, %s)",
                (answer_id, chosen_opt_id),
            )

        conn.commit()
        print(f"  done @{username}")

    print(f"\nCreated {total_q_created} questions, {total_a_created} answers.\n")

    # ── 4. Recalculate total_answers and option counts/percentages ─────────────
    print("Recalculating totals…")
    cur.execute(
        """
        UPDATE questions q
        SET total_answers = (
            SELECT COUNT(*) FROM answers a WHERE a.question_id = q.id
        )
        WHERE q.author_id = %s
        """,
        (author_id,),
    )
    cur.execute(
        """
        UPDATE question_options qo
        SET
            count = (
                SELECT COUNT(*) FROM answer_options ao WHERE ao.option_id = qo.id
            ),
            percentage = CASE
                WHEN q.total_answers > 0
                THEN (
                    SELECT COUNT(*) FROM answer_options ao WHERE ao.option_id = qo.id
                )::float * 100.0 / q.total_answers
                ELSE 0.0
            END
        FROM questions q
        WHERE qo.question_id = q.id AND q.author_id = %s
        """,
        (author_id,),
    )
    conn.commit()
    print("Done. All totals updated.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
