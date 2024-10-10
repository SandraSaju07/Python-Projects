def create_acronym(phrase):
    """
    This function takes a phrase and returns its acronym, ignoring common words.
    :param phrase: The input phrase from the user.
    :return: The acronym as a string.
    """
    common_words = {'of','and','the','in','on','for'}
    words = phrase.split()

    # Create acronym by ignoring common words
    acronym = ''.join([word[0].upper() for word in words if word.lower not in common_words])

    return acronym

if __name__ == '__main__':
    user_input = input("Enter a Phrase: ")

    # Handle empty input
    if user_input.strip():
        acronym = create_acronym(user_input)
        print(f'The acronym is: {acronym}')
    else:
        print('Please enter a valid phrase.')