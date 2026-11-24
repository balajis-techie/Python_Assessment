import math


def get_grade(mark: float) -> str:
    if not math.isfinite(mark) or not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def add_student(students: list[tuple[str, float]]) -> None:
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be blank.")
        return

    while True:
        entered_mark = input(f"Mark for {name} (0-100): ").strip()
        try:
            mark = float(entered_mark)
            get_grade(mark)
        except ValueError:
            print("Enter a number from 0 to 100.")
            continue

        students.append((name, mark))
        print(f"Added {name}.")
        return


def format_mark(mark: float) -> str:
    return str(int(mark)) if mark.is_integer() else str(mark)


def show_results(students: list[tuple[str, float]]) -> None:
    if not students:
        print("No students have been added yet.")
        return

    name_width = max(len("Name"), max(len(name) for name, _ in students))
    print(f"{'Name':<{name_width}}  {'Mark':>6}  Grade")
    for name, mark in students:
        print(f"{name:<{name_width}}  {format_mark(mark):>6}  {get_grade(mark)}")

    marks = [mark for _, mark in students]
    average = sum(marks) / len(marks)
    print(
        f"Average: {average:.1f} "
        f"Highest: {format_mark(max(marks))} "
        f"Lowest: {format_mark(min(marks))}"
    )


def main() -> None:
    # A list preserves entry order and allows different students to share a name.
    students: list[tuple[str, float]] = []

    try:
        while True:
            print("\nStudent Grade Manager")
            print("1. Add student")
            print("2. Show results")
            print("3. Quit")
            choice = input("Choose an option (1-3): ").strip()

            if choice == "1":
                add_student(students)
            elif choice == "2":
                show_results(students)
            elif choice == "3":
                print("Goodbye.")
                return
            else:
                print("Invalid choice. Enter 1, 2, or 3.")
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended. Goodbye.")


if __name__ == "__main__":
    main()
