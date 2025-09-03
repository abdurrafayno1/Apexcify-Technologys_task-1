import pandas as pd

# 1) CSV file load karna
df = pd.read_csv("student_marks.csv")

print("Original DataFrame:\n", df)

# 2) Har student ka average nikalna
df["Average"] = df[["Math", "English", "Chemistry"]].mean(axis=1)

print("\nDataFrame with Averages:\n", df)

# 3) Sabse highest average wale student ko find karna
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Student:")
print("Name:", top_student["Name"])
print("Average Score:", top_student["Average"])

