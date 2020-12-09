from flask_caching import Cache


cache = Cache(config={'CACHE_TYPE': 'redis'})


def has(key: str) -> bool:
    return cache.cache.has(key)


cache.__setattr__('has', has)
