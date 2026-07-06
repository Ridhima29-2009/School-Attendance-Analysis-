import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": [
        "Aman", "Riya", "Rahul", "Sneha",
        "Aman", "Pooja", None, "Arjun"
    ],
    "Class": [
        "10A", "10B", "10A", "10C",
        "10A", "10B", "10C", "10A"
    ],
    "Attendance (%)": [
        95, 88, None, 91,
        95, 85, 78, 90
    ],
    "Maths Marks": [
        92, 81, 76, None,
        92, 85, 70, 88
    ],
    "Status": [
        "Present", "Present", "Absent", "Present",
        "Present", "Absent", "Present", "Present"
    ]
}

df = pd.DataFrame(data)

print("School Attendance Analysis")
print(df)

print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nInfo")
df.info()

print("\nDescribe")
print(df.describe())

Highest_Attendance = df["Attendance (%)"].max()
print("\nHighest Attendance:", Highest_Attendance)

Lowest_Attendance = df["Attendance (%)"].min()
print("\nLowest Attendance:", Lowest_Attendance)

Student_Highest_Attendance = df.loc[df["Attendance (%)"].idxmax()]
print("\nStudent with Highest Attendance")
print(Student_Highest_Attendance)

Student_Lowest_Attendance = df.loc[df["Attendance (%)"].idxmin()]
print("\nStudent with Lowest Attendance")
print(Student_Lowest_Attendance)

High_Attendance = df[df["Attendance (%)"] > 90]
print("\nStudents with Attendance > 90")
print(High_Attendance)

Class10A = df[df["Class"] == "10A"]
print("\nStudents from Class 10A")
print(Class10A)

Average_Attendance = df.groupby("Class")["Attendance (%)"].mean()
print("\nClass Wise Average Attendance")
print(Average_Attendance)

Average_Maths = df.groupby("Class")["Maths Marks"].mean()
print("\nClass Wise Average Maths Marks")
print(Average_Maths)

Total_Students = df["Class"].value_counts()
print("\nStudents in Each Class")
print(Total_Students)

print("\nMissing Values")
print(df.isnull())

print("\nNon-Missing Values")
print(df.notnull())

df["Attendance (%)"] = df["Attendance (%)"].fillna(80)

df["Maths Marks"] = df["Maths Marks"].fillna(
    df["Maths Marks"].mean()
)

df["Student"] = df["Student"].fillna("Unknown")

print("\nData After Filling Missing Values")
print(df)

print("\nDuplicate Rows")
print(df.duplicated())

df = df.drop_duplicates()

df = df.drop("Status", axis=1)

df["Final Attendance"] = df["Attendance (%)"].apply(
    lambda x: x + 2
)

print("\nStudents with Attendance >90 and Maths Marks >80")
print(
    df.query(
        "`Attendance (%)` > 90 and `Maths Marks` > 80"
    )
)

df["Percentage Contribution"] = (
    df["Final Attendance"] /
    df["Final Attendance"].sum()
) * 100

print("\nPercentage Contribution")
print(df[["Student", "Percentage Contribution"]])

df = df.sort_values(
    "Attendance (%)",
    ascending=False
)

print("\nSorted Data")
print(df)

plt.bar(df["Student"], df["Attendance (%)"])
plt.title("Student VS Attendance")
plt.xlabel("Student")
plt.ylabel("Attendance (%)")
plt.show()

Average_Attendance = df.groupby("Class")["Attendance (%)"].mean()

plt.bar(
    Average_Attendance.index,
    Average_Attendance.values
)
plt.title("Class VS Average Attendance")
plt.xlabel("Class")
plt.ylabel("Average Attendance")
plt.show()