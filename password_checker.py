from strength_rules import check_strength
from breach_checker import check_pwned
from hash_generator import generate_hashes

def main():
    password = input("Enter a password to analyze: ")

    print("\n[1] Checking password strength...")
    score, feedback = check_strength(password)
    print(f"Score: {score}/6")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")
    else:
        print("Great! Your password is strong.")

    print("\n[2] Checking if password has been leaked...")
    breached, count = check_pwned(password)
    if breached:
        print(f"⚠️ This password has been found {count} times in data breaches!")
    else:
        print("✅ This password has not been found in known breaches.")

    print("\n[3] Hash representations:")
    hashes = generate_hashes(password)
    for algo, hash_val in hashes.items():
        print(f"{algo}: {hash_val}")

if __name__ == "__main__":
    main()
