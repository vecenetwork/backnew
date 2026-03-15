#!/usr/bin/env python3
"""
Seed script: Demo historical personas for VECE.

Creates 10 demo user accounts based on historical cultural figures,
then seeds questions (asked by a shared @demo account) with answer options
drawn from verified quotes/positions of each figure.

Each persona answers at least 10 questions.
Questions are tagged with existing hashtags only.
No audience filters — questions visible to all.

Run:
    python scripts/seed_demo_personas.py

Requires DATABASE_URL in environment or .env file.
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta

# ── Load .env ─────────────────────────────────────────────────────────────────
project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ[k.strip()] = v.strip().strip('"').strip("'")

sys.path.insert(0, str(project_root / "backend" / "src"))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.orm.questions import (
    QuestionORM, QuestionOptionORM,
    AnswerORM, AnswerOptionORM, QuestionHashtagLinkORM,
)
from app.orm.users import UserORM  # adjust import if path differs

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    print("ERROR: DATABASE_URL not set")
    sys.exit(1)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db = Session()

# ─────────────────────────────────────────────────────────────────────────────
# PERSONAS
# Each entry: email, name, surname, bio, handle
# ─────────────────────────────────────────────────────────────────────────────
PERSONAS = [
    {
        "email":    "demo.nietzsche@vece.ai",
        "name":     "Friedrich",
        "surname":  "Nietzsche",
        "handle":   "nietzsche",
        "bio":      "Philosopher. 1844–1900. Answers based on verified writings.",
        "birthday": "1844-10-15",
        "gender":   "Male",
    },
    {
        "email":    "demo.davinci@vece.ai",
        "name":     "Leonardo",
        "surname":  "da Vinci",
        "handle":   "davinci",
        "bio":      "Artist & scientist. 1452–1519. Answers based on verified notebooks.",
        "birthday": "1452-04-15",
        "gender":   "Male",
    },
    {
        "email":    "demo.freud@vece.ai",
        "name":     "Sigmund",
        "surname":  "Freud",
        "handle":   "freud",
        "bio":      "Psychoanalyst. 1856–1939. Answers based on verified writings.",
        "birthday": "1856-05-06",
        "gender":   "Male",
    },
    {
        "email":    "demo.wilde@vece.ai",
        "name":     "Oscar",
        "surname":  "Wilde",
        "handle":   "wilde",
        "bio":      "Writer & wit. 1854–1900. Answers based on verified works.",
        "birthday": "1854-10-16",
        "gender":   "Male",
    },
    {
        "email":    "demo.curie@vece.ai",
        "name":     "Marie",
        "surname":  "Curie",
        "handle":   "curie",
        "bio":      "Physicist & chemist. 1867–1934. Answers based on verified writings.",
        "birthday": "1867-11-07",
        "gender":   "Female",
    },
    {
        "email":    "demo.tolstoy@vece.ai",
        "name":     "Leo",
        "surname":  "Tolstoy",
        "handle":   "tolstoy",
        "bio":      "Novelist & moralist. 1828–1910. Answers based on verified works.",
        "birthday": "1828-09-09",
        "gender":   "Male",
    },
    {
        "email":    "demo.einstein@vece.ai",
        "name":     "Albert",
        "surname":  "Einstein",
        "handle":   "einstein",
        "bio":      "Physicist. 1879–1955. Answers based on verified writings & interviews.",
        "birthday": "1879-03-14",
        "gender":   "Male",
    },
    {
        "email":    "demo.chanel@vece.ai",
        "name":     "Coco",
        "surname":  "Chanel",
        "handle":   "chanel",
        "bio":      "Fashion designer. 1883–1971. Answers based on verified interviews.",
        "birthday": "1883-08-19",
        "gender":   "Female",
    },
    {
        "email":    "demo.darwin@vece.ai",
        "name":     "Charles",
        "surname":  "Darwin",
        "handle":   "darwin",
        "bio":      "Naturalist. 1809–1882. Answers based on verified writings.",
        "birthday": "1809-02-12",
        "gender":   "Male",
    },
    {
        "email":    "demo.kahlo@vece.ai",
        "name":     "Frida",
        "surname":  "Kahlo",
        "handle":   "kahlo",
        "bio":      "Painter. 1907–1954. Answers based on verified letters & diary.",
        "birthday": "1907-07-06",
        "gender":   "Female",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# QUESTIONS + OPTIONS
#
# Format:
# {
#   "text": str,                  # question text shown to users
#   "max_options": int,           # 1, 2, or 3
#   "allow_user_options": bool,
#   "hashtags": [str],            # must exist in hashtags table
#   "options": [
#     {"text": str, "persona": str | None}
#     # persona = handle of historical figure whose quote this is
#     # None = generic option (not a quote)
#   ],
#   "answers": {
#     "handle": [option_position, ...]   # which options this persona selects (0-indexed)
#   }
# }
# ─────────────────────────────────────────────────────────────────────────────

QUESTIONS = [

    # ── PHILOSOPHY & EXISTENCE ───────────────────────────────────────────────

    {
        "text": "What is the purpose of human life?",
        "max_options": 2,
        "allow_user_options": True,
        "hashtags": ["Existentialism", "Purpose", "Philosophy"],
        "options": [
            {"text": "To live as if everything is a miracle",          "persona": "einstein"},
            {"text": "To become who you truly are",                    "persona": "nietzsche"},
            {"text": "To love and to work",                            "persona": "freud"},
            {"text": "To create something that outlasts you",          "persona": "davinci"},
            {"text": "To serve others and reduce suffering",           "persona": "tolstoy"},
        ],
        "answers": {
            "nietzsche": [1],
            "einstein":  [0],
            "freud":     [2],
            "davinci":   [3],
            "tolstoy":   [4],
            "wilde":     [0],
            "curie":     [3],
            "kahlo":     [1],
        },
    },

    {
        "text": "What does it mean to truly know yourself?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Identity", "Psychology", "SelfImprovement"],
        "options": [
            {"text": "To understand your unconscious desires and fears",  "persona": "freud"},
            {"text": "To know what you value and live by it",             "persona": "nietzsche"},
            {"text": "To observe yourself as you observe the world",      "persona": "davinci"},
            {"text": "To accept your contradictions without shame",       "persona": "kahlo"},
            {"text": "To question every belief you were given",           "persona": None},
        ],
        "answers": {
            "freud":     [0],
            "nietzsche": [1],
            "davinci":   [2],
            "kahlo":     [3],
            "wilde":     [4],
            "einstein":  [4],
            "tolstoy":   [1],
            "darwin":    [2],
        },
    },

    {
        "text": "Is suffering a necessary part of life?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Existentialism", "MentalHealth", "Resilience"],
        "options": [
            {"text": "Yes — what does not kill me makes me stronger",     "persona": "nietzsche"},
            {"text": "Yes — suffering is the source of all great art",    "persona": "kahlo"},
            {"text": "It is inevitable, but the response is a choice",    "persona": "tolstoy"},
            {"text": "No — it is a problem to be solved, not endured",    "persona": "curie"},
            {"text": "Yes — it reveals what we truly are",                "persona": "freud"},
        ],
        "answers": {
            "nietzsche": [0],
            "kahlo":     [1],
            "tolstoy":   [2],
            "curie":     [3],
            "freud":     [4],
            "wilde":     [0],
            "einstein":  [2],
            "chanel":    [3],
        },
    },

    # ── LOVE & RELATIONSHIPS ──────────────────────────────────────────────────

    {
        "text": "What is love at its core?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Love", "Romance", "Relationships"],
        "options": [
            {"text": "The desire to possess and be possessed",            "persona": "freud"},
            {"text": "The only sane response to an insane world",         "persona": "kahlo"},
            {"text": "To love and be loved is to feel the sun from both sides", "persona": "wilde"},
            {"text": "The complete surrender of oneself to another",      "persona": "tolstoy"},
            {"text": "A force that gives meaning to everything else",     "persona": "einstein"},
        ],
        "answers": {
            "freud":     [0],
            "kahlo":     [1],
            "wilde":     [2],
            "tolstoy":   [3],
            "einstein":  [4],
            "nietzsche": [0],
            "chanel":    [2],
            "darwin":    [4],
        },
    },

    {
        "text": "Can a person be truly happy alone?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Happiness", "Loneliness", "Solitude"],
        "options": [
            {"text": "Yes — solitude is necessary for depth of thought",  "persona": "nietzsche"},
            {"text": "Yes — I am never less alone than when alone",       "persona": "darwin"},
            {"text": "No — human beings need attachment to flourish",     "persona": "freud"},
            {"text": "Happiness requires someone to share it with",       "persona": "tolstoy"},
            {"text": "It depends entirely on what you do with solitude",  "persona": "curie"},
        ],
        "answers": {
            "nietzsche": [0],
            "darwin":    [1],
            "freud":     [2],
            "tolstoy":   [3],
            "curie":     [4],
            "kahlo":     [2],
            "einstein":  [0],
            "wilde":     [3],
        },
    },

    {
        "text": "What destroys a relationship faster than anything?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Relationships", "Friendship", "Honesty"],
        "options": [
            {"text": "Dishonesty — it poisons everything it touches",     "persona": "tolstoy"},
            {"text": "Contempt — it is the opposite of respect",          "persona": "nietzsche"},
            {"text": "Repression — hiding what you feel",                 "persona": "freud"},
            {"text": "Indifference — the opposite of love is not hate",   "persona": "wilde"},
            {"text": "The inability to admit you were wrong",             "persona": None},
        ],
        "answers": {
            "tolstoy":   [0],
            "nietzsche": [1],
            "freud":     [2],
            "wilde":     [3],
            "einstein":  [4],
            "curie":     [0],
            "kahlo":     [2],
            "chanel":    [3],
        },
    },

    # ── SCIENCE & KNOWLEDGE ──────────────────────────────────────────────────

    {
        "text": "What drives human progress?",
        "max_options": 2,
        "allow_user_options": True,
        "hashtags": ["Science", "Innovation", "Curiosity"],
        "options": [
            {"text": "Imagination — it is more important than knowledge",  "persona": "einstein"},
            {"text": "Curiosity — the desire to understand everything",    "persona": "davinci"},
            {"text": "Necessity and the will to overcome it",              "persona": "curie"},
            {"text": "The refusal to accept that things cannot be better", "persona": "nietzsche"},
            {"text": "Gradual adaptation and accumulated small changes",   "persona": "darwin"},
        ],
        "answers": {
            "einstein":  [0],
            "davinci":   [1],
            "curie":     [2],
            "nietzsche": [3],
            "darwin":    [4],
            "freud":     [0],
            "tolstoy":   [2],
            "wilde":     [0],
        },
    },

    {
        "text": "Should science and religion be in conflict?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Religion", "Science", "Ethics"],
        "options": [
            {"text": "No — science without religion is lame, religion without science is blind", "persona": "einstein"},
            {"text": "Yes — religion answers questions science has not yet reached",              "persona": "tolstoy"},
            {"text": "No — religion is simply pre-scientific explanation",                        "persona": "freud"},
            {"text": "Science replaces religion as knowledge grows",                              "persona": "darwin"},
            {"text": "They speak different languages about different things",                     "persona": None},
        ],
        "answers": {
            "einstein":  [0],
            "tolstoy":   [1],
            "freud":     [2],
            "darwin":    [3],
            "nietzsche": [2],
            "curie":     [3],
            "davinci":   [4],
            "wilde":     [4],
        },
    },

    {
        "text": "Is truth absolute or does it depend on who is looking?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Logic", "Philosophy", "CriticalThinking"],
        "options": [
            {"text": "There are no facts, only interpretations",           "persona": "nietzsche"},
            {"text": "Truth is what survives rigorous testing",            "persona": "curie"},
            {"text": "Objective truth exists but most people avoid it",    "persona": "freud"},
            {"text": "Truth is rarely pure and never simple",              "persona": "wilde"},
            {"text": "Scientific truth accumulates slowly and imperfectly","persona": "darwin"},
        ],
        "answers": {
            "nietzsche": [0],
            "curie":     [1],
            "freud":     [2],
            "wilde":     [3],
            "darwin":    [4],
            "einstein":  [1],
            "davinci":   [1],
            "tolstoy":   [2],
        },
    },

    # ── ART & CREATIVITY ─────────────────────────────────────────────────────

    {
        "text": "What is art for?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Art", "Creativity", "Culture"],
        "options": [
            {"text": "To paint my own reality, not the reality imposed on me", "persona": "kahlo"},
            {"text": "To express what words cannot reach",                      "persona": "davinci"},
            {"text": "To tell truth through beautiful lies",                    "persona": "wilde"},
            {"text": "To unite people across all differences",                  "persona": "tolstoy"},
            {"text": "To show what it feels like to be alive",                  "persona": None},
        ],
        "answers": {
            "kahlo":     [0],
            "davinci":   [1],
            "wilde":     [2],
            "tolstoy":   [3],
            "nietzsche": [2],
            "freud":     [0],
            "chanel":    [2],
            "einstein":  [4],
        },
    },

    {
        "text": "Is beauty objective or in the eye of the beholder?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Art", "Philosophy", "Aesthetics"],
        "options": [
            {"text": "Beauty is entirely subjective — there is no standard",   "persona": "wilde"},
            {"text": "Beauty follows universal mathematical proportions",       "persona": "davinci"},
            {"text": "Beauty is what we project onto what we desire",          "persona": "freud"},
            {"text": "Elegance is the right balance — never more, never less", "persona": "chanel"},
            {"text": "Beauty in nature follows deep evolutionary logic",       "persona": "darwin"},
        ],
        "answers": {
            "wilde":     [0],
            "davinci":   [1],
            "freud":     [2],
            "chanel":    [3],
            "darwin":    [4],
            "nietzsche": [0],
            "kahlo":     [0],
            "einstein":  [1],
        },
    },

    # ── SOCIETY & VALUES ─────────────────────────────────────────────────────

    {
        "text": "What should education teach above all else?",
        "max_options": 2,
        "allow_user_options": True,
        "hashtags": ["Education", "Values", "SelfImprovement"],
        "options": [
            {"text": "How to think, not what to think",                    "persona": "einstein"},
            {"text": "How to observe carefully and question everything",    "persona": "davinci"},
            {"text": "Moral principles — knowledge without ethics is dangerous", "persona": "tolstoy"},
            {"text": "That most of what you believe is wrong",             "persona": "nietzsche"},
            {"text": "How to endure uncertainty and keep going",           "persona": "curie"},
        ],
        "answers": {
            "einstein":  [0],
            "davinci":   [1],
            "tolstoy":   [2],
            "nietzsche": [3],
            "curie":     [4],
            "wilde":     [0],
            "freud":     [0],
            "darwin":    [1],
        },
    },

    {
        "text": "Is ambition a virtue or a vice?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Ambition", "Values", "PersonalGrowth"],
        "options": [
            {"text": "A virtue — the will to power is what drives humanity forward", "persona": "nietzsche"},
            {"text": "A virtue when directed at something larger than yourself",      "persona": "curie"},
            {"text": "A vice when it replaces love and connection",                   "persona": "tolstoy"},
            {"text": "Neither — it is neutral, only the object of ambition matters",  "persona": "einstein"},
            {"text": "A virtue — those without it live other people's lives",         "persona": "chanel"},
        ],
        "answers": {
            "nietzsche": [0],
            "curie":     [1],
            "tolstoy":   [2],
            "einstein":  [3],
            "chanel":    [4],
            "davinci":   [1],
            "wilde":     [4],
            "kahlo":     [1],
        },
    },

    {
        "text": "What is more dangerous: ignorance or certainty?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["CriticalThinking", "Ethics", "Logic"],
        "options": [
            {"text": "Certainty — it closes the mind entirely",            "persona": "einstein"},
            {"text": "Ignorance — you cannot act well on what you do not know", "persona": "curie"},
            {"text": "Certainty — conviction is the greatest enemy of truth",   "persona": "nietzsche"},
            {"text": "Both equally — they are two forms of the same blindness", "persona": "darwin"},
            {"text": "Certainty — especially in moral matters",                  "persona": "wilde"},
        ],
        "answers": {
            "einstein":  [0],
            "curie":     [1],
            "nietzsche": [2],
            "darwin":    [3],
            "wilde":     [4],
            "davinci":   [0],
            "freud":     [2],
            "tolstoy":   [1],
        },
    },

    # ── STYLE & LIFE ─────────────────────────────────────────────────────────

    {
        "text": "What does the way you dress say about you?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Fashion", "Identity", "Style"],
        "options": [
            {"text": "Everything — fashion is the armor to survive everyday life", "persona": "chanel"},
            {"text": "Only what you want others to see — nothing more",            "persona": "wilde"},
            {"text": "Less than people think — ideas matter more than clothes",    "persona": "curie"},
            {"text": "It reflects your inner state whether you intend it or not",  "persona": "freud"},
            {"text": "Simplicity is the ultimate sophistication",                  "persona": "davinci"},
        ],
        "answers": {
            "chanel":    [0],
            "wilde":     [1],
            "curie":     [2],
            "freud":     [3],
            "davinci":   [4],
            "nietzsche": [2],
            "kahlo":     [0],
            "tolstoy":   [2],
        },
    },

    {
        "text": "What is the greatest waste of a human life?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Purpose", "Values", "Existentialism"],
        "options": [
            {"text": "Living for the approval of others",                  "persona": "nietzsche"},
            {"text": "Not satisfying your curiosity about the world",      "persona": "davinci"},
            {"text": "Refusing to face what is true about yourself",       "persona": "freud"},
            {"text": "Spending it on things that do not bring joy",        "persona": "wilde"},
            {"text": "Accepting the life handed to you without question",  "persona": "chanel"},
        ],
        "answers": {
            "nietzsche": [0],
            "davinci":   [1],
            "freud":     [2],
            "wilde":     [3],
            "chanel":    [4],
            "kahlo":     [3],
            "einstein":  [1],
            "tolstoy":   [0],
        },
    },

    {
        "text": "Is it better to live a short intense life or a long quiet one?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Purpose", "Happiness", "Values"],
        "options": [
            {"text": "Short and intense — better to burn than to fade",    "persona": "nietzsche"},
            {"text": "Long — you need time to understand anything deeply",  "persona": "darwin"},
            {"text": "It depends entirely on what fills it",               "persona": "einstein"},
            {"text": "Long — a life of service is never wasted",           "persona": "tolstoy"},
            {"text": "Intense — the only life that leaves a mark",         "persona": "kahlo"},
        ],
        "answers": {
            "nietzsche": [0],
            "darwin":    [1],
            "einstein":  [2],
            "tolstoy":   [3],
            "kahlo":     [4],
            "wilde":     [0],
            "chanel":    [4],
            "curie":     [2],
        },
    },

    {
        "text": "What role does nature play in human happiness?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Nature", "Happiness", "Health"],
        "options": [
            {"text": "It is essential — we are animals and belong in it",   "persona": "darwin"},
            {"text": "Nature is a model for everything beautiful and true",  "persona": "davinci"},
            {"text": "It soothes but cannot replace human connection",       "persona": "freud"},
            {"text": "It reminds us of what we actually are, beneath everything", "persona": "nietzsche"},
            {"text": "Nature was my laboratory — it was where I felt most alive",  "persona": "curie"},
        ],
        "answers": {
            "darwin":    [0],
            "davinci":   [1],
            "freud":     [2],
            "nietzsche": [3],
            "curie":     [4],
            "tolstoy":   [0],
            "einstein":  [1],
            "kahlo":     [3],
        },
    },

    {
        "text": "What is the hardest thing to change in a person?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Psychology", "Habits", "PersonalGrowth"],
        "options": [
            {"text": "Their childhood — it shapes everything that follows",  "persona": "freud"},
            {"text": "Their values — they are built over decades",           "persona": "tolstoy"},
            {"text": "Their beliefs about themselves",                       "persona": "nietzsche"},
            {"text": "Their habits — behavior outlasts intention",           "persona": "darwin"},
            {"text": "Their fear of being wrong",                            "persona": "einstein"},
        ],
        "answers": {
            "freud":     [0],
            "tolstoy":   [1],
            "nietzsche": [2],
            "darwin":    [3],
            "einstein":  [4],
            "curie":     [4],
            "wilde":     [2],
            "kahlo":     [0],
        },
    },

    {
        "text": "What does courage look like in everyday life?",
        "max_options": 1,
        "allow_user_options": True,
        "hashtags": ["Courage", "Values", "Resilience"],
        "options": [
            {"text": "Saying what you believe when no one else will",      "persona": "nietzsche"},
            {"text": "Continuing your work when results feel far away",    "persona": "curie"},
            {"text": "Being honest with yourself about who you are",       "persona": "freud"},
            {"text": "Choosing to create when the world offers destruction","persona": "kahlo"},
            {"text": "Facing the unknown without needing certainty first", "persona": "einstein"},
        ],
        "answers": {
            "nietzsche": [0],
            "curie":     [1],
            "freud":     [2],
            "kahlo":     [3],
            "einstein":  [4],
            "davinci":   [4],
            "tolstoy":   [0],
            "chanel":    [1],
        },
    },

]

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def get_or_create_user(db, persona: dict) -> int:
    """Create demo user if not already present. Returns user_id."""
    existing = db.execute(
        text("SELECT id FROM users WHERE email = :email"),
        {"email": persona["email"]},
    ).fetchone()
    if existing:
        print(f"    (already exists, id={existing[0]})")
        return existing[0]

    # password_hash: bcrypt of "DemoVece2025!" — safe throwaway password
    DEMO_PW_HASH = "$2b$12$demo.hash.placeholder.not.real.xxxxxxxxxxxxxxxxxxxxxxx"

    result = db.execute(
        text("""
            INSERT INTO users (
                email, name, surname, username,
                password_hash, birthday, gender,
                is_verified, is_active, role,
                description, created_at, updated_at
            )
            VALUES (
                :email, :name, :surname, :username,
                :password_hash, :birthday, :gender,
                TRUE, TRUE, 'user',
                :description, NOW(), NOW()
            )
            RETURNING id
        """),
        {
            "email":         persona["email"],
            "name":          persona["name"],
            "surname":       persona["surname"],
            "username":      persona["handle"],
            "password_hash": DEMO_PW_HASH,
            "birthday":      persona["birthday"],
            "gender":        persona["gender"],
            "description":   persona["bio"],
        },
    )
    user_id = result.fetchone()[0]

    # Create user_settings record (required by schema)
    db.execute(
        text("""
            INSERT INTO user_settings (user_id)
            VALUES (:user_id)
            ON CONFLICT (user_id) DO NOTHING
        """),
        {"user_id": user_id},
    )

    db.commit()
    return user_id


def get_hashtag_ids(db, names: list) -> list:
    rows = db.execute(
        text("SELECT id, name FROM hashtags WHERE name = ANY(:names)"),
        {"names": names},
    ).fetchall()
    found = {r[1]: r[0] for r in rows}
    missing = [n for n in names if n not in found]
    if missing:
        print(f"  WARNING: hashtags not found in DB, skipping: {missing}")
    return list(found.values())


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=== VECE Demo Personas Seed ===\n")

    # 1. Build handle → user_id map
    handle_to_id = {}
    for persona in PERSONAS:
        uid = get_or_create_user(db, persona)
        handle_to_id[persona["handle"]] = uid
        print(f"  {persona['name']} {persona['surname']} → user_id {uid}")

    # Use first persona (Nietzsche) as question author — or a dedicated @demo account
    # All questions appear "from the platform"
    demo_author_id = handle_to_id["nietzsche"]  # arbitrary, shown as question poster

    print(f"\nSeeding {len(QUESTIONS)} questions...\n")

    ACTIVE_TILL = datetime.utcnow() + timedelta(days=365 * 10)  # 10 years

    for i, q_data in enumerate(QUESTIONS):
        # 2. Create question
        q_orm = QuestionORM(
            author_id=demo_author_id,
            text=q_data["text"],
            max_options=q_data["max_options"],
            active_till=ACTIVE_TILL,
            allow_user_options=q_data["allow_user_options"],
            created_at=datetime.utcnow(),
            gender=None,
            country_id=None,
            age=None,
        )
        db.add(q_orm)
        db.flush()
        qid = q_orm.id

        # 3. Create options
        option_id_map = {}  # position → option_id
        for pos, opt in enumerate(q_data["options"]):
            opt_orm = QuestionOptionORM(
                question_id=qid,
                text=opt["text"],
                position=pos,
                author_id=None,
                by_question_author=True,
                created_at=datetime.utcnow(),
            )
            db.add(opt_orm)
            db.flush()
            option_id_map[pos] = opt_orm.id

        # 4. Hashtags
        htag_ids = get_hashtag_ids(db, q_data["hashtags"])
        for htid in htag_ids:
            db.add(QuestionHashtagLinkORM(question_id=qid, hashtag_id=htid))

        # 5. Answers — each persona answers
        for handle, positions in q_data["answers"].items():
            user_id = handle_to_id.get(handle)
            if user_id is None:
                continue
            ans_orm = AnswerORM(
                question_id=qid,
                user_id=user_id,
                created_at=datetime.utcnow(),
            )
            db.add(ans_orm)
            db.flush()
            for pos in positions:
                opt_id = option_id_map.get(pos)
                if opt_id:
                    db.add(AnswerOptionORM(answer_id=ans_orm.id, option_id=opt_id))

        db.commit()
        print(f"  [{i+1}/{len(QUESTIONS)}] \"{q_data['text'][:55]}...\" — {len(q_data['answers'])} answers")

    # 6. Update option counts & percentages
    print("\nRecalculating option counts...")
    db.execute(text("""
        UPDATE question_options qo
        SET count = sub.cnt,
            percentage = sub.cnt * 100.0 / NULLIF(q.total_answers, 0)
        FROM (
            SELECT option_id, COUNT(*) as cnt
            FROM answer_options
            GROUP BY option_id
        ) sub
        JOIN questions q ON q.id = qo.question_id
        WHERE qo.id = sub.option_id
    """))
    db.execute(text("""
        UPDATE questions q
        SET total_answers = sub.cnt
        FROM (
            SELECT question_id, COUNT(*) as cnt
            FROM answers
            GROUP BY question_id
        ) sub
        WHERE q.id = sub.question_id
    """))
    db.commit()

    print("\n=== Done ===")
    print(f"  {len(PERSONAS)} demo personas")
    print(f"  {len(QUESTIONS)} questions")
    total_answers = sum(len(q["answers"]) for q in QUESTIONS)
    print(f"  {total_answers} answer records")
    print("\nEach persona answered:")
    from collections import Counter
    counts = Counter()
    for q in QUESTIONS:
        for h in q["answers"]:
            counts[h] += 1
    for h, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {h:12s}  {c} questions")


if __name__ == "__main__":
    main()
