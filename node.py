from polynomial import Polynomial
class Node:
    def __init__(self,data:Polynomial) -> None:
        self.data = data
        self.next = None