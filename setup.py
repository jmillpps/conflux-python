from distutils.core import setup
setup(
  name = 'conflux-python',         # How you named your package folder (MyLib)
  packages = ['conflux-python'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'python-based implementation of Conflux protocol',   # Give a short description about your library
  author = 'Justin Miller',                   # Type in your name
  author_email = 'jmillpps@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jmillpps/conflux-python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jmillpps/conflux-python/v_02.tar.gz',    # I explain this later on
  keywords = ['Conflux'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'hashlib',
          'ecdsa',
          'Crypto.Hash',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
