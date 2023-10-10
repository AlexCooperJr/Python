from bakery import assert_equal
def convert_hand(card:int):
    '''
    This function will intake the values of each card and convert to the appropriate value
    Arguement:
        it takes in an integer value representing a playing card
    Return:
        it will return a string if the number is 10 or greater but
        will return the integer otherwise
    '''
    if card==10:
        return 'X'
    if card==11:
        return 'J'
    if card==12:
        return 'Q'
    if card==13:
        return 'K'
    if card==14:
        return 'A'
    else:
        return card
    
def hand_to_string(hand:list[int])->str:
    '''
    This function should use another function convert_hand to take integers out of a list to
    convert each integer into a string
    Arguements:
        the varible hand which is a list of integers represening a hand of cards
    returns:
        this function returns the the integers (or strings if converted) as all string values
    '''
    card1=hand[0]
    display_card1=convert_hand(card1)
    card2=hand[1]
    display_card2=convert_hand(card2)
    card3=hand[2]
    display_card3=convert_hand(card3)
    players_hand=display_card1,display_card2,display_card3
    players_hand=str(players_hand)
    players_hand=players_hand.replace(",","")
    players_hand=players_hand.replace("'","")
    players_hand=players_hand.replace("(","")
    players_hand=players_hand.replace(")","")
    
    return players_hand
assert_equal(hand_to_string([1,2,3]),"1 2 3")
assert_equal(hand_to_string([10,11,12]),"X J Q")
assert_equal(hand_to_string([10,2,14]),"X 2 A")


def sort_hand(hand:list[int])->list[int]:
    '''
    this function takes in a list of 3 integers
    and sorts them in order greatest to least
    Arguements:
        This function requires a list of integers that represent a hand of cards
    Returns:
        This function returns a lsit fo integers but ordered from greatest to least
        representing the hand in order
    '''
    first_card=hand[0]
    second_card=hand[1]
    third_card=hand[2]
    if (first_card>= second_card) and (second_card>=third_card) and (first_card>=third_card):
        return [first_card,second_card,third_card]
    if (first_card>=second_card) and (second_card<third_card) and (first_card>=third_card):
        return [first_card,third_card,second_card]
    if (first_card<second_card) and (second_card>= third_card) and (first_card>=third_card):
        return [second_card,first_card,third_card]
    if (first_card<second_card) and (second_card>= third_card) and (first_card<third_card):
        return [second_card,third_card,first_card]
    if (first_card<second_card) and (second_card<third_card) and (first_card<third_card):
        return [third_card,second_card,first_card]
    if (first_card>=second_card) and (second_card< third_card) and (first_card<third_card):
        return [third_card,first_card,second_card]
    
assert_equal(sort_hand([1,2,3]),[3,2,1])
assert_equal(sort_hand([1,5,7]),[7,5,1])
assert_equal(sort_hand([9,5,7]),[9,7,5])
assert_equal(sort_hand([6,9,3]),[9,6,3])
assert_equal(sort_hand([4,2,1]),[4,2,1])
assert_equal(sort_hand([1,9,3]),[9,3,1])
    
def has_triple(hand:list[int])->bool:
    '''
    This function takes a list of 3 integers and determines whether or not the all 3 values are equal
    Arguements:
        this function requires a list of integers
        representing a hand of cards
    Returns:
        a boolean based on whether or not the hand represnts 3 of a kind
        (all 3 integers being the same)
    '''
    card1=hand[0]
    card2=hand[1]
    card3=hand[2]
    if card1==card2 and card1==card3:
        return True
    else:
        return False
    
assert_equal(has_triple([1,1,1]),True)
assert_equal(has_triple([1,2,1]),False)
assert_equal(has_triple([9,9,9]),True)
assert_equal(has_triple([2,1,1]),False)
assert_equal(has_triple([1,1,2]),False)
assert_equal(has_triple([12,12,12]),True)

def has_straight(hand:list[int])->bool:
    '''
    This functions intakes a list of 3 integers and determines whether or not the hand is a 'straight' or consecutive numbers
    Arguements:
        The hand a list of integers representing cards
    Returns:
        A boolean based on whether or not the hand has a straight
        a straight is 3 consecutive numbers
    '''
    card1=hand[0]
    card2=hand[1]
    card3=hand[2]
    if card2==card1+1 and card3==card2+1:
        return True
    if card3+1==card2 and card2+1==card1:
        return True
    else:
        return False
    
assert_equal(has_straight([1,2,3]),True)
assert_equal(has_straight([1,3,4]),False)
assert_equal(has_straight([2,5,7]),False)

def has_pair(hand:list[int])->bool:
    '''
    This function intakes a list of 3 integers and determines whether any of the values are equal
    arguements:
        hand(list[int]) representing the players hand
    returns:
        a boolen representing whether or not you have a pair
        2 cards that are equal with some other third card that is not related
    '''
    card1=hand[0]
    card2=hand[1]
    card3=hand[2]
    if card1==card2 or card2==card3 or card1==card3:
        return True
    else:
        return False
    
assert_equal(has_pair([1,1,2]),True)
assert_equal(has_pair([1,2,1]),True)
assert_equal(has_pair([2,1,1]),True)
assert_equal(has_pair([1,3,2]),False)

def score_hand(hand:list[int])->int:
    '''
    This function is intened to score a players hand by taking the values 
    using base-16 to determine a hand score
    arguements:
        hand(list[int]) representing the hand which is a list of integers
    returns:
        an integer value that can be compared to determine a winner down the line.
        using base-16 specific conditions recieve score multipliers making certain
        hand types trump others
    '''
    card1=hand[0]
    card2=hand[1]
    card3=hand[2]
    if has_triple(hand)==True:
        total=(16*(16**3))+(card1*(16**2))+(card2*16)+(card3)
        return total
    if has_straight(hand)==True:
        total=(15*(16**3))+(card1*(16**2))+(card2*16)+(card3)
        return total
    if has_pair(hand)==True:
        total=(card2*(16**3))+(card1*(16**2))+(card2*16)+(card3)
        return total
    else:
        return (card1*(16**2))+(card2*16)+(card3)
    
assert_equal(score_hand([5,3,1]),1329)
assert_equal(score_hand([1,1,1]),65809)
assert_equal(score_hand([3,2,1]),62241)
assert_equal(score_hand([2,1,1]),4625)
    
def dealer_plays(hand:list[int])->bool:
    '''
    This function is going to take in a list of 3 integers and by scoring the hand will determine 
    the dealers move
    arguements:
        hand which is a list that represents the dealers hand
    returns:
        a boolean True if the hand is queen high or better
    '''
    card1=hand[0]
    card2=hand[1]
    card3=hand[2]
    score=score_hand(hand)
    if score>=3105:
        return True
    else:
        return False
    
assert_equal(dealer_plays([5,3,1]),False)
assert_equal(dealer_plays([3,2,1]),True)
assert_equal(dealer_plays([12,3,5]),True)
assert_equal(dealer_plays([11,7,5]),False)

def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

def play_round()->int:
    player_hand=deal()
    dealer_hand=deal()
    player_hand=sort_hand(player_hand)
    dealer_hand=sort_hand(dealer_hand)
    player_hand_view=hand_to_string(player_hand)
    dealer_hand_view=hand_to_string(dealer_hand)
    print(player_hand_view)
    dealer_score=score_hand(dealer_hand)
    choice=get_choice()
    if choice=="f":
        return -10  
    if choice=="p":
        player_score=score_hand(player_hand)
        if dealer_plays(dealer_hand)==False:
            print(dealer_hand_view)
            return +10
        if dealer_plays(dealer_hand)==True:
            print(dealer_hand_view)
            if player_score > dealer_score:
                return +20
            if player_score < dealer_score:
                return -20     


        
score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")

             
