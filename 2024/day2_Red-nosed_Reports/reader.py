import os
class Reader:
    """  A class used to read data from a file."""
    def __init__(self):
        pass

    def load_data(self, filename):
        """ Loads data from a specified file. """
        try:
            script_dir = os.path.dirname(__file__)
            abs_file_path = os.path.join(script_dir, filename)
            file = open(abs_file_path, encoding='utf-8')
            entries = file.readlines()
        except Exception as e:
            print(f"Exception: {e}")
            return [""]
        else:
            return entries

    def load_int_separated_by_space(self, filename):
        """ Loads data from a specified file. """
        entries = self.load_data(filename)
        return [list(map(int, x.strip().split(" "))) for x in entries]