import json

# Explore the structure of this data.
filename ='Python_learning_chapter_2/downloading_data/data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'Python_learning_chapter_2/downloading_data/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)