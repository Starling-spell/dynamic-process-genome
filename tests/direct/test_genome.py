def test_graph_guards(direct_vm, direct_deploy, direct_alice, direct_bob):
    c = direct_deploy("contracts/DynamicProcessGenome.py")
    direct_vm.sender = direct_alice
    c.create_process_space("ops", "Operations", "input precedes output")
    c.add_process_node("ops", "input", "input", "source")
    c.add_process_node("ops", "output", "output", "result")
    c.connect_process_nodes("ops", "input", "output", "sequence")
    assert c.get_space("ops")["version"] == 0
    with direct_vm.expect_revert("owner required"):
        with direct_vm.prank(direct_bob):
            c.add_process_node("ops", "extra", "action", "x")
    with direct_vm.expect_revert("existing sequence edge"):
        c.review_insert_step("ops", "bad", "transform", "transform", "x", "output", "input",
                             "https://example.org/spec", "0" * 64, 0, 9999999999)


def test_evidence_bound_insert(direct_vm, direct_deploy, direct_alice):
    import hashlib
    import json
    import time
    from pathlib import Path

    body = Path("examples/process-spec.txt").read_bytes()
    digest = hashlib.sha256(body).hexdigest()
    direct_vm.mock_web(r".*example\.org/spec.*", {"status": 200, "body": body.decode()})
    direct_vm.mock_llm(r".*Treat this fetched process specification.*", json.dumps({"verdict": "SAFE"}))
    c = direct_deploy("contracts/DynamicProcessGenome.py")
    direct_vm.sender = direct_alice
    c.create_process_space("ops", "Operations", "The input step must precede the output step")
    c.add_process_node("ops", "input", "input", "source")
    c.add_process_node("ops", "output", "output", "result")
    c.connect_process_nodes("ops", "input", "output", "sequence")
    c.review_insert_step("ops", "transform-1", "transform", "transform", "normalize", "input", "output",
                         "https://example.org/spec", digest, 0, int(time.time()) + 3600)
    assert c.get_space("ops")["version"] == 1
    assert '"decision":"APPLY"' in c.get_mutation("ops", "transform-1")
