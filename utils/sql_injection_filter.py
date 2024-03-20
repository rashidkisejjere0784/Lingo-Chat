import re

def filter_sql_injection(user_input):
    sql_injection_pattern = r"[\"\'\`\;\%\-<>^\*\+={}\[\]|_()/\\\\]"
    
    filtered_input = re.sub(sql_injection_pattern, '', user_input)
    print(user_input, filtered_input)
    return filtered_input