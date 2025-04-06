import networkx as nx
from .graph import LineItemNode, LineItemGroup
from pricing.base_pricing import BasePricingGraph


class PizzaPricingGraph(BasePricingGraph):
    def __init__(self):
        # Initialize a directed graph
        super().__init__()
        self.name = "Pizza"

        # Store nodes in a dictionary for easy access
        base_layer = LineItemGroup('Base', {
            LineItemNode('Base1', price=8),
            LineItemNode('Base2', price=10),
            LineItemNode('Base3', price=12),
        })

        topping_layer = LineItemGroup('Topping', {
            LineItemNode('Topping1', price=1.5),
            LineItemNode('Topping2', price=2),
            LineItemNode('Topping3', price=2.5),
        })

        size_layer = LineItemGroup('Size', {
            LineItemNode('Size', multiplier=1.5),
        })

        # Define layers
        self.layers.append(base_layer)
        self.layers.append(topping_layer)
        self.layers.append(size_layer)

        self.add_nodes()


        # Add edges for each layer
        self.add_edges_for_layer(base_layer, topping_layer, allow_self_loop=False, skip_layer=size_layer)
        self.add_edges_for_layer(topping_layer, size_layer, allow_self_loop=True)


