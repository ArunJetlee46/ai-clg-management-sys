from app.services.agent_state import CampusState
from app.agents.common import with_retry


def run(state: CampusState) -> CampusState:
    def _inner(s: CampusState) -> CampusState:
        s.setdefault("audit_log", []).append("faculty_assistant:ok")
        s.setdefault("context", []).append("faculty task assistance prepared")
        return s
    return with_retry(_inner, state)
