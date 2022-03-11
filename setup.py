import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name='dino game',
    options={'build_exe': {'packages':['pygame'],
                                    'include_files':['imagens', 'sons']}},

    executables = executables

)