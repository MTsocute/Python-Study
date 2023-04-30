def count_word(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")



if __name__ == '__main__':
    filepath = "/Users/momo/Desktop/Python/Chapter10/data/"
    file_list = ['alice.txt', 'guest_reason.txt']
    for file in file_list:
        file = filepath + file
        count_word(file)