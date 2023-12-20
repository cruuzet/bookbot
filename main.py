def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_letter = get_num_chars(text, True)
  num_words = get_num_words(text)
  print_report(book_path, num_words, num_letter)

def get_book_text(path):
  with open("books/frankenstein.txt") as file:
    return file.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_chars(text, letters_only = False):
  lowercased_text = text.lower()
  chars = {}
  letters = {}

  for char in lowercased_text:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1

  if letters_only == True:
    for key, value in chars.items():
      if key.isalpha():
        letters[key] = value
    return letters

  return chars

def print_report(book, words, chars):
  print(f"--- Report of words and characters used in {book} ---\n")
  print(f"{words} words found in the document \n")
  chars_list = []
  for key, value in chars.items():
    chars_list.append(f"The letter '{key}' was found {value} times")
  chars_list.sort()
  for item in chars_list:
    print(item)  
  print("\n--- End of report ---")
main()
