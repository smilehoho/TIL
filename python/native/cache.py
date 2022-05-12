from functools import cache, lru_cache
from typing import Any
from collections import OrderedDict


def fetch_user(user_id: str) -> dict[str, Any]:
    print(f"저장소에서 {user_id} 사용자의 정보를 불러오고 있습니다.")
    return {
        "user_id": user_id,
        "email": f"{user_id}@gmail.com",
        "password": "user1234",
    }


# no cache
def get_user(user_id: str) -> dict[str, Any]:
    return fetch_user(user_id)


dict_cache = {}


def get_user_by_dict_cache(user_id: str) -> dict[str, Any]:
    if user_id not in dict_cache:
        dict_cache[user_id] = fetch_user(user_id)

    return dict_cache[user_id]


@cache
def get_user_by_cache(user_id: str) -> dict[str, Any]:
    return fetch_user(user_id)


@lru_cache
def get_user_by_lru_cache(user_id: str) -> dict[str, Any]:
    return fetch_user(user_id)


@lru_cache(maxsize=2)
def get_user_by_lru_cache2(user_id: str) -> dict[str, Any]:
    return fetch_user(user_id)


# lru_cache 따라하기
MAX_SIZE = 2
dict_lru_cache = OrderedDict()


def get_user_by_dict_lru_cache(user_id: str) -> dict[str, Any]:
    if user_id not in dict_lru_cache:
        if len(dict_lru_cache) == MAX_SIZE:
            dict_lru_cache.popitem(last=False)
        dict_lru_cache[user_id] = fetch_user(user_id)

    return dict_lru_cache[user_id]


if __name__ == "__main__":
    from random import choice

    for get_user_func in [
        get_user,
        get_user_by_dict_cache,
        get_user_by_cache,
        get_user_by_lru_cache,
        get_user_by_lru_cache2,
        get_user_by_dict_lru_cache,
    ]:
        print(f"{get_user_func.__name__:=^80}")
        for _ in range(10):
            get_user_func(choice(["David", "Joseph", "Esther"]))

        if hasattr(get_user_func, "cache_info"):
            print(get_user_func.cache_info())
