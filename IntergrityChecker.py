import requests
import hashlib

# Download a file from a URL
def download_file(url, file_name):
    response = requests.get(url)

    file = open(file_name, "wb")
    file.write(response.content)
    file.close()


# Calculate SHA-256 hash of a file
def calculate_hash(file_name):
    sha256 = hashlib.sha256()

    file = open(file_name, "rb")
    data = file.read()
    file.close()

    sha256.update(data)
    return sha256.hexdigest()


# Compare hashes
def check_integrity(calculated_hash, expected_hash):
    if calculated_hash == expected_hash:
        return True
    else:
        return False


# ---------- Main Program ----------
print("=== File Integrity Checker ===")

url = input("Enter file download URL: ")
expected_hash = input("Enter expected SHA-256 hash: ")
file_name = "downloaded_file"

print("\nDownloading file...")
download_file(url, file_name)

print("Calculating hash...")
calculated_hash = calculate_hash(file_name)

print("Calculated Hash:", calculated_hash)

if check_integrity(calculated_hash, expected_hash):
    print("File is safe and not changed")
else:
    print("File has been changed or corrupted")
