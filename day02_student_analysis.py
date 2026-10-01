import pandas as pd

#Create the DataFrame
students = [
    ["Aarav", 85, 90, 78],
    ["Diya", 92, 88, 95],
    ["Rohan", 65, 72, 68],
    ["Meera", 78, 81, 85],
    ["Kabir", 55, 60, 58]
]

df = pd.DataFrame(
    students,
    columns=["Name", "Python", "SQL", "AI"]
)

#Caluclating average and add as new column
df["Average"]=(df[["Python","SQL","AI"]]).mean(axis=1).round(2) #axis=1 create rowwise average, axis=0 create column average
print(df)

#Find the top-performing student
top_index =df["Average"].idxmax()
print("Top student:",df["Name"][top_index])
print("Average:",df["Average"][top_index])

#Print the entire record details of top student
print(df.loc[df["Average"].idxmax()])

#Identify students who need attention

print(df[df["Average"]<70]["Name"])


#Filter Rows
print(df[df["Average"] < 70])

#Filter rows + select a column:
print(df.loc[df["Average"] < 70, "Name"])

#Print the names of students whose AI score is greater than 80.
print(df.loc[df["AI"] > 80, "Name"])
print(df.loc[df["AI"] > 80, "Name"].tolist())

#Find the student with the highest AI score and print their name and AI score.
print("Top AI student:",df.loc[df["AI"].idxmax(),"Name"],"\nAI Score:",df.loc[df["AI"].idxmax(),"AI"])