from app.services.agent_state import CampusState


def with_retry(handler, state: CampusState, retries: int = 2):
    last_exc = None
    for _ in range(retries + 1):
        try:
            return handler(state)
        except Exception as exc:
            last_exc = exc
    state.setdefault("audit_log", []).append(f"agent_error:{last_exc}")
    return state
