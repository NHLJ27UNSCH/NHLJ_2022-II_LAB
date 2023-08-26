# 1. Número total de idiomas
import countries_data as pd
# Número total de idiomas
all_languages = set()
for country in pd.countries:
    for language in country["languages"]:
        all_languages.add(language)

print(f"Número total de idiomas: {len(all_languages)}")

#Diez idiomas más hablados
language_count = {}
for country in pd.countries:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
top_languages = sorted_languages[:10]

print("Top 10 idiomas más hablados del mundo:")
for lang, count in top_languages:
    print(f"{lang}: {count} countries")

#Diez países más poblados
sorted_countries = sorted(pd.countries, key=lambda x: x["population"], reverse=True)
top_populated_countries = sorted_countries[:10]

print("Top 10 países más poblados:")
for country in top_populated_countries:
    print(f"{country['name']}: {country['population']} people")