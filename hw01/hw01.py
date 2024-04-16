def total_salary(path: str) -> tuple[int, int]:
    sum_salary = 0
    with open(path, 'r') as fh:
        lines = [el.strip() for el in fh.readlines()]
        for line in lines:
            sum_salary += int(line.split(',')[1])
        mid_salary = sum_salary // len(lines)
    return sum_salary, mid_salary


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
