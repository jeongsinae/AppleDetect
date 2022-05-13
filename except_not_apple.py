bad_words = ['apple']

with open('all_output.txt') as oldfile, open('C:/Users/aaa/Desktop/9th Apple/d/not_apple_gt.txt', 'a') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
