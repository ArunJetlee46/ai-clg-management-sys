from langgraph.graph import END, StateGraph

from app.services.agent_state import CampusState
from app.agents import attendance, academic_advisor, faculty_assistant, placement, exam, timetable, analytics, notification, audit_trail, debate


def route_after_analytics(state: CampusState) -> str:
    return "debate" if state.get("risk_score", 0.0) > 0.65 else "notification"


def reflection(state: CampusState) -> CampusState:
    state.setdefault("audit_log", []).append("reflection:passed")
    return state


def build_graph():
    g = StateGraph(CampusState)
    g.add_node("attendance", attendance.run)
    g.add_node("academic_advisor", academic_advisor.run)
    g.add_node("faculty_assistant", faculty_assistant.run)
    g.add_node("placement", placement.run)
    g.add_node("exam", exam.run)
    g.add_node("timetable", timetable.run)
    g.add_node("analytics", analytics.run)
    g.add_node("debate", debate.run_debate)
    g.add_node("notification", notification.run)
    g.add_node("audit_trail", audit_trail.run)
    g.add_node("reflection", reflection)

    g.set_entry_point("attendance")
    g.add_edge("attendance", "academic_advisor")
    g.add_edge("academic_advisor", "faculty_assistant")
    g.add_edge("faculty_assistant", "placement")
    g.add_edge("placement", "exam")
    g.add_edge("exam", "timetable")
    g.add_edge("timetable", "analytics")
    g.add_conditional_edges("analytics", route_after_analytics, {"debate": "debate", "notification": "notification"})
    g.add_edge("debate", "audit_trail")
    g.add_edge("notification", "audit_trail")
    g.add_edge("audit_trail", "reflection")
    g.add_edge("reflection", END)
    return g.compile()


graph = build_graph()
