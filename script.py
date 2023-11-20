import requests


def download_and_save_word_list(fetched_url, fetched_file):
    # Send a GET request to the URL
    response = requests.get(fetched_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file
        with open(fetched_file, 'w') as file:
            file.write(response.text)
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")


# URL of the file containing the 10,000 most common English words
url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"

# Name of the file to save the words
file_name = "10000_common_words.txt"

# Download and save the word list
download_and_save_word_list(url, file_name)
