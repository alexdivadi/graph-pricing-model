class LineItemGroup:
    def __init__(self, name, nodes={}):
        """
        Initialize a graph node.
        :param name: Name of the Group.
        :param nodes: Collection of nodes in the group.
        """
        self.name = name
        self.nodes = nodes

