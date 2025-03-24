import requests

# Define book_id
book_id = 12345  # Replace with the actual book ID

content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
metadata_url = f"https://www.gutenberg.org/ebooks/{book_id}"

# Get book content
content_response = requests.get(content_url)
content = content_response.text

# Get metadata
metadata_response = requests.get(metadata_url)

print(content)