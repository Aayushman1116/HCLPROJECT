# STUDENT SOCIAL MEDIA AND MENTAL HEALTH
# Beginner-level answers for the 20 questions in the question PDF
#
# Libraries used: pandas, numpy and matplotlib
# Install them once using:
# pip install pandas numpy matplotlib
#
# Keep this Python file and the CSV file in the same folder.
# Then run this file and enter a question number from 1 to 20.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. READ THE CSV FILE
# ---------------------------------------------------------

data = pd.read_csv("student_social_media_mental_health_50.csv")
print(
"===================================================================================================================")
print("1. What are the readings of student Aarav Sharma? Display all the details of Aarav.")
print("2. Find the names and ages of all students whose country is India.")
print("3. What is the most used social media platform of Ananya Verma?")
print("4. Display the sleep time, anxiety level, depression level, and mental health index of Rohan Gupta.")
print("5. Find all students whose age is greater than 22.")
print("6. Display the names of all students whose anxiety level is High.")
print("7. Find students whose depression level is Moderate or High.")
print("8. Which students have a mental health index greater than 80?")
print("9. Find all students who sleep less than 6 hours per day.")
print("10. Display students who use Instagram for more than 3 hours per day.")
print("11. Calculate the average sleep time of all 50 students.")
print("12. Calculate the average mental health index of students from India.")
print("13. Find the student who has the highest Instagram screen time.")
print("14. Which student has the lowest mental health index?")
print("15. Calculate the total Facebook screen time of all students.")
print("16. Create a bar graph showing the sleep time of each student.")
print("17. Create a scatter plot showing the relationship between sleep time and anxiety level. If needed, encode the anxiety categories numerically and mention your encoding.")
print("18. Create a pie chart showing the distribution of students according to their most used social media platform.")
print("19. Create a bar graph comparing the average mental health index of students from different countries.")
print("20. Create a scatter plot showing the relationship between Instagram screen time and mental health index.")
print("====================================================================================================================")


# Ask the user which question they want to answer.
choice = int(input("\nEnter question number (1 to 20): "))
if choice!=21:

 while choice>=1 and choice<=20:

# ---------------------------------------------------------
# 3. ANSWERS
# ---------------------------------------------------------

  if choice == 1:
    # Question 1: All details of Aarav Sharma
    answer = data[data["Student name"] == "Aarav Sharma"]
    print("\nDetails of Aarav Sharma:")
    print(answer.to_string(index=False))


  elif choice == 2:
    # Question 2: Names and ages of students from India
    answer = data[data["Country"] == "India"]
    print("\nStudents from India:")
    print(answer[["Student name", "Age"]].to_string(index=False))


  elif choice == 3:
    # Question 3: Most used platform of Ananya Verma
    answer = data[data["Student name"] == "Ananya Verma"]
    if len(answer) > 0:
        print("\nMost used platform of Ananya Verma:")
        print(answer["Most used social media platform"].iloc[0])
    else:
        print("Ananya Verma was not found.")


  elif choice == 4:
    # Question 4: Details of Rohan Gupta
    answer = data[data["Student name"] == "Rohan Gupta"]
    columns = [
        "Student name",
        "Sleep time (hours/day)",
        "Anxiety level",
        "Depression level",
        "Mental health index (0-100)"
    ]
    print("\nDetails of Rohan Gupta:")
    print(answer[columns].to_string(index=False))


  elif choice == 5:
    # Question 5: Students older than 22
    answer = data[data["Age"] > 22]
    print("\nStudents whose age is greater than 22:")
    print(answer.to_string(index=False))


  elif choice == 6:
    # Question 6: Students with High anxiety
    answer = data[data["Anxiety level"] == "High"]
    print("\nStudents with High anxiety:")
    print(answer[["Student name", "Anxiety level"]].to_string(index=False))


  elif choice == 7:
    # Question 7: Students with Moderate or High depression
    answer = data[
        (data["Depression level"] == "Moderate") |
        (data["Depression level"] == "High")
    ]
    print("\nStudents with Moderate or High depression:")
    print(answer[["Student name", "Depression level"]].to_string(index=False))


  elif choice == 8:
    # Question 8: Mental health index greater than 80
    answer = data[data["Mental health index (0-100)"] > 80]
    print("\nStudents with mental health index greater than 80:")
    print(answer[["Student name", "Mental health index (0-100)"]].to_string(index=False))


  elif choice == 9:
    # Question 9: Students who sleep less than 6 hours
    answer = data[data["Sleep time (hours/day)"] < 6]
    print("\nStudents who sleep less than 6 hours:")
    print(answer[["Student name", "Sleep time (hours/day)"]].to_string(index=False))


  elif choice == 10:
    # Question 10: Instagram screen time more than 3 hours
    answer = data[data["Instagram screen time (hours/day)"] > 3]
    print("\nStudents using Instagram for more than 3 hours:")
    print(answer[["Student name", "Instagram screen time (hours/day)"]].to_string(index=False))


  elif choice == 11:
    # Question 11: Average sleep time
    sleep = data["Sleep time (hours/day)"]
    average = np.mean(sleep)
    print("\nAverage sleep time:", round(average, 2), "hours per day")


  elif choice == 12:
    # Question 12: Average mental health index of Indian students
    india = data[data["Country"] == "India"]
    average = np.mean(india["Mental health index (0-100)"])
    print("\nAverage mental health index of Indian students:", round(average, 2))


  elif choice == 13:
    # Question 13: Student with highest Instagram screen time
    highest = data["Instagram screen time (hours/day)"].idxmax()
    print("\nStudent with highest Instagram screen time:")
    print(data.loc[highest, ["Student name", "Instagram screen time (hours/day)"]])


  elif choice == 14:
    # Question 14: Student with lowest mental health index
    lowest = data["Mental health index (0-100)"].idxmin()
    print("\nStudent with lowest mental health index:")
    print(data.loc[lowest, ["Student name", "Mental health index (0-100)"]])


  elif choice == 15:
    # Question 15: Total Facebook screen time
    total = np.sum(data["Facebook screen time (hours/day)"])
    print("\nTotal Facebook screen time:", round(total, 2), "hours per day")


  elif choice == 16:
    # Question 16: Bar graph of sleep time
    plt.figure(figsize=(12, 6))
    plt.bar(data["Student name"], data["Sleep time (hours/day)"])
    plt.title("Sleep Time of Each Student")
    plt.xlabel("Student Name")
    plt.ylabel("Sleep Time (hours/day)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


  elif choice == 17:
    # Question 17: Scatter plot of sleep time and anxiety
    # Convert anxiety categories into numbers:
    # Low = 1, Moderate = 2, High = 3

    anxiety_number = data["Anxiety level"].map({
        "Low": 1,
        "Moderate": 2,
        "High": 3
    })

    plt.figure(figsize=(8, 5))
    plt.scatter(data["Sleep time (hours/day)"], anxiety_number)
    plt.title("Sleep Time and Anxiety Level")
    plt.xlabel("Sleep Time (hours/day)")
    plt.ylabel("Anxiety Level")
    plt.yticks([1, 2, 3], ["Low", "Moderate", "High"])
    plt.tight_layout()
    plt.show()

    print("\nAnxiety encoding: Low = 1, Moderate = 2, High = 3")


  elif choice == 18:
    # Question 18: Pie chart of most used social media platforms
    platform_count = data["Most used social media platform"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(
        platform_count,
        labels=platform_count.index,
        autopct="%1.1f%%"
    )
    plt.title("Most Used Social Media Platforms")
    plt.show()


  elif choice == 19:
    # Question 19: Average mental health index by country
    country_average = data.groupby("Country")[
        "Mental health index (0-100)"
    ].mean()

    plt.figure(figsize=(9, 5))
    plt.bar(country_average.index, country_average.values)
    plt.title("Average Mental Health Index by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Mental Health Index")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    print("\nAverage mental health index by country:")
    print(country_average.round(2))


  elif choice == 20:
    # Question 20: Instagram screen time vs mental health index
    plt.figure(figsize=(8, 5))
    plt.scatter(
        data["Instagram screen time (hours/day)"],
        data["Mental health index (0-100)"]
    )
    plt.title("Instagram Screen Time vs Mental Health Index")
    plt.xlabel("Instagram Screen Time (hours/day)")
    plt.ylabel("Mental Health Index")
    plt.tight_layout()
    plt.show()

  else:
    print("Invalid choice. Please enter a valid question number.")
  choice = int(input("\nEnter question number (1 to 20): "))

else:
    print("Thank You")



