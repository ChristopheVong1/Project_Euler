from itertools import combinations
from collections import defaultdict

def hand(hole_cards, community_cards):
    """
    Step 1: Combine all the cards
    Step 2: Check each hand from straight flush to nothing
    Step 3: For each hand check the rank to find the best combination
    Step 4: Return the result in the correct format
    """
    
    # Initialization
    all_cards = hole_cards + community_cards
    best_hand = None
    best_rank = (0, [])

    # Generate all possible 5-card combinations
    for five_cards in combinations(all_cards, 5):
        hand_type, ranks = evaluate_hand(five_cards)
        # Convert hand type to a numerical rank for comparison
        type_rank = hand_rank(hand_type)
        current_rank = (type_rank, ranks)
        if current_rank > best_rank:
            best_rank = current_rank
            best_hand = (hand_type, ranks)

    return best_hand

def colors(hands):
    """
    Get the color (spade, club, heart or diamond) of each cards
    Arg: hands: A list of cards where the last value shows the symbol of the card
    Return: A list of every symbol
    """
    return [card[-1] for card in hands]

def values(hands):
    """
    Get the value of each cards (the number), beware A counts as rank 14
    Arg: hands: A list of cards where the first values corresponds to the rank
    Return: A list of every value
    """
    return [card[:-1] for card in hands]

def is_straight_flush(hand):

def is_four_kind(hand):

def is_full_house(hand):

def is_flush(hand):

def is_straight(hand):

def is_three_kind(hand):

def is_two_pair(hand):

def is_pair(hand):


def evaluate_hand(five_cards):
    suits = [card[-1] for card in five_cards]
    ranks = sorted([card[:-1] for card in five_cards], key=rank_value, reverse=True)
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    sorted_counts = sorted(rank_counts.items(), key=lambda item: (-item[1], -rank_value(item[0])))
    is_flush = len(set(suits)) == 1
    is_straight, straight_high = check_straight(ranks)
    
    # Check for straight flush
    if is_straight and is_flush:
        return ("straight-flush", [straight_high])
    
    # Check for four of a kind
    if sorted_counts[0][1] == 4:
        kicker = sorted_counts[1][0] if len(sorted_counts) > 1 else None
        return ("four-of-a-kind", [sorted_counts[0][0], kicker] if kicker else [sorted_counts[0][0]])
    
    # Check for full house
    if sorted_counts[0][1] == 3 and len(sorted_counts) > 1 and sorted_counts[1][1] >= 2:
        return ("full house", [sorted_counts[0][0], sorted_counts[1][0]])
    
    # Check for flush
    if is_flush:
        return ("flush", [r for r, _ in sorted_counts])
    
    # Check for straight
    if is_straight:
        return ("straight", [straight_high])
    
    # Check for three of a kind
    if sorted_counts[0][1] == 3:
        kickers = [item[0] for item in sorted_counts[1:]]
        return ("three-of-a-kind", [sorted_counts[0][0]] + kickers[:2])
    
    # Check for two pair
    if sorted_counts[0][1] == 2 and len(sorted_counts) > 1 and sorted_counts[1][1] == 2:
        kicker = sorted_counts[2][0] if len(sorted_counts) > 2 else None
        pairs = sorted([sorted_counts[0][0], sorted_counts[1][0]], key=rank_value, reverse=True)
        return ("two pair", pairs + ([kicker] if kicker else []))
    
    # Check for pair
    if sorted_counts[0][1] == 2:
        kickers = [item[0] for item in sorted_counts[1:]]
        return ("pair", [sorted_counts[0][0]] + kickers[:3])
    
    # High card
    return ("nothing", [r for r, _ in sorted_counts])

def check_straight(ranks):
    unique_ranks = sorted(list({r for r in ranks}), key=rank_value)
    if len(unique_ranks) < 5:
        return False, None
    # Check for Ace-high straight (10, J, Q, K, A)
    if set(unique_ranks[-5:]) == {'10', 'J', 'Q', 'K', 'A'}:
        return True, 'A'
    # Check other straights
    for i in range(len(unique_ranks) - 4):
        consecutive = True
        for j in range(1, 5):
            if rank_value(unique_ranks[i + j]) != rank_value(unique_ranks[i]) + j:
                consecutive = False
                break
        if consecutive:
            return True, unique_ranks[i + 4]
    return False, None

def rank_value(rank):
    rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return rank_order.get(rank, 0)

def hand_rank(hand_type):
    rank_order = {
        "straight-flush": 8,
        "four-of-a-kind": 7,
        "full house": 6,
        "flush": 5,
        "straight": 4,
        "three-of-a-kind": 3,
        "two pair": 2,
        "pair": 1,
        "nothing": 0
    }
    return rank_order.get(hand_type, 0)

