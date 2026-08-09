from app.services.agent_state import CampusState


def run_debate(state: CampusState) -> CampusState:
    risk = state.get("risk_score", 0.0)
    notes = state.setdefault("debate_notes", [])
    notes.append(f"placement argues risk={risk:.2f}")
    notes.append(f"analytics counters with confidence={(risk*0.8):.2f}")
    state.setdefault("audit_log", []).append("debate:completed")
    return state
