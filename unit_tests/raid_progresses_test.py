from typing import List, Any

import pytest

from src.raid_progresses import RaidState, raid_progresses


class TestRaidProgresses:
    @pytest.mark.parametrize(
        "raid_state,expected_result",
        [
            (["need_init", "need_recon", "need_restripe"], ["init_progress", "recon_progress", "restripe_progress"]),
            (["initing", "reconstructing", "restriping"], ["init_progress", "recon_progress", "restripe_progress"]),
            (["online", "degraded"], []),
            (["offline"], [])
        ]
    )
    def test_raid_progresses_with_correct_states(self, raid_state: List[RaidState], expected_result: List[str]):
        got_result = raid_progresses(raid_state)
        assert expected_result == got_result, f"Unexpected raid_progresses function result: " \
                                              f"expected {expected_result}, got {got_result}"

    @pytest.mark.parametrize(
        "raid_state",
        [
            pytest.param([], marks=pytest.mark.xfail(reason="Empty state")),
            pytest.param(["need_recon", "raid_state"],
                         marks=pytest.mark.xfail(reason="The state has a string that is not a RaidState value")),
            pytest.param(["online", 42], marks=pytest.mark.xfail(reason="The state has an incorrect type value")),
            pytest.param(("online", "degraded"), marks=pytest.mark.xfail(reason="The state is a tuple, not a list")),
            pytest.param("need_init", marks=pytest.mark.xfail(
                reason="The state is a RaidState value, not a list of RaidState values"
            )),
            pytest.param("raid_state",
                         marks=pytest.mark.xfail(reason="The state is a string that is not a RaidState value")),
            pytest.param(42, marks=pytest.mark.xfail(reason="The state has a non-string type", raises=TypeError)),
        ]
    )
    def test_raid_progresses_with_incorrect_states(self, raid_state: Any):
        raid_progresses(raid_state)
