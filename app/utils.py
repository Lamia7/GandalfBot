"""Contains utilitary functions that we will use to transform data
before sending it to JS (front)"""


def change_to_upper(text):
    return {
        "text-original": text,
        "text-changed": text.upper()
    }
