def combine_lines(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as result:
        for line1, line2 in zip(f1, f2):
            combined_line = line1.strip() + ' ' + line2.strip() + '\n'
            result.write(combined_line)


