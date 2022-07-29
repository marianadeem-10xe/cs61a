# Discussion 7 

# Q2.Filter-Iter

from pkg_resources import yield_lines


def filter_iter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***" 
    yield from [i for i in iterable if fn(i)]

    # Q3.Merge
    def merge(a, b):
        """
        >>> def sequence(start, step):
        ...     while True:
        ...         yield start
        ...         start += step
        >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
        >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
        >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
        >>> [next(result) for _ in range(10)]
        [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
        """
        "*** YOUR CODE HERE ***"
        e_in_a = next(a)
        e_in_b = next(b)

        while True:
            if e_in_a==e_in_b:
                yield next(a)

            else:
                yield from [e_in_a, e_in_b]    
            e_in_a = next(a)
            e_in_b = next(b)    

# Q4.WWPD-OOP
class Student:
    num_students = 0 # this is a class attribute
    def __init__(self, name, staff):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.num_students += 1
        print("There are now", Student.num_students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

# Q5.Email: Complete the implementation
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """
    def __init__(self, msg, sender_name, recipient_name):
        "*** YOUR CODE HERE ***"
        self.msg            = msg
        self.sender_name    = sender_name
        self.recipient_name = recipient_name
class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"
        email.recipient_name.inbox.append(email.msg)


    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """
    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.name   = name
        self.server = server
        self.server.clients[self.name] = self

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        "*** YOUR CODE HERE ***"
        email = Email(msg, self.name, recipient_name)
        self.server.clients[recipient_name].inbox.append(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        "*** YOUR CODE HERE ***"
        self.inbox.append(email.msg)
 
 # Q7. Cats
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives
    def talk(self):
        """ Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        "*** YOUR CODE HERE ***"
        if self.lives>0:
            self.lives-=1
        else:
            print(self.name + " has no more lives to lose!")    
            self.is_alive = False

# Q8. Noisy cat
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""

    def talk(self):
        """Talks twice as much as a regular cat.

        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        Cat.talk(self)
        Cat.talk(self)

# Q9. Exam prep: Amplify
from functools import reduce

def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that are all true values

    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    "*** YOUR CODE HERE ***"
    yield x
    while f(x):
        yield f(x)
        x=f(x)

# Q10. Fibonacci Generator
def fib_gen():
    """
    >>> fg = fib_gen()
    >>> for _ in range(7):
    ...     print(next(fg))
    0
    1
    1
    2
    3
    5
    8
    """
    yield from [0,1]
    a = [[0,1]]
    for x, y in a:
        yield x+y
        a.append([a[-1][-1], x+y])

# Q11: Cucumber - Fall 2015 Final Q7        
class Game:
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> g = Game()
    >>> g.play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    >>> g.winners
    [1]
    >>> g.play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It is not your turn, player 3
    It is not your turn, player 0
    The round is over, player 1
    >>> g.winners
    [1, 3]
    >>> g.play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It is not your turn, player 2
    >>> g.winners
    [1, 3]
    """
    def __init__(self):
        self.winners = []

    def play_round(self, starter, cards):
        r = Round(starter)
        for who, card in cards:
            try:
                r.play(who, card)
            except AssertionError as e:
                print(e)
        if r.winner != None:
            self.winners.append(r.winner)

class Round:
    players = 4

    def __init__(self, starter):
        self.starter = starter
        self.next_player = starter
        self.highest = -1
        self.winner = None
        
    
    def play(self, who, card):
        assert  self.next_player!=self.starter or self.winner==None, f'The round is over, player {who}'
        assert who == self.next_player, f'It is not your turn, player {who}'
        self.next_player = (who+1)%4
        
        if card >= self.highest:
            self.highest = card
            self.player_with_highest = who
            
        if self.next_player==self.starter:
            self.winner = self.player_with_highest   
            self.cards_played  = 0
    
    def is_complete(self):
        """Checks if a game could end."""
        return len(self.cards)%4==0

# Q12. Partition generator
def partition_gen(n):
    """
    >>> for partition in partition_gen(4): # note: order doesn't matter
    ...     print(partition)
    [4]
    [3, 1]
    [2, 2]
    [2, 1, 1]
    [1, 1, 1, 1]
    """
    """def yield_helper(j, k):
        if j == 0:
            ____________________________________________
        elif ____________________________________________:
            for small_part in ________________________________:
                yield ____________________________________________
            yield ________________________________________
    yield from yield_helper(n, n)"""
    
           