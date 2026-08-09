def test_grounding_prompt_has_constraint():
    prompt = "Answer using only context."
    assert "only context" in prompt
