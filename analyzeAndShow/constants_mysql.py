db_names = ["UKSW_ANIMALS_RESULTS", "UKSW_APPEARANCE_RESULTS", "UKSW_ART_RESULTS", "UKSW_BIOLOGY_RESULTS", "UKSW_BIRDS_RESULTS", "UKSW_BODY_RESULTS", "UKSW_BUILDINGS_RESULTS", "UKSW_BUSINESS_RESULTS",
            "UKSW_CHANGE_CAUSE_AND_EFFECT_RESULTS", "UKSW_CLOTHES_AND_FASHION_RESULTS", "UKSW_COLOURS_AND_SHAPES_RESULTS", "UKSW_COMPUTERS_RESULTS", "UKSW_COOKING_AND_EATING_RESULTS",
            "UKSW_CRIME_AND_PUNISHMENT_RESULTS", "UKSW_DANGER_RESULTS", "UKSW_DIFFICULTY_AND_FAILURE_RESULTS", "UKSW_DISABILITY_RESULTS", "UKSW_DISCUSSION_AND_AGREEMENT_RESULTS",
            "UKSW_DOUBT_GUESSING_AND_CERTAINTY_RESULTS", "UKSW_DRINKS_RESULTS", "UKSW_EDUCATION_RESULTS", "UKSW_ENGINEERING_RESULTS", "UKSW_FAMILY_AND_RELATIONSHIPS_RESULTS", "UKSW_FARMING_RESULTS",
            "UKSW_FEELINGS_RESULTS", "UKSW_FILM_AND_THEATRE_RESULTS", "UKSW_FISH_AND_SHELLFISH_RESULTS", "UKSW_FOOD_RESULTS", "UKSW_GAMES_AND_TOYS_RESULTS", "UKSW_GARDENS_RESULTS",
            "UKSW_GEOGRAPHY_RESULTS", "UKSW_HEALTHCARE_RESULTS", "UKSW_HEALTH_AND_FITNESS_RESULTS", "UKSW_HEALTH_PROBLEMS_RESULTS", "UKSW_HISTORY_RESULTS", "UKSW_HOBBIES_RESULTS",
            "UKSW_HOLIDAYS_RESULTS", "UKSW_HOUSES_AND_HOMES_RESULTS", "UKSW_INSECTS_WORMS_ETC_RESULTS", "UKSW_JOBS_RESULTS", "UKSW_LANGUAGE_RESULTS", "UKSW_LAW_AND_JUSTICE_RESULTS",
            "UKSW_LIFE_STAGES_RESULTS", "UKSW_LITERATURE_AND_WRITING_RESULTS", "UKSW_MATHS_AND_MEASUREMENT_RESULTS", "UKSW_MENTAL_HEALTH_RESULTS", "UKSW_MONEY_RESULTS", "UKSW_MUSIC_RESULTS",
            "UKSW_OPINION_AND_ARGUMENT_RESULTS", "UKSW_PEOPLE_IN_SOCIETY_RESULTS", "UKSW_PERMISSION_AND_OBLIGATION_RESULTS", "UKSW_PERSONAL_QUALITIES_RESULTS",
            "UKSW_PHONES_EMAIL_AND_THE_INTERNET_RESULTS", "UKSW_PHYSICS_AND_CHEMISTRY_RESULTS", "UKSW_PLANTS_AND_TREES_RESULTS", "UKSW_POLITICS_RESULTS", "UKSW_PREFERENCES_AND_DECISIONS_RESULTS",
            "UKSW_RELIGION_AND_FESTIVALS_RESULTS", "UKSW_SCIENTIFIC_RESEARCH_RESULTS", "UKSW_SHOPPING_RESULTS", "UKSW_SOCIAL_ISSUES_RESULTS", "UKSW_SPACE_RESULTS",
            "UKSW_SPORTS_BALL_AND_RACKET_SPORTS_RESULTS", "UKSW_SPORTS_OTHER_SPORTS_RESULTS", "UKSW_SPORTS_WATER_SPORTS_RESULTS", "UKSW_SUCCESS_RESULTS", "UKSW_SUGGESTIONS_AND_ADVICE_RESULTS",
            "UKSW_THE_ENVIRONMENT_RESULTS", "UKSW_TIME_RESULTS", "UKSW_TRANSPORT_BY_AIR_RESULTS", "UKSW_TRANSPORT_BY_BUS_AND_TRAIN_RESULTS", "UKSW_TRANSPORT_BY_CAR_OR_LORRY_RESULTS",
            "UKSW_TRANSPORT_BY_WATER_RESULTS", "UKSW_TV_RADIO_AND_NEWS_RESULTS", "UKSW_WAR_AND_CONFLICT_RESULTS", "UKSW_WEATHER_RESULTS", "UKSW_WORKING_LIFE_RESULTS"]

all_categories = ['ANIMALS', 'APPEARANCE', 'ART', 'BIOLOGY', 'BIRDS', 'BODY', 'BUILDINGS', 'BUSINESS', 'CHANGE CAUSE AND EFFECT', 'CLOTHES AND FASHION', 'COLOURS AND SHAPES', 'COMPUTERS',
                  'COOKING AND EATING', 'CRIME AND PUNISHMENT', 'DANGER', 'DIFFICULTY AND FAILURE', 'DISABILITY', 'DISCUSSION AND AGREEMENT', 'DOUBT GUESSING AND CERTAINTY', 'DRINKS', 'EDUCATION',
                  'ENGINEERING', 'FAMILY AND RELATIONSHIPS', 'FARMING', 'FEELINGS', 'FILM AND THEATRE', 'FISH AND SHELLFISH', 'FOOD', 'GAMES AND TOYS', 'GARDENS', 'GEOGRAPHY', 'HEALTHCARE',
                  'HEALTH AND FITNESS', 'HEALTH PROBLEMS', 'HISTORY', 'HOBBIES', 'HOLIDAYS', 'HOUSES AND HOMES', 'INSECTS WORMS ETC', 'JOBS', 'LANGUAGE', 'LAW AND JUSTICE', 'LIFE STAGES',
                  'LITERATURE AND WRITING', 'MATHS AND MEASUREMENT', 'MENTAL HEALTH', 'MONEY', 'MUSIC', 'OPINION AND ARGUMENT', 'PEOPLE IN SOCIETY', 'PERMISSION AND OBLIGATION', 'PERSONAL QUALITIES',
                  'PHONES EMAIL AND THE INTERNET', 'PHYSICS AND CHEMISTRY', 'PLANTS AND TREES', 'POLITICS', 'PREFERENCES AND DECISIONS', 'RELIGION AND FESTIVALS', 'SCIENTIFIC RESEARCH', 'SHOPPING',
                  'SOCIAL ISSUES', 'SPACE', 'SPORTS BALL AND RACKET SPORTS', 'SPORTS OTHER SPORTS', 'SPORTS WATER SPORTS', 'SUCCESS', 'SUGGESTIONS AND ADVICE', 'THE ENVIRONMENT', 'TIME',
                  'TRANSPORT BY AIR', 'TRANSPORT BY BUS AND TRAIN', 'TRANSPORT BY CAR OR LORRY', 'TRANSPORT BY WATER', 'TV RADIO AND NEWS', 'WAR AND CONFLICT', 'WEATHER', 'WORKING LIFE']

# %%
tb_names = ["BelarusianVsEnglish", "BelarusianVsFrench", "BelarusianVsGerman", "BelarusianVsPolish", "BelarusianVsSpanish", "BulgarianVsBelarusian", "BulgarianVsEnglish", "BulgarianVsFrench",
            "BulgarianVsGerman", "BulgarianVsPolish", "BulgarianVsSpanish", "CroatianVsBelarusian", "CroatianVsBulgarian", "CroatianVsCzech", "CroatianVsDanish", "CroatianVsEnglish",
            "CroatianVsEstonian", "CroatianVsFinish", "CroatianVsFrench", "CroatianVsGerman", "CroatianVsGreek", "CroatianVsIrish", "CroatianVsPolish", "CroatianVsSpanish", "CroatianVsWelsh",
            "CzechVsBelarusian", "CzechVsBulgarian", "CzechVsEnglish", "CzechVsFrench", "CzechVsGerman", "CzechVsPolish", "CzechVsSpanish", "DanishVsBelarusian", "DanishVsBulgarian", "DanishVsCzech",
            "DanishVsEnglish", "DanishVsFrench", "DanishVsGerman", "DanishVsPolish", "DanishVsSpanish", "DanishVsWelsh", "EnglishVsGerman", "EnglishVsPolish", "EnglishVsSpanish",
            "EstonianVsBelarusian", "EstonianVsBulgarian", "EstonianVsCzech", "EstonianVsDanish", "EstonianVsEnglish", "EstonianVsFrench", "EstonianVsGerman", "EstonianVsGreek", "EstonianVsPolish",
            "EstonianVsSpanish", "EstonianVsWelsh", "FinishVsBelarusian", "FinishVsBulgarian", "FinishVsCzech", "FinishVsDanish", "FinishVsEnglish", "FinishVsEstonian", "FinishVsFrench",
            "FinishVsGerman", "FinishVsGreek", "FinishVsPolish", "FinishVsSpanish", "FinishVsWelsh", "FrenchVsEnglish", "FrenchVsGerman", "FrenchVsPolish", "FrenchVsSpanish", "GeorgianVsBelarusian",
            "GeorgianVsBulgarian", "GeorgianVsCroatian", "GeorgianVsCzech", "GeorgianVsDanish", "GeorgianVsEnglish", "GeorgianVsEstonian", "GeorgianVsFinish", "GeorgianVsFrench", "GeorgianVsGerman",
            "GeorgianVsGreek", "GeorgianVsHungarian", "GeorgianVsIrish", "GeorgianVsItalian", "GeorgianVsPolish", "GeorgianVsSpanish", "GeorgianVsWelsh", "GreekVsBelarusian", "GreekVsBulgarian",
            "GreekVsCzech", "GreekVsDanish", "GreekVsEnglish", "GreekVsFrench", "GreekVsGerman", "GreekVsPolish", "GreekVsSpanish", "GreekVsWelsh", "HungarianVsBelarusian", "HungarianVsBulgarian",
            "HungarianVsCroatian", "HungarianVsCzech", "HungarianVsDanish", "HungarianVsEnglish", "HungarianVsEstonian", "HungarianVsFinish", "HungarianVsFrench", "HungarianVsGerman",
            "HungarianVsGreek", "HungarianVsIrish", "HungarianVsPolish", "HungarianVsSpanish", "HungarianVsWelsh", "IrishVsBelarusian", "IrishVsBulgarian", "IrishVsCzech", "IrishVsDanish",
            "IrishVsEnglish", "IrishVsEstonian", "IrishVsFinish", "IrishVsFrench", "IrishVsGerman", "IrishVsGreek", "IrishVsPolish", "IrishVsSpanish", "IrishVsWelsh", "ItalianVsBelarusian",
            "ItalianVsBulgarian", "ItalianVsCroatian", "ItalianVsCzech", "ItalianVsDanish", "ItalianVsEnglish", "ItalianVsEstonian", "ItalianVsFinish", "ItalianVsFrench", "ItalianVsGerman",
            "ItalianVsGreek", "ItalianVsHungarian", "ItalianVsIrish", "ItalianVsPolish", "ItalianVsSpanish", "ItalianVsWelsh", "LatvianVsBelarusian", "LatvianVsBulgarian", "LatvianVsCroatian",
            "LatvianVsCzech", "LatvianVsDanish", "LatvianVsEnglish", "LatvianVsEstonian", "LatvianVsFinish", "LatvianVsFrench", "LatvianVsGeorgian", "LatvianVsGerman", "LatvianVsGreek",
            "LatvianVsHungarian", "LatvianVsIrish", "LatvianVsItalian", "LatvianVsPolish", "LatvianVsSpanish", "LatvianVsWelsh", "MacedonianVsBelarusian", "MacedonianVsBulgarian",
            "MacedonianVsCroatian", "MacedonianVsCzech", "MacedonianVsDanish", "MacedonianVsEnglish", "MacedonianVsEstonian", "MacedonianVsFinish", "MacedonianVsFrench", "MacedonianVsGeorgian",
            "MacedonianVsGerman", "MacedonianVsGreek", "MacedonianVsHungarian", "MacedonianVsIrish", "MacedonianVsItalian", "MacedonianVsLatvian", "MacedonianVsPolish", "MacedonianVsSpanish",
            "MacedonianVsWelsh", "NorwegianVsBelarusian", "NorwegianVsBulgarian", "NorwegianVsCroatian", "NorwegianVsCzech", "NorwegianVsDanish", "NorwegianVsEnglish", "NorwegianVsEstonian",
            "NorwegianVsFinish", "NorwegianVsFrench", "NorwegianVsGeorgian", "NorwegianVsGerman", "NorwegianVsGreek", "NorwegianVsHungarian", "NorwegianVsIrish", "NorwegianVsItalian",
            "NorwegianVsLatvian", "NorwegianVsMacedonian", "NorwegianVsPolish", "NorwegianVsSpanish", "NorwegianVsWelsh", "PolishVsGerman", "PolishVsSpanish", "PortugueseVsBelarusian",
            "PortugueseVsBulgarian", "PortugueseVsCroatian", "PortugueseVsCzech", "PortugueseVsDanish", "PortugueseVsEnglish", "PortugueseVsEstonian", "PortugueseVsFinish", "PortugueseVsFrench",
            "PortugueseVsGeorgian", "PortugueseVsGerman", "PortugueseVsGreek", "PortugueseVsHungarian", "PortugueseVsIrish", "PortugueseVsItalian", "PortugueseVsLatvian", "PortugueseVsMacedonian",
            "PortugueseVsNorwegian", "PortugueseVsPolish", "PortugueseVsSpanish", "PortugueseVsWelsh", "RomanshVsBelarusian", "RomanshVsBulgarian", "RomanshVsCroatian", "RomanshVsCzech",
            "RomanshVsDanish", "RomanshVsEnglish", "RomanshVsEstonian", "RomanshVsFinish", "RomanshVsFrench", "RomanshVsGeorgian", "RomanshVsGerman", "RomanshVsGreek", "RomanshVsHungarian",
            "RomanshVsIrish", "RomanshVsItalian", "RomanshVsLatvian", "RomanshVsMacedonian", "RomanshVsNorwegian", "RomanshVsPolish", "RomanshVsPortuguese", "RomanshVsSpanish", "RomanshVsWelsh",
            "SerbianVsBelarusian", "SerbianVsBulgarian", "SerbianVsCroatian", "SerbianVsCzech", "SerbianVsDanish", "SerbianVsEnglish", "SerbianVsEstonian", "SerbianVsFinish", "SerbianVsFrench",
            "SerbianVsGeorgian", "SerbianVsGerman", "SerbianVsGreek", "SerbianVsHungarian", "SerbianVsIrish", "SerbianVsItalian", "SerbianVsLatvian", "SerbianVsMacedonian", "SerbianVsNorwegian",
            "SerbianVsPolish", "SerbianVsPortuguese", "SerbianVsRomansh", "SerbianVsSlovak", "SerbianVsSpanish", "SerbianVsWelsh", "SlovakVsBelarusian", "SlovakVsBulgarian", "SlovakVsCroatian",
            "SlovakVsCzech", "SlovakVsDanish", "SlovakVsEnglish", "SlovakVsEstonian", "SlovakVsFinish", "SlovakVsFrench", "SlovakVsGeorgian", "SlovakVsGerman", "SlovakVsGreek", "SlovakVsHungarian",
            "SlovakVsIrish", "SlovakVsItalian", "SlovakVsLatvian", "SlovakVsMacedonian", "SlovakVsNorwegian", "SlovakVsPolish", "SlovakVsPortuguese", "SlovakVsRomansh", "SlovakVsSpanish",
            "SlovakVsWelsh", "SpanishVsGerman", "WelshVsBelarusian", "WelshVsBulgarian", "WelshVsCzech", "WelshVsEnglish", "WelshVsFrench", "WelshVsGerman", "WelshVsPolish", "WelshVsSpanish"]
# %%
all_languages = ['English', 'Belarusian', 'French', 'German', 'Polish', 'Spanish', 'Bulgarian', 'Croatian', 'Czech', 'Danish', 'Estonian', 'Finish', 'Greek', 'Irish', 'Welsh', 'Georgian', 'Hungarian',
                 'Italian', 'Latin', 'Macedonian', 'Norwegian', 'Portuguese', 'Romansh', 'Serbian', 'Slovak']
