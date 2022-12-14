from typing import List, Literal


RaidState = Literal[
    "need_init",
    "initing",
    "need_recon",
    "reconstructing",
    "need_restripe",
    "restriping",
    "online",
    "offline",
    "degraded"
]


def raid_progresses(state: List[RaidState]) -> List[str]:
    res = []
    if "need_init" in state or "initing" in state:
        res.append("init_progress")
    if "need_recon" in state or "reconstructing" in state:
        res.append("recon_progress")
    if "need_restripe" in state or "restriping" in state:
        res.append("restripe_progress")
    return res
