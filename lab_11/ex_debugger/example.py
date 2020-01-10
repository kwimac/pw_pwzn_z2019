import util

filename = __file__
import pdb; pdb.set_trace()  # Ustawienie kursora debuggera
filename_path = util.get_path(filename)
print(f'path = {filename_path}')
