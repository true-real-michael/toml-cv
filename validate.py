import tomllib

with open("cv.toml", "rb") as f:
    try:
        data = tomllib.load(f)
        print("TOML is valid!")
        from pprint import pprint

        pprint(data)
    except tomllib.TOMLDecodeError as e:
        print(f"TOML is invalid: {e}")
