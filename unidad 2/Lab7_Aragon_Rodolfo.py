student = {
    "name": "",
    "programming": 0,
    "design": 0,
    "networking": 0,
    "data_analysis": 0
}

# Input
student["name"] = input("Enter your name: ")

student["programming"] = int(input("Enter your Programming score (1-10): "))
student["design"] = int(input("Enter your Design score (1-10): "))
student["networking"] = int(input("Enter your Networking score (1-10): "))
student["data_analysis"] = int(input("Enter your Data Analysis score (1-10): "))

# Display dictionary
print("\nCareer Assessment Report")
print("Name:", student["name"])
print("Programming:", student["programming"])
print("Design:", student["design"])
print("Networking:", student["networking"])
print("Data Analysis:", student["data_analysis"])

# Determine career
scores = {
    "programming": student["programming"],
    "design": student["design"],
    "networking": student["networking"],
    "data_analysis": student["data_analysis"]
}

highest = max(scores.values())
top_skills = [skill for skill, score in scores.items() if score == highest]

if len(top_skills) >= 2:
    career = "Multiple Career Paths Identified"
elif top_skills[0] == "programming":
    career = "Software Developer"
elif top_skills[0] == "design":
    career = "UI/UX Designer"
elif top_skills[0] == "networking":
    career = "Network Administrator"
elif top_skills[0] == "data_analysis":
    career = "Data Analyst"

print("Recommended Career:", career)