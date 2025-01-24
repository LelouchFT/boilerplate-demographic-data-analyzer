import pandas as pd


def calculate_demographic_data(print_data=True):
    # Lire les données depuis un fichier
    df = pd.read_csv('adult.data.csv')

    # Combien de personnes de chaque race sont représentées dans ce dataset ? 
    # Cela devrait être une série Pandas avec les noms des races comme index.
    race_count = df['race'].value_counts()

    # Quelle est l'âge moyen des hommes ?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)

    # Quel est le pourcentage de personnes ayant un diplôme de licence (Bachelor's) ?
    percentage_bachelors = round(df['education'].value_counts(normalize = True).get("Bachelors")*100 , 1)

    # Quel pourcentage de personnes ayant un niveau d'éducation avancé 
    # (Licence, Master ou Doctorat) gagnent plus de 50K ? 
    # Quel pourcentage de personnes sans niveau d'éducation avancé gagnent plus de 50K ?

    # Avec et sans Licence, Master ou Doctorat
    higher_education = df[df['education'].isin(["Bachelors" ,"Masters" ,"Doctorate"])]
    lower_education = df[~df['education']. isin(["Bachelors" ,"Masters" ,"Doctorate"])]
    

    # Pourcentage des personnes ayant un salaire >50K
    higher_education_rich=round( higher_education['salary'].value_counts(normalize = True).get('>50K')*100,1)
    lower_education_rich =round( lower_education['salary'].value_counts(normalize = True).get('>50K')*100, 1)

    # Quel est le nombre minimal d'heures qu'une personne travaille par semaine 
    # (caractéristique `hours-per-week`) ?
    min_work_hours = df["hours-per-week"].min()

    # Quel pourcentage des personnes qui travaillent le nombre minimal d'heures 
    # par semaine ont un salaire >50K ?
    num_min_workers = df[df["hours-per-week"] == min_work_hours ]

    rich_percentage = round(num_min_workers["salary"].value_counts(normalize = True).get(">50K"), 1)*100

    # Quel pays a le pourcentage le plus élevé de personnes gagnant >50K ?
    highest_earning_country = (df[df['salary'] == ">50K"]['native-country'].value_counts()/df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage =round((df[ df['salary'] ==">50K"]['native-country'].value_counts()*100/df["native-country"].value_counts()).max(),1)
    # Quelle est la profession la plus populaire parmi ceux qui gagnent >50K en Inde ?
    top_IN_occupation = df[(df['native-country'] == "India") & (df['salary'] == ">50K")]['occupation'].value_counts().idxmax()

    # NE PAS MODIFIER LE CODE CI-DESSOUS

    if print_data:
        print("Nombre de chaque race :\n", race_count) 
        print("Âge moyen des hommes :", average_age_men)
        print(f"Pourcentage avec un diplôme de Licence : {percentage_bachelors}%")
        print(f"Pourcentage des personnes avec une éducation avancée gagnant >50K : {higher_education_rich}%")
        print(f"Pourcentage des personnes sans éducation avancée gagnant >50K : {lower_education_rich}%")
        print(f"Temps de travail minimal : {min_work_hours} heures/semaine")
        print(f"Pourcentage des riches parmi ceux qui travaillent le moins : {rich_percentage}%")
        print("Pays avec le pourcentage le plus élevé de riches :", highest_earning_country)
        print(f"Pourcentage le plus élevé de riches dans un pays : {highest_earning_country_percentage}%")
        print("Professions les plus populaires en Inde :", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()