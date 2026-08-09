from typing import TypedDict, List


class CampusState(TypedDict, total=False):
    student_id: int
    query: str
    context: List[str]
    risk_score: float
    debate_notes: List[str]
    notifications: List[str]
    audit_log: List[str]
