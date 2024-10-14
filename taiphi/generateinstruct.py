from langgraph.graph import AgentState

def GenerateInstruct(state: AgentState) -> AgentState:
    """
    Generate instructions based on the current state.

    This function adds two messages to the state's message list:
    1. The name of the function itself
    2. A placeholder message indicating that a user query should be added

    Args:
        state (AgentState): The current state of the agent, containing information
                            such as messages and other relevant data.

    Returns:
        AgentState: The updated state with new messages appended to the message list.

    Note:
        This function is a placeholder and should be expanded to include actual
        instruction generation logic based on the user's query and the current state.
    """
    state["messages"].append(GenerateInstruct.__name__)
    state["messages"].append("add user+query")
    return state

