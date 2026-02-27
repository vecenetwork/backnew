from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime, timedelta
import random

from app.orm.questions import QuestionOptionORM, QuestionORM, AnswerORM, AnswerOptionORM, QuestionHashtagLinkORM


def populate_questions_answers(db_url: str, user_ids: list, hashtag_ids: list):
    """Populates the questions, question_options, answers, and answer_options tables, including hashtag associations."""

    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    fake = Faker()

    questions_data = []
    options_data = []
    answers_data = []
    answer_options_data = []
    question_hashtag_links_data = []

    for _ in range(1000):  # Generate 1000 questions
        max_options = random.randint(3, 10)
        active_till = datetime.utcnow() + timedelta(days=random.randint(1, 30))
        gender_options = random.sample(["Male", "Female", "Other"], random.randint(0, 3)) if random.random() < 0.5 else None
        country_options = random.sample(user_ids, random.randint(0, len(user_ids))) if random.random() < 0.5 else None
        age_start = random.randint(18, 60) if random.random() < 0.5 else None
        age_end = random.randint(age_start, 80) if age_start is not None else None
        age_range = f"[{age_start},{age_end}]" if age_start is not None else None

        question_data = {
            "author_id": random.choice(user_ids),
            "text": fake.sentence(),
            "max_options": max_options,
            "active_till": active_till,
            "allow_user_options": fake.boolean(),
            "created_at": datetime.utcnow(),
            "gender": gender_options,
            "country_id": country_options,
            "age": age_range,
        }
        questions_data.append(question_data)

    db.bulk_save_objects([QuestionORM(**q) for q in questions_data])
    db.commit()

    question_ids = [q.id for q in db.query(QuestionORM).all()]

    for question_id in question_ids:
        question = db.query(QuestionORM).filter(QuestionORM.id == question_id).first()

        # Generate hashtag associations
        selected_hashtag_ids = random.sample(hashtag_ids, random.randint(7, 10))
        for hashtag_id in selected_hashtag_ids:
            question_hashtag_links_data.append(QuestionHashtagLinkORM(
                question_id=question_id,
                hashtag_id=hashtag_id,
            ))

        for position in range(question.max_options):
            option_data = {
                "question_id": question_id,
                "text": fake.sentence(),
                "position": position,
                "author_id": random.choice(user_ids) if fake.boolean() else None,
                "by_question_author": fake.boolean(),
                "created_at": datetime.utcnow(),
            }
            options_data.append(option_data)

    db.bulk_save_objects([QuestionOptionORM(**o) for o in options_data])
    db.bulk_save_objects(question_hashtag_links_data)
    db.commit()

    for question_id in question_ids:
        # Generate answers for each question, ensuring uniqueness
        answered_users = set()  # prevent duplicate answers
        for _ in range(min(10, len(user_ids))):  # Generate some answers per question, prevent too many answers.
            user_id = random.choice(user_ids)
            while (question_id, user_id) in answered_users:  # prevent duplicate answers
                user_id = random.choice(user_ids)
            answered_users.add((question_id, user_id))
            answer_data = {
                "question_id": question_id,
                "user_id": user_id,
                "created_at": datetime.utcnow(),
            }
            answers_data.append(answer_data)

    db.bulk_save_objects([AnswerORM(**a) for a in answers_data])
    db.commit()

    answer_ids = [a.id for a in db.query(AnswerORM).all()]

    for answer_id in answer_ids:
        answer = db.query(AnswerORM).filter(AnswerORM.id == answer_id).first()
        question = db.query(QuestionORM).filter(QuestionORM.id == answer.question_id).first()
        answer_option_count = random.randint(1, min(3, question.max_options))
        selected_option_ids = random.sample([opt.id for opt in question.options], answer_option_count)

        for option_id in selected_option_ids:
            answer_options_data.append({
                "answer_id": answer_id,
                "option_id": option_id,
            })

    db.bulk_save_objects(
        [AnswerOptionORM(**ao) for ao in answer_options_data]
    )
    db.commit()
    db.close()
