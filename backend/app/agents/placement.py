from app.services.agent_state import CampusState
from app.agents.common import with_retry


def run(state: CampusState) -> CampusState:
    def _inner(s: CampusState) -> CampusState:
        s.setdefault("audit_log", []).append("placement:ok")
        s.setdefault("context", []).append("placement insights prepared")
        return s
    return with_retry(_inner, state)
