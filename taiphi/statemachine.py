import operator
from typing import Annotated, Sequence, TypedDict

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