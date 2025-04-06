import networkx as nx
import matplotlib.pyplot as plt

from .graph import LineItemGroup, LineItemNode

class SubgraphLayer:
    """
    A class to encapsulate a subgraph as a layer in the parent graph.
    """
    def __init__(self, name, subgraph):
        self.name = name
        self.subgraph = subgraph

    @property
    def nodes(self):
        """
        Retrieve all nodes from the subgraph.
        """
        return self.get_nodes()

    def get_nodes(self):
        """
        Retrieve all nodes from the subgraph.
        """
        return self.subgraph.nodes.values()

    def get_edges(self):
        """
        Retrieve all edges from the subgraph.
        """
        return self.subgraph.edges


class BasePricingGraph:
    def __init__(self):
        # Initialize a directed graph
        self.graph = nx.DiGraph()
        self.layers: list[LineItemGroup] = []
        self.nodes: dict[str: LineItemNode] = {}
        self.name = "BaseItem"

    def add_nodes(self):
        """
        Add a nodes to the graph.
        """
        all_nodes = set()
        for layer in self.layers:
            if isinstance(layer, LineItemGroup):
                all_nodes.update(layer.nodes)
            elif isinstance(layer, LineItemNode) or isinstance(layer, nx.DiGraph):
                all_nodes.add(layer)
            if isinstance(layer, SubgraphLayer):
                continue

        self.nodes = {node.name: node for node in all_nodes}

        # Add all nodes to the graph
        self.graph.add_nodes_from(all_nodes)
        

    def add_edges_for_layer(self, current_layer: LineItemGroup, next_layer: LineItemGroup, allow_self_loop=False, skip_layer=None, connect_within_layer=False):
        """
        Add edges for a layer in the graph.
        :param current_layer: List of nodes in the current layer.
        :param next_layer: List of nodes in the next layer.
        :param allow_self_loop: Whether nodes in the current layer can have self-loops.
        :param skip_layer: Optional layer to skip connections to.
        :param connect_within_layer: Whether nodes in the current layer should connect to other nodes in the same layer.
        """
        if skip_layer is not None and next_layer == skip_layer:
            return

        for node in current_layer.nodes:
            # Connect to all nodes in the next layer
            self.graph.add_edges_from((node, next_node) for next_node in next_layer.nodes)

            # Add self-loop if allowed
            if allow_self_loop:
                self.graph.add_edge(node, node)

            # Connect to other nodes in the same layer if allowed
            if connect_within_layer:
                self.graph.add_edges_from((node, other_node) for other_node in current_layer.nodes if node != other_node)

    def calculate_price(self, traversal_path):
        """
        Calculate the price based on a traversal path.
        :param traversal_path: List of node names representing the traversal path.
        :return: Total price calculated based on the traversal.
        """
        price = 0

        for node_name in traversal_path:
            node = self.nodes[node_name]
            price += node.price
            price *= node.multiplier

        return price

    def generate_receipt(self, order):
        """
        Generate a receipt based on the given order.
        :param order: List of node names representing the order.
        """
        total_price = 0
        for node_name in order:
            node = self.nodes[node_name]
            if node.price > 0:
                print(f"{node.name}: ${node.price:.2f}")
            total_price += node.price
            total_price *= node.multiplier
        print(f"{self.name}: ${total_price:.2f}")

    def display_graph(self):
        """
        Display the graph visually using matplotlib with layers shown sequentially.
        """
        plt.figure(figsize=(10, 8))


        pos = {}

        n = len(self.layers)

        # Assign positions for each layer
        for j, layer in enumerate(self.layers):
            if not layer.nodes:
                    continue
            elif len(layer.nodes) < 2:
                pos[next(iter(layer.nodes))] = (1.5, n-j)
            else:
                for i, node in enumerate(layer.nodes):
                    pos[node] = (i, n-j)

        # Draw the graph with the specified positions
        nx.draw(self.graph, pos, with_labels=False, node_size=3000, node_color="lightblue")
        labels = {node: f"{node.name}\n${node.price}" for node in self.graph.nodes}
        nx.draw_networkx_labels(self.graph, pos, labels=labels)
        plt.title("Pricing Graph (Sequential Layers)")
        plt.show()


