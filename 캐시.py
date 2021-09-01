def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cities = [city.lower() for city in cities]
    cache = []
    time = 0
    for city in cities:
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache = cache[1:] + [city]
            time += 5
        else:
            cache.remove(city)
            cache.append(city)
            time += 1
    return time