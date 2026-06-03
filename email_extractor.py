import re

# Read text file
with open("sample.txt", "r") as file:
    content = file.read()

# Find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save emails to a new file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("\nExtracted Emails:")

for email in emails:
    print(email)