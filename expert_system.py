import json

# Load the JSON files
with open(r"D:\CSTT\computer_troubleshooters\phanLoai.json", "r", encoding="utf-8") as pl_file:
    phan_loai_data = json.load(pl_file)

with open(r"D:\CSTT\computer_troubleshooters\trieuChung.json", "r", encoding="utf-8") as tc_file:
    trieu_chung_data = json.load(tc_file)

# Build a mapping from category to symptoms
category_to_symptoms = {}
for pl in phan_loai_data:
    category_id = pl["maPhanLoai"]
    category_name = f"{pl['tenPhanLoaiChinh']} - {pl['tenPhanLoaiCuThe']}"
    category_to_symptoms[category_name] = [
        tc for tc in trieu_chung_data if tc["maPhanLoai"] == category_id
    ]

# Display categories
print("Select categories (separate numbers with commas):")
categories = list(category_to_symptoms.keys())
for idx, cat in enumerate(categories, start=1):
    print(f"{idx}. {cat}")

# User selects multiple categories
category_indices = input("Enter category numbers: ").split(',')
selected_categories = [categories[int(idx.strip()) - 1] for idx in category_indices]

print(f"\nYou selected: {', '.join(selected_categories)}")

# Display symptoms for the selected categories
print("\nRelated Symptoms:")
selected_symptoms = []
for category in selected_categories:
    selected_symptoms.extend(category_to_symptoms[category])

for idx, symptom in enumerate(selected_symptoms, start=1):
    print(f"{idx} - {symptom['tenTrieuChung']}")


