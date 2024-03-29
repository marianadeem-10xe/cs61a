"""Typing test implementation"""

from doctest import OutputChecker
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    select_from = [p for p in paragraphs if select(p)]
    return select_from[k] if k<len(select_from) else ""        

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def search_words_in(sentence):
        words = remove_punctuation(lower(sentence)).split()    
        return bool(sum([1 for w in topic if w in words]))             
    return search_words_in
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
 
    if len(typed_words)==0:
        if len(reference_words)==0:        
            return float(100)
        else:
            return float(0)
    else:
        if len(reference_words) > len(typed_words):
            loop_over = len(typed_words)
        else: 
            loop_over = len(reference_words)   
    
        correct_words = sum([1 for i in range(loop_over) if typed_words[i] == reference_words[i]])        
        return correct_words/len(typed_words)*100        
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    total_words, min_taken = len(typed)/5, elapsed/60 
    return total_words/min_taken
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        valid_words: a list of strings representing valid words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    diff = [diff_function(typed_word, w, limit) for w in valid_words]
    return typed_word if min(diff) > limit else valid_words[diff.index(min(diff))]    
    # END PROBLEM 5

def feline_flips(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_flips("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_flips("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_flips("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_flips("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_flips("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    len_diff = abs(len(start)-len(goal))
    # Base case
    if not start or not goal:
        return len_diff
            
    # Recursive case    
    else:
        if start[0]==goal[0]:
            total = feline_flips(start[1:], goal[1:], limit)
            return total if total<=limit else limit+1 
        else: 
            total = 1 + feline_flips(start[1:], goal[1:], limit)
            return total if total<=limit else limit+1   
    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    """len_diff   = abs(len(start)-len(goal))
    add        = lambda l , str : l+str
    remove     = lambda str : str[1:]
    substitute = lambda l, str : l+str[1:]
    def count_changes(start, goal, limit):    
        # Base case
        if not start or not goal:
            return len_diff
        else:
            count = [0, 0, 0]
            added_str, rem_str, sub_str = start[:], start[:], start[:]
            
            while added_str or rem_str or sub_str:
                
                if added_str[0]!=goal[0]:
                    added_str = add(goal[0], start)
                    count[0]+=1
                if rem_str[0] not in goal:
                    rem_str   = remove(start)
                    count[1]+=1
                if  sub_str[0] not in goal and len(start)==len(goal):
                    sub_str   = substitute(goal[0], start)
                    count[2]+=1"""        
                 
    """if not start or not goal:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return abs(len(start)-len(goal))
        # END

    elif start==goal:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    else:
        add        = lambda start, goal : goal[0]+start if goal[0] not in start else start
        remove     = lambda start, goal : start[1:] if start[0] not in goal else start
        substitute = lambda start, goal : goal[0]+start[1:] if len(start)==len(goal) else start

        # BEGIN
        "*** YOUR CODE HERE ***"
        if start[0]!=goal[0]:
            if goal[0] not in start:
                total = 1 + minimum_mewtations(add(start, goal), goal, limit-1)
            total = 1 + minimum_mewtations(remove(start, goal), goal, limit-1)
            total = 1 + minimum_mewtations(substitute(start, goal), goal, limit-1)
        
        return total if total<=limit else limit+1
        # END"""
    
    
    # Recursive case
    """else:
        if start[0]== goal[0]:
            total = minimum_mewtations(start[1:], goal[1:], limit)
        
        else:
            if start[0] in goal:    # Check if the letter needs to be removed or kept
                if start.count(start[0]) > goal.count(start[0]):
                    start = start[1:]       # remove letter
                    total = 1 + minimum_mewtations(start, goal, limit)

                else:
                    start = goal[0] + start
                    total = 1 + minimum_mewtations(start[1:], goal[1:], limit)

            elif start[0] not in goal and len_diff:
                start = start[1:]       # remove letter
                total = 1 + minimum_mewtations(start, goal, limit)
            
            else:
                if start[1] == goal[0]:                   
                    start = start[1:]       # remove letter
                    total = 1 + minimum_mewtations(start, goal, limit)

                else:
                    start = goal[0] + start[1:]         # remove then add letter = substitute letter, count as one change
                    total = 1 + minimum_mewtations(start[1:], goal[1:], limit)
        print(total)
        return total if total <= limit else limit+1"""
        # END
print("changes",minimum_mewtations("rlogcul", "logical", 10))


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(sofar, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        send: a function used to send progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    progress = 0
    for i in range(len(sofar)):
        if sofar[i]==prompt[i]:
            progress+=1
        else: break    
    prog_dict = {"id": user_id, "progress": progress/len(prompt)}
    send(prog_dict) 
    return prog_dict["progress"]      
        
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(p, ['collar', 'plush', 'blush', 'repute'])
    >>> get_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for player_t in times_per_player:
        p_time = []
        for t_idx in range(len(player_t)-1):
            p_time.append(player_t[t_idx+1]-player_t[t_idx])
        times.append(p_time)
    return game(words, times)        
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    """
    player_indices = range(len(get_times(game)))  # contains an *index* for each player
    word_indices = range(len(get_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    
    words, times = get_words(game), get_times(game)
    output = [[] for p in player_indices]  
    for w_idx in word_indices:
        fastest_p, fastest_time = 0,float("inf")
        for p in player_indices:
            time_p = time(game, p, w_idx)
            if time_p<fastest_time:
                fastest_p = p
                fastest_time = time_p
        output[fastest_p].append(word_at(game, w_idx))

    return output        
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def get_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def get_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
