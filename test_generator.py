def generate_test_scenarios(requirement):
    scenarios = {
        "Positive Tests": [
            f"Verify the user can successfully complete: {requirement}",
            "Verify the expected result is displayed after successful completion."
        ],
        "Negative Tests": [
            "Verify the system handles invalid input correctly.",
            "Verify the system displays a clear error message when the action fails."
        ],
        "Edge Cases": [
            "Verify behavior with empty or missing input.",
            "Verify behavior with maximum allowed input values.",
            "Verify repeated user actions do not cause unexpected behavior."
        ],
        "Usability Checks": [
            "Verify instructions and messages are clear to the user.",
            "Verify the user can understand what to do after an error occurs."
        ]
    }

    return scenarios


requirement = input("Enter a product requirement: ")

results = generate_test_scenarios(requirement)

print("\nGenerated QA Test Scenarios:\n")

for category, tests in results.items():
    print(category)
    for test in tests:
        print(f"- {test}")
    print()
