from distutils.core import setup
setup(
  name = 'EtherBlockchain',
  packages = ['blockchain', 'libs'],
  version = '0.1',
  license='MIT',
  description = 'Ethereum Blockchain Ecosystem Api (Polygon, Bsc and other)',
  author = 'Qiuby Zhukhi',
  author_email = 'qzhukhi@gmail.com',
  url = 'https://github.com/QiubyZ/EtherBlock',
  keywords = ['Python Ethereum Block Chain', 'Binance smartchain api python', 'Polygon Blockchain api python'],
  install_requires=[
          'requests',
          'bs4',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
