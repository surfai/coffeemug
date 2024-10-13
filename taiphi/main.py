from langgraph.graph import Graph
from queryextractnode import QueryExtractNode
from calltaiphi import CallTaiphi
from generateinstruct import GenerateInstruct
import os
from IPython.display import Image, display


"""
This script defines and executes a Langchain graph workflow for processing user queries.

The workflow consists of three main components:
1. QueryExtractNode: Extracts and processes the initial user query.
2. CallTaiphi: Interacts with the Taiphi system based on the extracted query.
3. GenerateInstruct: Generates instructions or responses based on Taiphi's output.

The script demonstrates how to set up the graph, compile it into an executable app,
and run it with both single invocation and streaming modes.
"""

# Define a Langchain graph
workflow = Graph()

"""
Define and configure the Langchain graph workflow.

This workflow consists of three nodes:
- QueryExtractNode: Processes the initial user query
- CallTaiphi: Interacts with the Taiphi system
- GenerateInstruct: Generates final instructions or responses

The workflow is set up as a linear sequence from QueryExtractNode to CallTaiphi to GenerateInstruct.
"""

workflow.add_node("QueryExtractNode", QueryExtractNode)
workflow.add_node("CallTaiphi", CallTaiphi)
workflow.add_node("GenerateInstruct", GenerateInstruct)

workflow.add_edge('QueryExtractNode', 'CallTaiphi')
workflow.add_edge('CallTaiphi', 'GenerateInstruct')

workflow.set_entry_point("QueryExtractNode")
workflow.set_finish_point("GenerateInstruct")


app = workflow.compile()

"""
Demonstrate the usage of the compiled Langchain graph.

This section shows how to invoke the workflow with a sample input using the invoke() method.
It processes the input through all nodes in the graph and returns the final output.
"""

# Create the /img folder if it doesn't exist
os.makedirs("img", exist_ok=True)

# Generate and save the graph as an image
try:
    image_path = os.path.join("img", "workflow_graph.png")
    workflow.get_graph().draw_png(image_path)
    print(f"Graph image saved to: {image_path}")
    
    # Optionally, you can still display the image if you're in a Jupyter notebook
    # display(Image(image_path))
except Exception as e:
    print("Error generating or saving the graph image:", e)

# Example of invoking the compiled workflow
#result = app.invoke('I am moving from')
#print("Invoke result:", result)

"""
Stream the workflow execution and print the output from each node.

This section demonstrates how to use the stream() method to process the input
and display the intermediate results from each node in the workflow. This is useful
for understanding the step-by-step processing of the input through the graph.
"""

# Streaming example
input = 'Starting'
for output in app.stream(input):
    # stream() yields dictionaries with output keyed by node name
    for key, value in output.items():
        print(f"Output from node '{key}':")
        print("---")
        print(value)
    print("\n---\n")
