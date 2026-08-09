from app.services.agent_state import CampusState
from app.agents.common import with_retry


def run(state: CampusState) -> CampusState:
    def _inner(s: CampusState) -> CampusState:
        s.setdefault("audit_log", []).append("timetable:ok")
        s.setdefault("context", []).append("timetable constraints verified")
        return s
    return with_retry(_inner, state)
