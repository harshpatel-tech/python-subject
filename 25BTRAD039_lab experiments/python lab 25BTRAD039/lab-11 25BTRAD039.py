# Lab Exercise 11: Log File Reader Program
filename = "application.log"
try:
    with open(filename, "r") as file:
        logs = file.readlines()
    if len(logs) == 0:
        print("The log file is empty.")
    else:
        error = 0
        warning = 0
        info = 0
        error_lines = []
        for line in logs:
            if "ERROR" in line:
                error += 1
                error_lines.append(line.strip())
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1
        print("Log Summary")
        print("-" * 20)
        print("Errors:", error)
        print("Warnings:", warning)
        print("Info :", info)
        print("Total lines read:", len(logs))
        if error > 0:
            print("\nError messages found:")
            for line in error_lines:
                print(" ", line)
except FileNotFoundError:
    print("Log file not found.")
