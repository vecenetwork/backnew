#!/usr/bin/env python3
"""Seeds the Golden 450 hashtags into the database."""
import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ[k.strip()] = v.strip().strip('"').strip("'")


HASHTAGS = [
    "AbandonedPlaces", "Psychology", "Emotions", "PersonalityTypes", "MBTI",
    "Mindfulness", "Meditation", "SelfEsteem", "Identity", "Dreams",
    "Spirituality", "Religion", "Atheism", "Agnosticism", "Ethics",
    "Morality", "Logic", "CriticalThinking", "Introversion", "Extroversion",
    "Resilience", "Nostalgia", "Ambition", "Discipline", "TimeManagement",
    "Happiness", "Loneliness", "Stoicism", "Optimism", "Pessimism",
    "Confidence", "Empathy", "Forgiveness", "Loyalty", "Courage",
    "Curiosity", "Intuition", "Habits", "Procrastination", "Existentialism",
    "SelfCare", "SelfImprovement", "PersonalGrowth", "Values", "Minimalism",
    "Purpose", "MentalHealth", "Anxiety", "StressManagement", "Grief",
    "Health", "Longevity", "Sleep", "Nutrition", "Dieting",
    "PlantBased", "Veganism", "Vegetarianism", "IntermittentFasting", "Supplements",
    "Biohacking", "Skincare", "Haircare", "Hygiene", "Fitness",
    "GymLife", "Yoga", "Pilates", "CrossFit", "Bodybuilding",
    "Calisthenics", "Aerobics", "Running", "Swimming", "Cycling",
    "Walking", "Athletics", "SportsScience", "Healthcare", "MedicalTech",
    "Aging", "Bioethics", "PhysicalTherapy", "BodyImage", "BodyPositivity",
    "FirstAid", "ImmuneSystem", "Metabolism", "Posture", "Flexibility",
    "DentalHealth", "HolisticHealth", "AlternativeMedicine", "Pharmacy", "Anatomy",
    "Physiology", "MentalClarity", "Hydration", "EnergyLevels", "Recovery",
    "Dating", "DatingApps", "Romance", "Marriage", "Divorce",
    "FamilyDynamics", "Parenting", "Childhood", "Adolescence", "Grandparents",
    "Siblings", "Friendship", "BestFriends", "SocialSkills", "Networking",
    "Community", "Neighbors", "Solitude", "SocialAnxiety", "PublicSpeaking",
    "ConflictResolution", "Masculinity", "Femininity", "LGBTQ", "GenderEquality",
    "SocialJustice", "Mentorship", "Leadership", "Teamwork", "Hospitality",
    "Etiquette", "Charisma", "Persuasion", "GroupDynamics", "PeerPressure",
    "OnlineCommunities", "LongDistance", "Heartbreak", "Jealousy", "Betrayal",
    "Honesty", "Boundaries", "SmallTalk", "StoryTelling", "Diplomacy",
    "Collaboration", "ParentingStyles", "EarlyEducation", "Adoption",
    "Finance", "Investing", "RealEstate", "StockMarket", "Cryptocurrency",
    "Bitcoin", "Blockchain", "Banking", "Economics", "Capitalism",
    "Socialism", "Wealth", "Poverty", "Inequality", "Inflation",
    "Taxes", "Accounting", "Insurance", "Budgeting", "Savings",
    "Debt", "Retirement", "Career", "CareerChange", "JobSearch",
    "ResumeWriting", "Freelancing", "RemoteWork", "Entrepreneurship", "Startups",
    "VentureCapital", "Management", "Productivity", "WorkLifeBalance", "SideHustle",
    "PassiveIncome", "Marketing", "Advertising", "DigitalMarketing", "PersonalBranding",
    "Sales", "CustomerService", "BusinessStrategy", "ProfessionalEthics", "CorporateCulture",
    "Logistics", "ECommerce", "Retail", "Manufacturing", "TechIndustry",
    "HumanResources", "Consulting", "PublicRelations", "SmallBusiness", "Franchising",
    "GlobalTrade", "CommercialProperty", "NonProfit", "Philanthropy", "Fundraising",
    "Home", "InteriorDesign", "Architecture", "Urbanism", "UrbanPlanning",
    "SmartHome", "HomeRenovation", "DIY", "Gardening", "Landscaping",
    "Organizing", "SustainableLiving", "ZeroWaste", "Fashion", "Style",
    "Streetwear", "SustainableFashion", "Vintage", "Thrifting", "Jewelry",
    "Accessories", "Cosmetics", "Travel", "Backpacking", "SoloTravel",
    "LuxuryTravel", "Glamping", "RoadTrips", "Hotels", "Gastronomy",
    "Cooking", "Baking", "Recipes", "FineDining", "StreetFood",
    "FastFood", "ComfortFood", "HomeCooking", "Foodie", "CoffeeCulture",
    "Tea", "Wine", "CraftBeer", "Cocktails", "Spirits",
    "Desserts", "Pastries", "Breakfast", "Brunch", "Seafood",
    "Steaks", "Spices", "EthnicCuisine", "Superfoods", "FoodDelivery",
    "Restaurants", "GroceryShopping", "Pets", "Dogs", "Cats",
    "FishKeeping", "DailyRoutine", "Commuting", "ApartmentLiving", "CityLife",
    "CountryLife", "SuburbanLife", "TinyHouse", "Art", "Painting",
    "Sculpture", "Drawing", "GraphicDesign", "Photography", "Videography",
    "Cinema", "Movies", "TVSeries", "Documentary", "RealityTV",
    "TrueCrime", "Podcasts", "Radio", "AudioBooks", "Literature",
    "Fiction", "NonFiction", "Novels", "ShortStories", "Poetry",
    "Writing", "Copywriting", "Journalism", "News", "SocialMedia",
    "Influencers", "TikTokCulture", "YouTube", "Music", "Concerts",
    "Festivals", "HipHop", "RockMusic", "PopMusic", "EDM",
    "Techno", "Jazz", "ClassicalMusic", "IndieMusic", "KPop",
    "MetalMusic", "Gaming", "VideoGames", "Esports", "BoardGames",
    "Chess", "RolePlayingGames", "TabletopGames", "StandUpComedy", "Humor",
    "Memes", "Theater", "Dance", "MusicalInstruments", "Piano",
    "Guitar", "Drums", "Collecting", "Technology", "ArtificialIntelligence",
    "MachineLearning", "Robotics", "Automation", "Future", "Futurism",
    "Gadgets", "Smartphones", "Computers", "Software", "Coding",
    "Programming", "AppDevelopment", "WebDesign", "Cybersecurity", "DataPrivacy",
    "BigData", "CloudComputing", "InternetCulture", "Algorithms", "SocialMediaAlgorithms",
    "Metaverse", "VR", "AR", "SpaceExploration", "SpaceTravel",
    "Astronomy", "Satellites", "RenewableEnergy", "ElectricVehicles", "BatteryTech",
    "SmartCities", "DigitalEthics", "Biometrics", "3DPrinting", "Drones",
    "OpenSource", "Linux", "Hardware", "Nature", "Wildlife",
    "Ecology", "Sustainability", "ClimateChange", "Environmentalism", "Conservation",
    "Pollution", "Recycling", "Science", "Physics", "Biology",
    "Chemistry", "Genetics", "Geology", "Geography", "Earth",
    "Oceans", "MarineLife", "Forests", "Mountains", "Weather",
    "NaturalDisasters", "Agriculture", "Botany", "Zoology", "Archaeology",
    "Anthropology", "Evolution", "Fossils", "Universe", "Gravity",
    "DNA", "ScientificMethod", "Research", "Politics", "Democracy",
    "Geopolitics", "InternationalRelations", "Law", "Justice", "HumanRights",
    "FreeSpeech", "Censorship", "Activism", "Feminism", "Humanism",
    "Education", "University", "OnlineLearning", "History", "WorldHistory",
    "AncientCivilizations", "War", "Peace", "Government", "Citizenship",
    "Immigration", "Globalization", "Nationalism", "Propaganda", "PublicTransport",
    "Infrastructure", "NorthAmerica", "LATAM", "Europe", "Asia",
    "Africa",
    # Additional tags from demo questions
    "Professionalism", "DecisionMaking", "DigitalLife", "DigitalDetox", "Wellness",
    "Innovation", "Relationships", "Love", "Personality", "Experience", "PopCulture",
    "Risk", "GigEconomy", "PublicPolicy", "Knowledge", "Adventure", "Environment",
]


def main():
    import psycopg2

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

    # Deduplicate (Loyalty, Minimalism, Nutrition appear twice in original list)
    seen = set()
    unique = []
    for name in HASHTAGS:
        if name not in seen:
            seen.add(name)
            unique.append(name)

    # Single batch insert (much faster)
    cur.execute("SELECT COUNT(*) FROM hashtags")
    count_before = cur.fetchone()[0]

    cur.execute(
        """
        INSERT INTO hashtags (name)
        SELECT unnest(%s::text[])
        ON CONFLICT (name) DO NOTHING
        """,
        (unique,),
    )

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM hashtags")
    count_after = cur.fetchone()[0]
    conn.close()

    added = count_after - count_before
    print(f"✅ Hashtags in DB: {count_after} (added {added} new, {len(unique)} in list).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
