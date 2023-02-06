def func(shirota, dolgota, coords):
    map_params = {
        "ll": ",".join([dolgota, shirota]),
        "spn": ",".join([shirota, shirota]),
        "l": "map",
        "pt": ','.join(coords.split())
    }
    return map_params
