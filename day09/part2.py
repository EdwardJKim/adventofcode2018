"""
--- Part Two ---

Amused by the speed of your answer, the Elves are curious:

What would the new winning Elf's score be if the number of the last marble were
100 times larger?
"""


class Node:

    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def play(num_players: int, last_marble:int) -> int:

    head = curr = Node(0)
    head.next = head
    head.prev = head

    count = player = 1
    scores = [0] * (num_players + 1)

    while count <= last_marble:

        if count % 23 == 0:

            scores[player] += count
            for _ in range(7):
                curr = curr.prev
            scores[player] += curr.data
            next_node = curr.next
            prev_node = curr.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            curr = next_node

        else:
            curr = curr.next
    
            new_node = Node(count, curr, curr.next)
    
            next_node = curr.next
            curr.next = new_node
            next_node.prev = new_node
            
            curr = curr.next

        count += 1
        player = player % num_players + 1

    return max(scores)


def test_play():

    assert play(9, 25) == 32
    assert play(10, 1618) == 8317
    assert play(13, 7999) == 146373
    assert play(17, 1104) == 2764
    assert play(21, 6111) == 54718
    assert play(30, 5807) == 37305


if __name__ == "__main__":

    test_play()
    print("all tests passed")

    num_players = input("Enter number of players: ")
    last_marble = input("Enter how much last marble is worth: ")
    answer = play(int(num_players), int(last_marble))
    print("answer:", answer)
