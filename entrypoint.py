#japoromahelper.run()
"""if __name__ == '__main__':
    import japoromahelper
    japoromahelper.makrons.main()
"""
import os
from japoromahelper.makrons import main
from japoromahelper.utils import is_frozen, frozen_temp_path

if is_frozen:
    basedir = frozen_temp_path
else:
    basedir = os.path.dirname(os.path.abspath(__file__))
main(resource_dir=os.path.join(basedir, 'resources'))
