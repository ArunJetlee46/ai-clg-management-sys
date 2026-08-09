from app.graph import graph


def test_graph_runs():
    out = graph.invoke({"student_id": 1, "query": "help", "risk_score": 0.8})
    assert "audit_log" in out
    assert any("debate" in item for item in out["audit_log"])
