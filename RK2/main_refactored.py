class Computer:
    def __init__(self, id: int, name: str, cost: int, display_class_id: int = None):
        self.id = id
        self.name = name
        self.threads = cost
        self.display_class_id = display_class_id


class DisplayClass:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class ComputerAndDisplayClass:
    def __init__(self, display_class_id: int, computer_id: int):
        self.display_class_id = display_class_id
        self.computer_id = computer_id


def list_computers_with_name_ending_ov(computers, display_classes, links):
    result = []
    for link in links:
        computer = next(c for c in computers if c.id == link.computer_id)
        if computer.name.endswith("n"):
            display_class = next(d for d in display_classes if d.id == link.display_class_id)
            result.append((computer.name, display_class.name))
    return result


def list_average_threads_per_display(display_classes, computers, links):
    avg_threads_per_class = []
    for display_class in display_classes:
        related_computers = [
            c for c in computers if any(l.display_class_id == display_class.id and l.computer_id == c.id for l in links)
        ]
        if related_computers:
            total_threads = sum(c.threads for c in related_computers)
            avg_threads = total_threads / len(related_computers)
            avg_threads_per_class.append((display_class.name, avg_threads))
    avg_threads_per_class.sort(key=lambda x: x[1])
    return avg_threads_per_class


def list_display_classes_starting_with_n(display_classes, computers, links):
    result = []
    for display_class in display_classes:
        if display_class.name.startswith("N"):
            related_computers = [
                c for c in computers if any(l.display_class_id == display_class.id and l.computer_id == c.id for l in links)
            ]
            computer_names = [c.name for c in related_computers]
            result.append((display_class.name, computer_names))
    return result
