def get_cats_info(path) -> list[dict]:
    cats_info = []
    with open(path, 'r') as fh:
        lines = [el.strip() for el in fh.readlines()]
        for line in lines:
            cats_info.append({
                'id': line.split(',')[0],
                'name': line.split(',')[1],
                'age': line.split(',')[2]
            })
    return cats_info


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
