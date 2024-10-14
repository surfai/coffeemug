from typing import TypedDict, Annotated, Sequence
import operator

class AgentState(TypedDict):
    messages: Annotated[Sequence[str], operator.add]
    summary: Annotated[Sequence[str], operator.add]
    instruction: Annotated[Sequence[str], operator.add]
    taipi_body: Annotated[Sequence[str], operator.add]
    user_raw_query: Annotated[Sequence[str], operator.add]
    user_refined_query: Annotated[Sequence[str], operator.add]
    parameters_to_taiphi: Annotated[Sequence[str], operator.add]
