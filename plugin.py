from os import getenv
from sys import exit

from requests import get


def write_outputs(outputs: dict[str, str]):
    output_file = open(getenv("DRONE_OUTPUT"), "a")

    for k, v in outputs:
        output_file.write(f"{k}={v}\n")

    output_file.close()


def main(url: str):
    resp = get(url)

    resp.raise_for_status()

    return resp.text


if __name__ == "__main__":
    url = getenv("PLUGIN_URL")

    if not url:
        print("URL required")
        exit(1)

    resp = main(url)

    write_outputs({"URL": url, "RESPONSE": resp})
