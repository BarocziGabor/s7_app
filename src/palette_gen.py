from pathlib import Path
from typing import Literal
from palette import theme

def gen_qss_withvars(qss_file_path: Path | str, dark_or_light: Literal["dark", "light"] = "dark") -> str:
    """

    Args:
        qss_file_path (Path | str): _description_
        dark_or_light (Literal[&quot;dark&quot;, &quot;light&quot;], optional): _description_. Defaults to "dark".

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    if dark_or_light not in ["dark", "light"]:
        raise ValueError("dark_or_light must be either 'dark' or 'light'")

    qss_file_path = Path(qss_file_path)
    qss = qss_file_path.read_text()
    colors = theme[dark_or_light]

    new_lines = []
    for line in qss.splitlines():
        if line.find(r"%%") < 0:
            new_lines.append(line)
            continue
        for key, value in colors.items():
            placeholder = f"%%{key}%%"
            if placeholder in line:
                new_lines.append(line.replace(placeholder, value))
                break
       
    return "\n".join(new_lines)


