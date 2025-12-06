with open('this.txt', 'r') as file:
    lines = file.readlines()
    with open('output.txt', 'w') as output_file:
        for line in lines:
            output_file.write(line)