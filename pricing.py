from pricing import PizzaPricingGraph, LineItemNode, LineItemGroup, BasePricingGraph
from pricing.base_pricing import SubgraphLayer


class PricingGraph(BasePricingGraph):
    def __init__(self):
        super().__init__()
        self.name = "Order"

        # Store nodes in a dictionary for easy access
        pizza_subgraph = PizzaPricingGraph()
        pizza_layer = SubgraphLayer('Pizza', pizza_subgraph)

        drink_layer = LineItemGroup('Drink', {
            LineItemNode('Drink1', price=2),
            LineItemNode('Drink2', price=3),
            LineItemNode('Drink3', price=4),
        })

        tax_layer = LineItemGroup('Tax', {
            LineItemNode('Tax', multiplier=1.1),
        })

        # Define layers
        self.layers.append(pizza_layer)
        self.layers.append(drink_layer)
        self.layers.append(tax_layer)

        # Add nodes and edges from subgraphs and layers
        self.add_nodes_from_subgraph_layer(pizza_layer)
        self.add_nodes()

        # Add edges for each layer
        self.add_edges_for_layer(drink_layer, tax_layer, allow_self_loop=True)

    def add_nodes_from_subgraph_layer(self, subgraph_layer):
        """
        Add nodes from a SubgraphLayer to the current graph.
        :param subgraph_layer: An instance of SubgraphLayer.
        """
        for node in subgraph_layer.get_nodes():
            self.nodes[node.name] = node

    def generate_receipt(self, order):
        """
        Generate a receipt based on the given order.
        :param order: List of node names representing the order.
        """
        print("Receipt:")
        total_price = 0
        for node_name in order:
            node = self.nodes[node_name]
            if node.price > 0:
                print(f"{node.name}: ${node.price:.2f}")
            total_price += node.price
            total_price *= node.multiplier
        print(f"Total Price: ${total_price:.2f}")


# Example usage:
# Define a traversal path using node names: ['Base2', 'Topping1', 'Topping2', 'Size', 'Tax']
pricing_graph = PricingGraph()
# Example usage:
# pricing_graph.display_graph()
# Example usage:
# Define traversal paths for two pizzas
order = ['Base2', 'Topping1', 'Topping2', 'Size', 'Tax', 'Base1', 'Topping3', 'Size', 'Tax']

# # Calculate the total price for the entire order
total_price = pricing_graph.calculate_price(order)

# # Print the total price
print(f"Total Price for the Order: ${total_price:.2f}")

# # Generate a receipt for the entire order
pricing_graph.generate_receipt(order)


