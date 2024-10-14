"""
This module defines the main structure and flow of the Taiphi agent system.

It sets up a state graph using langgraph, defining the nodes and edges
for the agent's workflow. The graph includes steps for query extraction,
calling Taiphi, and generating instructions.
"""

from langgraph.graph import Graph, StateGraph
from queryextract import QueryExtract
from calltaiphi import CallTaiphi
from generateinstruct import GenerateInstruct
from typing import TypedDict, Annotated, Sequence
import operator
import os
from IPython.display import Image
from statemachine import AgentState

# Create a StateGraph instance with AgentState
stateclassgraph = StateGraph(AgentState)

# Add nodes to the graph
stateclassgraph.add_node("QueryExtract", QueryExtract)
stateclassgraph.add_node("CallTaiphi", CallTaiphi)
stateclassgraph.add_node("GenerateInstruct", GenerateInstruct)

# Define edges between nodes
stateclassgraph.add_edge("QueryExtract", "CallTaiphi")
stateclassgraph.add_edge("CallTaiphi", "GenerateInstruct")

# Set the entry and finish points of the graph
stateclassgraph.set_entry_point("QueryExtract")
stateclassgraph.set_finish_point("GenerateInstruct")

# Compile the graph into an executable application
stateclassgraph_app = stateclassgraph.compile()

inputs = {
    "messages": ["Starting ..."],
    "user_query": ["add user+query"],
    "raw_query": ["add raw+query"],
    "refined_query": ["add refined+query"],
    "taiphi_response": ["add taiphi+response"],
    "summary": ["add summary"],
    "instruction": ["add instruction"],
    "final_response": ["add final+response"]
    }

out = stateclassgraph_app.invoke(inputs)

print(out['messages'])
#print(out['messages'][-1])



