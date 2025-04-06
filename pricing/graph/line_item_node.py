class LineItemNode:
    def __init__(self, name, price=0, multiplier=1):
        """
        Initialize a graph node.
        :param name: Name of the node.
        :param price: Price associated with the node (default is 0).
        :param multiplier: Multiplier associated with the node (default is 1).
        """
        if price != 0 and multiplier != 1:
            raise ValueError("A node cannot have both a price and a multiplier. They must be mutually exclusive.")
        self.name = name
        self.price = price
        self.multiplier = multiplier

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, LineItemNode) and self.name == other.name

    def __repr__(self):
        return f"GraphNode(name={self.name}, price={self.price}, multiplier={self.multiplier})"
