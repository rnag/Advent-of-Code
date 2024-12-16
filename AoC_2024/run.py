import sys
from importlib import import_module

def main():
    # Get the day number from the command line arguments
    day_number = sys.argv[1].zfill(2)  # e.g., '14'
    input_file = sys.argv[2] if len(sys.argv) > 2 else None  # Optional input file

    # Try to import the corresponding day module dynamically
    try:
        # Dynamically import the day script (e.g., AoC_2024.Days.day_14)
        day_module = import_module(f"AoC_2024.Days.{day_number}")
        # Call the solution function if it exists in the module
        if hasattr(day_module, "solve"):
            day_module.solve(input_file)
        else:
            print(f"No 'solve' function found in {day_number}.py.")
    except ModuleNotFoundError:
        print(f"Day {day_number} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
