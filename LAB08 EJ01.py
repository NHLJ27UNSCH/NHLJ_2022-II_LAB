#acceder al archivo countries_data.py
import countries_data as cd

#Crear una función llamada los 10 idiomas más hablados en el mundo
def idiomas_mas_habladoss():
    print('\n'*5)
    cont_idiomas = {}
    for country in cd.countries:
        for idioma in country["languages"]:
            if idioma in cont_idiomas:
                cont_idiomas[idioma] += 1
            else:
                cont_idiomas[idioma] = 1

    sorted_languages = sorted(cont_idiomas.items(), key=lambda x: x[1], reverse=True)
    top_languages = sorted_languages[:10]

    print("Top 10 idiomas más hablados del mundo:")
    for lang, count in top_languages:
        print(f"{lang}: {count} countries")
idiomas_mas_habladoss()


print('\n'*5)

#Crear una función llamada los países más poblados.
def paises_mas_pobladoss():
    sorted_countries = sorted(cd.countries, key=lambda x: x["population"], reverse=True)
    top_populated_countries = sorted_countries[:10]

    print("Top 10 países más poblados:")
    for country in top_populated_countries:
        print(f"{country['name']}: {country['population']} people")

paises_mas_pobladoss()