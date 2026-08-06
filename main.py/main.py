print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)
print()

# ---------------- Student Name Validation ----------------
while True:
    student_name = input("Enter student name: ")

    if student_name.strip() != "":
        break

    print("Student name cannot be empty.")
    print()

# ---------------- Registration Number ----------------
registration_number = input("Enter registration number: ")

# ---------------- Graduation Year ----------------
graduation_year = int(input("Enter graduation year: "))

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

# ---------------- Attendance Validation ----------------
while True:
    attendance = float(input("Enter attendance percentage: "))

    if attendance >= 0 and attendance <= 100:
        print("Attendance accepted.")
        break

    print("Invalid attendance. Enter a value between 0 and 100.")
    print()

# ---------------- Project-Completion Input ----------------
while True:
    project_input = input(
        "Has the student completed the required project?\n"
        "Enter yes or no: "
    )

    if project_input == "yes" or project_input == "no":
        break

    print("Invalid input. Enter only yes or no.")
    print()

if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# ---------------- Profile-Verification Input ----------------
while True:
    profile_input = input(
        "Is the student profile verified?\n"
        "Enter yes or no: "
    )

    if profile_input == "yes" or profile_input == "no":
        break

    print("Invalid input. Enter only yes or no.")
    print()

if profile_input == "yes":
    profile_verified = True
else:
    profile_verified = False

# ---------------- Initialize Counters and Accumulators ----------------
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

print()
print("PRACTICE SCORES")
print("-" * 50)

# ---------------- Process Seven Practice Days ----------------
for day in range(1, 8):

    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "
            )
        )

        if score == -1 or (score >= 0 and score <= 100):
            break

        print("Invalid score. Enter -1 or a value between 0 and 100.")

    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        print()
        continue

    attempted_days += 1
    total_score += score

    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

    if score >= 75 and score <= 100:
        strong_days += 1
        print(f"Day {day} Result: Strong")
    elif score >= 60 and score <= 74:
        satisfactory_days += 1
        print(f"Day {day} Result: Satisfactory")
    elif score >= 40 and score <= 59:
        improvement_days += 1
        print(f"Day {day} Result: Needs Improvement")
    else:
        critical_days += 1
        print(f"Day {day} Result: Critical")

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    print()

# ---------------- Average Calculation ----------------
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

# ---------------- Placement-Readiness Boolean Expressions ----------------
attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)

# ---------------- Final Status Priority ----------------
if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No coding practice was attempted"
    next_action = "Attempt the required coding practices"
elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = f"Critical score found on Day {first_critical_day}"
    next_action = "Revise the concepts from the first critical day"
elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practice days attempted"
    next_action = "Complete at least six practice days"
elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four practice days passed"
    next_action = "Pass at least four coding practices"
elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score is below 70"
    next_action = "Improve the average score to at least 70"
elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance is below 75 percent"
    next_action = "Improve attendance to at least 75 percent"
elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year is not eligible"
    next_action = "Check the eligible graduation-year requirement"
elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Required project is incomplete"
    next_action = "Complete the required project"
elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Student profile is not verified"
    next_action = "Complete profile verification"
else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"

# ---------------- Final Report ----------------
print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)
print()

print("STUDENT PROFILE")
print()
print(f"Student Name             : {student_name}")
print(f"Registration Number      : {registration_number}")
print(f"Graduation Year          : {graduation_year}")
print(f"Attendance               : {attendance}")

if project_completed:
    print("Project Completed        : Yes")
else:
    print("Project Completed        : No")

if profile_verified:
    print("Profile Verified         : Yes")
else:
    print("Profile Verified         : No")

print()
print("PRACTICE SUMMARY")
print()
print("Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")
print()
print(f"Strong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")

print()
print("PERFORMANCE ANALYSIS")
print()
print(f"Total Score              : {total_score}")
print(f"Average Score            : {round(average_score, 2)}")

if first_attempt_found:
    print(f"Highest Score            : {highest_score}")
    print(f"Highest Score Day        : Day {highest_score_day}")
    print(f"Lowest Score             : {lowest_score}")
    print(f"Lowest Score Day         : Day {lowest_score_day}")
else:
    print("Highest Score            : Not Available")
    print("Highest Score Day        : Not Available")
    print("Lowest Score             : Not Available")
    print("Lowest Score Day         : Not Available")

print()
print("CRITICAL SCORE INFORMATION")
print()

if critical_score_found:
    print("Critical Score Found     : Yes")
    print(f"First Critical Day       : Day {first_critical_day}")
    print(f"First Critical Score     : {first_critical_score}")
else:
    print("Critical Score Found     : No")
    print("First Critical Day       : Not Applicable")
    print("First Critical Score     : Not Applicable")

print()
print("FINAL DECISION")
print()
print(f"Final Status             : {final_status}")
print(f"Primary Blocker          : {primary_blocker}")
print(f"Next Action              : {next_action}")
print()
print("=" * 50)