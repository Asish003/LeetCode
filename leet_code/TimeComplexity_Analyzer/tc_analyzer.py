import ast

# Helper function to set parent attributes
def add_parents(node, parent=None):
    node.parent = parent  # Set the parent attribute
    for child in ast.iter_child_nodes(node):
        add_parents(child, node)  # Recursively set the parent for each child

class ExtendedTimeComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.recursive_calls = []
        self.loop_complexity = []
        self.branching_complexity = []

    def visit_FunctionDef(self, node):
        print(f"Analyzing function: {node.name}")
        self.current_function_name = node.name  # Track the current function name
        self.generic_visit(node)

    def visit_Call(self, node):
        # Check if the call is recursive by comparing with the current function name
        if isinstance(node.func, ast.Name):
            if node.func.id == self.current_function_name:  # Direct recursion check
                self.recursive_calls.append(node.func.id)
                print("Detected recursive call:", node.func.id)
        self.generic_visit(node)

    def visit_For(self, node):
        print("Detected a for loop - potential O(n) complexity.")
        self.loop_complexity.append("O(n)")
        self.generic_visit(node)

    def visit_While(self, node):
        print("Detected a while loop.")
        self.loop_complexity.append("O(n)")  # Placeholder, adjust as needed
        self.generic_visit(node)

    def visit_If(self, node):
        print("Detected an if statement.")
        self.branching_complexity.append("Conditional path")
        self.generic_visit(node)

def analyze_code_complexity(code):
    tree = ast.parse(code)
    add_parents(tree)  # Call the helper to add parent attributes
    analyzer = ExtendedTimeComplexityAnalyzer()
    analyzer.visit(tree)
    return {
        "recursive_calls": analyzer.recursive_calls,
        "loop_complexity": analyzer.loop_complexity,
        "branching_complexity": analyzer.branching_complexity,
    }

# Example usage
code_sample = """
class Solution:
    def numJewelsInStones(self, nums) -> int:
        for i in range(len(nums)):
            print(i)
"""
max_length=0
s=15
nums=[2,3,5,5,10,1,1,3,5,5]
sums={}
count=0
for i,num in enumerate(nums):
    count+=num
    if count==s:
        max_length=i+1
    if (count-s) in sums:
        max_length=max(max_length,i-sums[count-s])
    if count not in sums:
        sums[count]=i 
print(max_length)

complexity_info = analyze_code_complexity(code_sample)
print("Complexity Info:", complexity_info)
