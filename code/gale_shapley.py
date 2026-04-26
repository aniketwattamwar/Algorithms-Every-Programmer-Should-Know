def gale_shapley(students_prefs, universities_prefs):
    free_students = list(students_prefs.keys())
    matches = {}
    proposal_index = {student: 0 for student in students_prefs}

    while free_students:
        student = free_students[0]
        preferences = students_prefs[student]
        if proposal_index[student] >= len(preferences):
            free_students.pop(0)
            continue

        uni = preferences[proposal_index[student]]
        proposal_index[student] += 1

        if uni not in matches:
            matches[uni] = student
            free_students.pop(0)
        else:
            current_student = matches[uni]
            uni_preferences = universities_prefs[uni]
            if uni_preferences.index(student) < uni_preferences.index(current_student):
                matches[uni] = student
                free_students.pop(0)
                free_students.append(current_student)
            else:
                # University prefers current assignment, student stays free
                pass

    return matches


def print_matching(title, students_prefs, universities_prefs):
    print(f"--- {title} ---")
    matches = gale_shapley(students_prefs, universities_prefs)
    for uni, student in matches.items():
        print(f"{uni} is matched with {student}")
    print()


if __name__ == "__main__":
    students = {
        'Alice': ['Y', 'X', 'Z'],
        'Bob': ['X', 'Y', 'Z'],
        'Carol': ['X', 'Y', 'Z'],
    }
    universities = {
        'X': ['Alice', 'Bob', 'Carol'],
        'Y': ['Bob', 'Alice', 'Carol'],
        'Z': ['Carol', 'Alice', 'Bob'],
    }
    print_matching("Test 1: Original Gale-Shapley example", students, universities)
