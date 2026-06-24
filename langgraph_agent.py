from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from router_llm import choose_tool

from tools.resume_analyzer import analyze_resume
from tools.jd_matcher import match_resume_jd
from tools.skill_gap import skill_gap
from tools.interview_questions import generate_questions


class State(TypedDict):
    user_input: str
    result: str


def router(state):

    tool = choose_tool(
        state["user_input"]
    )

    print(f"\n[Router Selected] {tool}")

    return tool


def resume_node(state):

    state["result"] = analyze_resume()

    return state


def jd_node(state):

    state["result"] = match_resume_jd()

    return state


def skill_node(state):

    state["result"] = skill_gap()

    return state


def interview_node(state):

    state["result"] = generate_questions()

    return state


builder = StateGraph(State)

builder.add_node(
    "resume",
    resume_node
)

builder.add_node(
    "jd",
    jd_node
)

builder.add_node(
    "skill",
    skill_node
)

builder.add_node(
    "interview",
    interview_node
)

builder.set_conditional_entry_point(
    router
)

builder.add_edge(
    "resume",
    END
)

builder.add_edge(
    "jd",
    END
)

builder.add_edge(
    "skill",
    END
)

builder.add_edge(
    "interview",
    END
)

graph = builder.compile()


def run_agent(user_input):

    result = graph.invoke(
        {
            "user_input": user_input,
            "result": ""
        }
    )

    return result["result"]