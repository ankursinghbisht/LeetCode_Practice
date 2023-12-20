class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_map = defaultdict(lambda: defaultdict(int))
        dish_set = set()

        for order in orders:
            table_number, dish = int(order[1]), order[2]
            dish_set.add(dish)
            table_map[table_number][dish] += 1

        result = []

        # Prepare headings
        headings = ["Table"] + sorted(dish_set)
        result.append(headings)

        # Fill the table
        for table_number, dish_count in sorted(table_map.items()):
            row = [str(table_number)]
            for dish in sorted(dish_set):
                row.append(str(dish_count.get(dish, 0)))
            result.append(row)

        return result