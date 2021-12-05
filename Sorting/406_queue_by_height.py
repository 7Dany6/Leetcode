class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[
            1]))  # here we sort given sequence: firstly, we're looking at the person's height, then we compare by people in front of

        final_queue = []  # variable where we're going to store final queue

        for person in people:
            final_queue.insert(person[1], person)

        return final_queue
    