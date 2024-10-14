from langgraph.graph import Graph, StateGraph
from taiphi.queryextract import QueryExtractNode
from calltaiphi import CallTaiphi
from generateinstruct import GenerateInstruct
from typing import TypedDict, Annotated, Sequence
import operator
import os
from IPython.display import Image


"""
This script defines and executes a Langchain graph workflow for processing user queries.

The workflow consists of three main components:
1. QueryExtractNode: Extracts and processes the initial user query.
2. CallTaiphi: Interacts with the Taiphi system based on the extracted query.
3. GenerateInstruct: Generates instructions or responses based on Taiphi's output.

The script demonstrates how to set up the graph, compile it into an executable app,
and run it with both single invocation and streaming modes.
"""

AgentState = {}
AgentState["messages"] = []
AgentState["raw_query"] = []
AgentState["refined_query"] = []
AgentState["taiphi_response"] = []
AgentState["summary"] = []
AgentState["instruction"] = []
AgentState["final_response"] = []

"""
AgentState: A dictionary representing the state of the agent.

This dictionary is used to store and manage the state of the agent throughout its execution.
It currently contains a single key-value pair:

Attributes:
    messages (list): A list of strings representing the messages or actions
                     processed by the agent. This list is appended to as the
                     agent progresses through its workflow, allowing for
                     tracking of the agent's actions and decision-making process.

Usage:
    The AgentState dictionary is typically passed between different functions
    or nodes in a workflow graph. Each function can modify the state by
    appending to the 'messages' list, thereby building up a history of the
    agent's actions.

Example:
    AgentState = {}
    AgentState["messages"] = []
    
    def some_function(state):
        state["messages"].append("Performed action X")
        return state

Note:
    This simple structure can be expanded to include additional keys for more
    complex state management as the agent's capabilities grow.
"""


def function1(state):
    state["messages"].append(function1.__name__)
    state["user_query"].append("add user+query")
    return state

def function2(state):
    state["messages"].append(function2.__name__)
    return state

def statefunction1(state: AgentState) -> AgentState:
    state["messages"].append(statefunction1.__name__)
    state["messages"].append("add user+query")
    return state

def statefunction2(state: AgentState) -> AgentState:
    state["messages"].append(statefunction2.__name__)
    state["messages"].append("processed query")
    return state

# Define a new LangGraph workflow
stateworkflow = Graph()

# Add nodes to the graph
stateworkflow.add_node("Function1", function1)
stateworkflow.add_node("Function2", function2)

# Add edge to connect the nodes
stateworkflow.add_edge("Function1", "Function2")

# Set entry and finish points
stateworkflow.set_entry_point("Function1")
stateworkflow.set_finish_point("Function2")

# Compile the workflow
state_app = stateworkflow.compile()

# Example of invoking the compiled workflow
initial_state = {
    "messages": ["Starting..."],
    "user_query": ["add user+query"]
    }
result = state_app.invoke(initial_state)
print("State workflow result:", result)

# Streaming example for the state workflow
#print("\nStreaming state workflow:")
#for output in state_app.stream(initial_state):
#    for key, value in output.items():
#        print(f"Output from node '{key}':")
#        print("---")
#        print(value)
#    print("\n---\n")

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

#Image(filename="./img/workflow_graph.png", width=400)

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


class AgentState(TypedDict):
    messages: Annotated[Sequence[str], operator.add]
    summary: Annotated[Sequence[str], operator.add]
    instruction: Annotated[Sequence[str], operator.add]

stateclassgraph = StateGraph(AgentState)

stateclassgraph.add_node("StateFunction1", statefunction1)
stateclassgraph.add_node("StateFunction2", statefunction2)

stateclassgraph.add_edge("StateFunction1", "StateFunction2")

stateclassgraph.set_entry_point("StateFunction1")
stateclassgraph.set_finish_point("StateFunction2")

stateclassgraph_app = stateclassgraph.compile()

inputs = {
    "messages": ["Starting ...Tell me about Japan's Industrial Growth"],
    "user_query": ["add user+query"],
    "raw_query": ["add raw+query"],
    "refined_query": ["add refined+query"],
    "taiphi_response": ["add taiphi+response"],
    "summary": ["add summary"],
    "instruction": ["add instruction"],
    "final_response": ["add final+response"]
    }
out = stateclassgraph_app.invoke(inputs)

#print(out['messages'])
print(out['messages'][-1])
