def gale_shapley(students_prefs, universities_prefs):
    """
    Implements the Gale-Shapley stable marriage algorithm.
    
    Finds a stable matching between students and universities where no two
    participants would prefer each other over their current matches.
    
    Args:
        students_prefs (dict): Dictionary where keys are students and values
                              are lists of universities in order of preference.
        universities_prefs (dict): Dictionary where keys are universities and
                                  values are lists of students in order of preference.
    
    Returns:
        dict: Dictionary mapping universities to matched students.
    """
    free_students = list(students_prefs.keys())  # Students who haven't been matched yet
    matches = {}  # Current matches: university -> student
    proposal_index = {student: 0 for student in students_prefs}  # Track proposal attempts

    while free_students:
        student = free_students[0]  # Get next free student
        preferences = students_prefs[student]
        
        # If student has no more universities to propose to, remove from free list
        if proposal_index[student] >= len(preferences):
            free_students.pop(0)
            continue

        uni = preferences[proposal_index[student]]  # Next university to propose to
        proposal_index[student] += 1  # Move to next preference

        if uni not in matches:
            # University is free, accept proposal
            matches[uni] = student
            free_students.pop(0)  # Student is now matched
        else:
            current_student = matches[uni]
            uni_preferences = universities_prefs[uni]
            # Check if university prefers new student over current one
            if uni_preferences.index(student) < uni_preferences.index(current_student):
                matches[uni] = student  # Accept new proposal
                free_students.pop(0)  # New student matched
                free_students.append(current_student)  # Old student becomes free
            else:
                # University prefers current assignment, student stays free
                pass

    return matches


def print_matching(title, students_prefs, universities_prefs):
    """
    Runs the Gale-Shapley algorithm and prints the resulting matches.
    
    Args:
        title (str): Title to display for the test case.
        students_prefs (dict): Student preferences.
        universities_prefs (dict): University preferences.
    """
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
