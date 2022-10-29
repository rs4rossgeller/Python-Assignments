class BoyerMoore:
    """To find the majority element in the array."""

    def __init__(self, candidate_array):
        self.votes: int = 0
        self.candidate: int = -1
        self.candidate_array: list = candidate_array

    def find_majority(self) -> int:
        """
        To find the majority element in the array.

        Returns:
            int: The majority element in the array.
        """
        for i in self.candidate_array:
            if self.votes == 0:
                self.candidate = i
                self.votes += 1
            elif self.candidate == i:
                self.votes += 1
            else:
                self.votes -= 1

        if self.is_majority():
            return self.candidate
        else:
            return -1

    def is_majority(self) -> bool:
        """
        To find whether the candidate element is the majority element.

        Returns:
            bool: True if the candidate element is the majority element, False otherwise.

        """
        count: int = 0
        for i in self.candidate_array:
            if i == self.candidate:
                count += 1
        return count > len(self.candidate_array) // 2


if __name__ == "__main__":
    bm = BoyerMoore([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    print("Candidate Array: ", bm.candidate_array)
    print("Majority element is: ", bm.find_majority())
