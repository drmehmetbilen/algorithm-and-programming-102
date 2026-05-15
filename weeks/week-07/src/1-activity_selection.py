def select_activities(activities):
    """
    Return a maximum-size compatible set of activities
    by choosing the earliest finishing compatible activity.
    """
    ordered = sorted(activities, key=lambda activity: activity[2])
    selected = []
    last_finish = None

    for name, start, finish in ordered:
        if last_finish is None or start >= last_finish:
            selected.append((name, start, finish))
            last_finish = finish

    return selected


if __name__ == "__main__":
    sample = [
        ("A", 1, 4),
        ("B", 3, 5),
        ("C", 0, 6),
        ("D", 5, 7),
        ("E", 8, 9),
        ("F", 5, 9),
    ]

    print("Activities:")
    for activity in sample:
        print(activity)

    print("\nSelected schedule:")
    for activity in select_activities(sample):
        print(activity)
