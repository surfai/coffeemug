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
from state import AgentState

class AgentState(TypedDict):
    """
    Represents the state of the agent throughout its execution.

    This TypedDict defines the structure of the agent's state, including
    various fields that are updated and accessed during the agent's operation.

    Attributes:
        messages (Sequence[str]): A list of messages in the conversation.
        summary (Sequence[str]): A list of summaries generated during the process.
        instruction (Sequence[str]): A list of instructions for the agent.
        taipi_body (Sequence[str]): The body of the Taiphi response.
        user_raw_query (Sequence[str]): The original, unprocessed user query.
        user_refined_query (Sequence[str]): The processed and refined user query.
        parameters_to_taiphi (Sequence[str]): Parameters to be passed to Taiphi.

    Note:
        All attributes are annotated with `operator.add`, indicating that
        they can be concatenated or added together when updating the state.
    """
    messages: Annotated[Sequence[str], operator.add]
    summary: Annotated[Sequence[str], operator.add]
    instruction: Annotated[Sequence[str], operator.add]
    taipi_body: Annotated[Sequence[str], operator.add]
    user_raw_query: Annotated[Sequence[str], operator.add]
    user_refined_query: Annotated[Sequence[str], operator.add]
    parameters_to_taiphi: Annotated[Sequence[str], operator.add]

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
stateclassgraph.set_finish_point("StateFunction2")

# Compile the graph into an executable application
stateclassgraph_app = stateclassgraph.compile()

"""
The `stateclassgraph_app` is the compiled version of the state graph,
ready to be executed. It represents the full workflow of the Taiphi agent,
from query extraction to instruction generation.
"""
