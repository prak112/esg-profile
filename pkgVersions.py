# check and print each library status
from ast import Mod
from platform import python_version


try:
    # python
    print('python: %s' % python_version())
    # requests
    import requests
    print('requests: %s' % requests.__version__)
    # BeautifulSoup
    import bs4
    print ('BeautifulSoup: %s' % bs4.__version__)
    # lxml & html5lib
    import lxml, html5lib
    print(f"lxml: {lxml.__version__}\nhtml5lib: {html5lib.__version__}")
    # scipy
    import scipy
    print('scipy: %s' % scipy.__version__)
    # numpy
    import numpy
    print('numpy: %s' % numpy.__version__)
    # scikit-learn
    import sklearn
    print('sklearn: %s' % sklearn.__version__)
    # pandas
    import pandas
    print('pandas: %s' % pandas.__version__)
    # matplotlib
    import matplotlib
    print('matplotlib: %s' % matplotlib.__version__)
    # seaborn
    import seaborn
    print('seaborn: %s' %seaborn.__version__)
    # statsmodels
    import statsmodels
    print('statsmodels: %s' % statsmodels.__version__)

    print("\nAll Set! Good to go!")



except ModuleNotFoundError:
    print("Module/Library Not Found!")