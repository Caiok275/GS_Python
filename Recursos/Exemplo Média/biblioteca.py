def media_lista(num) -> float:

    if len(num) == 0:
        return 0
    return sum(num) / len(num)