from app.services.agent_state import CampusState
from app.agents.common import with_retry


def run(state: CampusState) -> CampusState:
    def _inner(s: CampusState) -> CampusState:
        s.setdefault("audit_log", []).append("notification:ok")
        s.setdefault("context", []).append("notifications drafted")
        return s
    return with_retry(_inner, state)
