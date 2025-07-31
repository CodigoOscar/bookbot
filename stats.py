def get_word_count(text):
  word_list = text.split()
  return len(word_list)

def get_letter_count(text):
  char_count = {}
  for char in text:
    c = char.lower()
    if c in char_count:
      char_count[c] += 1
    else:
      char_count[c] = 1
  return char_count

def get_letter_dict(characters):
    new_char_list = []
    for key, value in characters.items():
        new_char_list.append({"name":key, "count":value})
    new_char_list.sort(reverse=True, key=sort_on)
    return new_char_list

def sort_on(items):
    return items["count"]
