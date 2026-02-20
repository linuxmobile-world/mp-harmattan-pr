import sys
REGION_CODE = sys.argv[-1]
with open(f"mp-harmattan-{REGION_CODE}-pr/DEBIAN/control", 'r') as f:
    file = f.read()
result = ''
for line in file.split("\n"):
    if line == '':
        result += '\n'
        continue
    print(line)
    linetype, command = line.split(": ", 1)
    if linetype == "Depends":
        dependencies = []
        for dependency in command.split(", "):
            if f"-{REGION_CODE}" in dependency:
                dependencies.append(dependency)
        dependencies.append("mp-harmattan-community-pr (>= 2025.0)")
        command = ", ".join(dependencies)
    result += f'{linetype}: {command}\n'
with open(f"mp-harmattan-{REGION_CODE}-pr/DEBIAN/control", 'w') as f:
    f.write(result)