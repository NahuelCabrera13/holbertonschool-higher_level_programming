#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        try:
            super().remove(item)
            print(f"Removed {item} from the list.")
        except ValueError:
            print(f"Item {item} not found in the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
