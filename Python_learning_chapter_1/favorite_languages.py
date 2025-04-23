favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
        print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languags are:")
        for language in languages:
            print(f"\t{language.title()}")