from dotenv import load_dotenv, find_dotenv
import os

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    return os.getenv("OPENAI_API_KEY")

def get_serper_api_key():
    load_env()
    return os.getenv("SERPER_API_KEY")

def pretty_print_result(result):
    parsed = []
    for line in result.split('\\n'):
        if len(line) > 80:
            words = line.split()
            newline = ''
            for word in words:
                if len(newline) + len(word) + 1 > 80:
                    parsed.append(newline)
                    newline = word
                else:
                    newline += ' ' + word if newline else word
            parsed.append(newline)
        else:
            parsed.append(line)
    return '\\n'.join(parsed)
