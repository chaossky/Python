# Tree Node class
class TreeNode:
    def __init__(self, value):
        if value is None:
            raise ValueError("Node value cannot be None")
        self.value = value
        self.children = []  # List to store child nodes

    def add_child(self, child_node):
        """Add a child node to the current node."""
        if not isinstance(child_node, TreeNode):
            raise TypeError("Child must be a TreeNode instance")
        self.children.append(child_node)

    def remove_child(self, child_node):
        """Remove a child node if it exists."""
        if child_node in self.children:
            self.children.remove(child_node)

    def __repr__(self):
        return f"TreeNode({self.value})"


# Tree class
class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def traverse(self, node=None, level=0):
        """Print the tree structure in a hierarchical format."""
        if node is None:
            node = self.root
        print(" " * (level * 4) + f"- {node.value}")
        for child in node.children:
            self.traverse(child, level + 1)

    def search(self, value, node=None):
        """Search for a value in the tree using DFS."""
        if node is None:
            node = self.root
        if node.value == value:
            return node
        for child in node.children:
            found = self.search(value, child)
            if found:
                return found
        return None


# Example usage
if __name__ == "__main__":
    # Create a tree
    tree = Tree("Root")

    # Add children to root
    child_a = TreeNode("A")
    child_b = TreeNode("B")
    tree.root.add_child(child_a)
    tree.root.add_child(child_b)

    # Add grandchildren
    child_a.add_child(TreeNode("A1"))
    child_a.add_child(TreeNode("A2"))
    child_b.add_child(TreeNode("B1"))

    # Display tree
    print("Tree Structure:")
    tree.traverse()

    # Search for a node
    search_value = "A2"
    result = tree.search(search_value)
    if result:
        print(f"\nNode '{search_value}' found: {result}")
    else:
        print(f"\nNode '{search_value}' not found.")