"""Remake Bible books into json"""
import json
import io


def htm_to_json(file_path: str, json_name: str, book_name: str):
    """Function to converts Bible htm from VisioBible to json"""
    # Get text of book and clear all unnecessary tags
    file = open(file_path, mode='rt', encoding='utf-8')
    book_text = file.read()
    book_text = book_text.replace('<p>', '')
    book_text = book_text.replace('<h4>', '')
    book_text = book_text.replace('</h4>', '')
    file.close()
    file = io.StringIO(book_text)   # Reload text as file

    book_json = {'name': book_name,  # Set format for book's json
                 'chapters': []
                 }

    while True:     # Iterate all verses
        verse = file.readline().strip()
        if verse == '':  # If no text than break loop
            break

        if verse.lower().startswith(book_name.lower()):  # If it's chapter
            book_json['chapters'].append([])    # then continue and add new
            continue                            # list for new chapter
        book_json['chapters'][-1].append(verse[verse.find(' ') + 1:])

    json_file = open(json_name, mode='wt', encoding='utf-8')  # Write book
    json.dump(book_json, json_file)                           # to json
    json_file.flush()
