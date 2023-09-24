import sys

class Participant:
    def __init__(self, name:str, skills:list):
        self.name = name
        self.skills = skills

    def __str__(self):
        return f"{self.name}, {self.skills}"

def create_order(captain:Participant):
    """
    Create order of the skills
    @param captain Participant: captain
    @return dict[int, int]: order of the skills
    """
    order = {}
    for i, skill in enumerate(captain.skills[::-1]):
        order[skill] = i

    return order

def merge_count_order(left:list[int], right:list[int], order:dict[int, int]):
    """
    Merge two sorted arrays with order that is dict of the values and its expected index
    @param left list[int]: left sorted array
    @param right list[int]: right sorted array
    @param order dict[int, int]: order of the values
    @return (list[int], int): merged sorted array and number of inversions
    """
    merged = []
    count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if order[left[i]] <= order[right[j]]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count

def merge_sort_count(skills:list[int], order:dict[int, int]):
    """
    Merge sort counting inversions
    @param skills list[int]: list of skills
    @return (list[int], int): sorted list of skills and number of inversions
    """
    if len(skills) <= 1:
        return skills, 0
    
    mid = len(skills) // 2
    left, left_inv = merge_sort_count(skills[:mid],order)
    right, right_inv = merge_sort_count(skills[mid:],order)
    merged, merge_inv = merge_count_order(left, right, order)
    
    return merged, (left_inv + right_inv + merge_inv)

def find_participant_with_least_inversions(participants:list[Participant],captain:Participant):
    """
    Find participant with the least number of inversions
    @param participants list[Participant]: list of participants
    @return Participant: participant with the least number of inversions
    """
    order = create_order(captain)

    min_inversions = float('inf')
    result = None

    for p in participants:
        _, inversions = merge_sort_count(p.skills, order)
        #print(p," con " , inversions)  #Debug line
        if inversions < min_inversions:
            min_inversions = inversions
            result = p

    return result

def read_participants(path: str):
    """
    Read participants from file
    @param path str: path to file
    @return list[Participant]: list of participants
    """
    participants = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            arr = line.split(",")
            skills = [int(x.strip()) for x in arr[1:]]
            participant = Participant(arr[0], skills)
            participants.append(participant)

    return participants

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("No arguments given")
        return
    
    participants = read_participants(args[0])

    captain_index = int(args[1])
    if captain_index >= len(participants):
        print("Captain number is too high")
        return
    
    captain = participants.pop(captain_index)

    best=find_participant_with_least_inversions(participants, captain)
    if best is None:
        print("No best match found")
        return
    print(captain.name, ",", best.name)

# Other solution but not divide and conquer, it just works for the one with the least inversions

def compare_skills_with_best(skills:list[int], order:dict[int, int]):
    """
    Compare skills with the best match
    @param skills list[int]: list of skills
    @param order dict[int, int]: order of the values
    @return int: distance between the skills and the best match
    """
    distance = 0
    for i, skill in enumerate(skills):
        distance += abs(order[skill] - i)
    return distance

def get_best_match(participants:list[Participant], captain:Participant):
    """
    Get best match for the captain
    @param participants list[Participant]: list of participants
    @param captain Participant: captain
    @return Participant: best match for the captain
    """
    order = create_order(captain)
    distance = float('inf')
    result = None
    for p in participants:
        d = compare_skills_with_best(p.skills, order)
        print(p," con " , d)
        if d < distance:
            distance = d
            result = p
    return result

if __name__ == "__main__":
    main()


