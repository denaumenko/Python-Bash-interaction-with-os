import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


log = " jkndckjcsnkjnsdncscks csnckjnscnkncs   cskncksncsjkn [12345]: Error"
regex = r"\[(\d+)\]"

result = re.search(regex,log)
print(result[1])
print(extract_pid(log))
log = " jkndckjcsnkjnsdncscks csnckjnscnkncs   cskncksncsjkn [cage]:"
result = re.search(regex,log)



print(extract_pid(log))

def extract_pid_with_message(log_line):
    regex = r"\[(\d+)\]: (\w*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid_with_message("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid_with_message("99 elephants in a [cage]")) # None
print(extract_pid_with_message("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid_with_message("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)