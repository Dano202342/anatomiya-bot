from .blood import BLOOD
from .bones import BONES
from .glands import GLANDS
from .kidney import KIDNEY
from .muscles import MUSCLES
from .nerves import NERVES
from .skin import SKIN

SECTIONS = {s["key"]: s for s in (NERVES, MUSCLES, SKIN, BONES, KIDNEY, BLOOD, GLANDS)}


def get_category(sec: str, cat: str) -> dict | None:
    s = SECTIONS.get(sec)
    if not s:
        return None
    return next((c for c in s["categories"] if c["key"] == cat), None)


def get_item(sec: str, cat: str, key: str) -> dict | None:
    c = get_category(sec, cat)
    if not c:
        return None
    return next((i for i in c["items"] if i["key"] == key), None)


def all_items():
    """(sec, cat, item) uchliklari — barcha mavzular."""
    for s in SECTIONS.values():
        for c in s["categories"]:
            for i in c["items"]:
                yield s["key"], c["key"], i
