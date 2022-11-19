
import MemSys
def filesystem():
    fs = MemSys.MemSys()
    fs.create_directory('.', "Dir_1")

    return fs
filesystem()