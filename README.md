# Graph Pricing Model

The **Graph Pricing Model** is a Python-based project that uses graph structures to model and calculate pricing for complex orders. It supports modular subgraphs, allowing for flexible and reusable pricing components.

## Features

- **Layered Graph Structure**: Define pricing layers (e.g., Pizza, Drinks, Tax) with nodes representing individual items or components.
- **Subgraph Support**: Use subgraphs as layers to encapsulate reusable pricing logic.
- **Dynamic Pricing**: Support for fixed prices and multipliers (e.g., tax).
- **Receipt Generation**: Generate detailed receipts for orders.

## Project Structure

```
graph-pricing-model/
├── pricing.py          # Main graph implementation
├── pricing/            # Supporting modules
│   ├── base_pricing.py # Base classes and utilities
│   └── ...             # Other pricing-related modules
└── README.md           # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/graph-pricing-model.git
   cd graph-pricing-model
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Example Code

```python
from pricing import PricingGraph

# Initialize the pricing graph
pricing_graph = PricingGraph()

# Define an order as a list of node names
order = ['Base2', 'Topping1', 'Topping2', 'Size', 'Tax', 'Base1', 'Topping3', 'Size', 'Tax']

# Calculate the total price for the order
total_price = pricing_graph.calculate_price(order)
print(f"Total Price for the Order: ${total_price:.2f}")

# Generate a receipt for the order
pricing_graph.generate_receipt(order)
```

### Output Example

```
Receipt:
Base2: $5.00
Topping1: $1.50
Topping2: $2.00
Size: $3.00
Tax: $1.10
Base1: $4.00
Topping3: $1.75
Size: $3.00
Tax: $1.10
Total Price: $22.45
```

## Key Classes

### `BasePricingGraph`
- The base class for creating pricing graphs.
- Manages nodes, edges, and traversal logic.

### `LineItemNode`
- Represents an individual item in the pricing graph.
- Supports fixed prices and multipliers.

### `LineItemGroup`
- Groups related nodes into a logical layer.

### `SubgraphLayer`
- Encapsulates a subgraph as a reusable layer in the parent graph.

### `PricingGraph`
- Extends `BasePricingGraph` to define a complete pricing model.
- Includes layers for pizza, drinks, and tax.

## Extending the Project

To add new layers or subgraphs:
1. Create a new subgraph class (e.g., `DessertPricingGraph`).
2. Add it as a `SubgraphLayer` in `PricingGraph`.
3. Define edges to connect it to other layers.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For questions or support, please contact [your-email@example.com].