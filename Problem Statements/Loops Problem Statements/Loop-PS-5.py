log_messages=["INFO", "DEBUG", "WARNING", "ERROR", "INFO", "CRITICAL", "WARNING"] 
for log in log_messages:
    if log=="INFO":
        continue
    elif log=="WARNING" or log=="ERROR":
        print(log)
    elif log=="CRITICAL":
        break
