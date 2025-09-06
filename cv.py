import tomllib
import jinja2
from enum import Enum
from typing import Dict, Any
from datetime import date


def render_dates(data: Dict[str, Any]):
    def helper(data: Any):
        if isinstance(data, date):
            return data.strftime("%m.%Y")
        elif isinstance(data, list):
            return [helper(x) for x in data]
        elif isinstance(data, dict):
            return render_dates(data)
        return data

    return {k: helper(v) for k, v in data.items()}


with open("cv.toml", "rb") as f:
    data = tomllib.load(f)

data = render_dates(data)

env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
template = env.get_template("cv.html")
html = template.render(**data)

with open("cv-out.html", "w") as f:
    f.write(html)
