import os
from collections import Counter
import socket
import re

data_dir = '/home/data'

text_files = os.listdir(data_dir)

# Function to count total number of words in a text file
def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return len(words)

# Read and count words in IF.txt
if_path = os.path.join(data_dir, 'IF.txt')
if_word_count = count_words(if_path) if os.path.exists(if_path) else 0

# Read and count words in Limerick-1.txt
limerick_path = os.path.join(data_dir, 'Limerick-1.txt')
limerick_word_count = count_words(limerick_path) if os.path.exists(limerick_path) else 0

# Calculate grand total number of words
grand_total = if_word_count + limerick_word_count

# Find top 3 words with maximum counts in IF.txt
if_word_counts = Counter()
# with open(if_path, "r") as file:
#     text = file.read().lower().replace(",", "")  # Replace commas 
#     if_word_counts.update(text.split())
# if_word_counts.update(open(if_path).read().lower().split())

characters_to_replace = ",;:.!?"

# Create translation table to replace characters with blank space
translation_table = str.maketrans(characters_to_replace, " " * len(characters_to_replace))

# Read the file, replace characters with blank space, update the counter with lowercase words
with open(if_path, "r") as file:
    text = file.read().lower().translate(translation_table)  # Replace characters with blank space
    if_word_counts.update(text.split())
top_words = if_word_counts.most_common(3)

# Find IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())

# Write output to result.txt
output_path = '/home/output/result.txt'
with open(output_path, 'w') as output_file:
    output_file.write("List of text files:\n")
    for file in text_files:
        output_file.write(file + '\n')
    output_file.write(f"\nTotal number of words in IF.txt: {if_word_count}\n")
    output_file.write(f"Total number of words in Limerick-1.txt: {limerick_word_count}\n")
    output_file.write(f"Grand total number of words: {grand_total}\n")
    output_file.write("\nTop 3 words with maximum counts in IF.txt:\n")
    for word, count in top_words:
        output_file.write(f"{word}: {count}\n")
    output_file.write(f"\nIP address of the machine: {ip_address}\n")

# Print output to console
with open(output_path, 'r') as output_file:
    print(output_file.read())
