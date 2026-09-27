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
