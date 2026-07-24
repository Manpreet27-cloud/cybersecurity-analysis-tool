def analyze_log(filename):
    try:
        with open(filename, "r") as file:
            failed = 0
            warnings = 0
            errors = 0

            for line in file:
                if "Failed login" in line or "Authentication failure" in line or "Invalid password" in line or "Login failed" in line:
                    failed += 1

                if "WARNING" in line:
                    warnings += 1

                if "ERROR" in line:
                    errors += 1

            print("Security Log Summary")
            print("--------------------")
            print("Failed login attempts:", failed)
            print("Warnings:", warnings)
            print("Errors:", errors)

    except FileNotFoundError:
        print("Error: Log file not found.")


analyze_log("sample_security.log")