import subprocess

output = subprocess.check_output(['./crypto/dec_command_line', '512885a5bad338b6', 'abcdefabcdefabcd'])
output = str(output)[2:-1]
print(output)
for i in range(len(output)):
    if output[i] == '\\':
        output = output[:i]
        break;
print(output)

