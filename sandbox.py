with open("oreo.md") as f:
    lines = f.readlines()

for line in lines:
	if "oreo" not in line and "?" not in line and "---" not in line and not line == '\n' :
		print line