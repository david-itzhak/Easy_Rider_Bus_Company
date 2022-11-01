import re


def validate_time_format(time_string: str):
    time_pattern = '[0-2][0-9]:[0-5][0-9]$'
    match_result = re.match(time_pattern, time_string)
    return True if match_result else False


def validate_stop_name(stop_name_string: str):
    stop_name_pattern = r"[A-Z]\w+\s([A-Z]\w+\s)*(Avenue|Street|Road|Boulevard)$"
    match_result = re.match(stop_name_pattern, stop_name_string)
    return True if match_result else False
