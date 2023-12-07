import os


STARTER_CODE = """

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    


if __name__ == "__main__":
    main()
"""


def create_starter_code(filepath: str):
    with open(filepath, "w") as f:
        f.write(STARTER_CODE)


def main():
    day_num = int(input("Day number: "))

    if os.path.exists(f"day-{day_num}"):
        print("That directory already exists!")
        return

    directory = f"day-{day_num}"
    os.mkdir(directory)

    # Create files
    open(f"{directory}/input.txt", "w").close()

    starter_code_paths = [
        f"{directory}/part_1.py",
        f"{directory}/part_2.py"
    ]

    # Create starter python files
    for starter_code_path in starter_code_paths:
        create_starter_code(starter_code_path)

    print("Created files successfully!")

    print("Adding files to git...")
    for starter_code_path in starter_code_paths:
        os.system(f"git add {starter_code_path}")
    print("Added files to git!")
    print("Completed!")


if __name__ == "__main__":
    main()
