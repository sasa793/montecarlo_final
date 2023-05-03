from setuptools import setup

setup(name= 'montecarlo',
      version= '1.0.0',
      url= 'https://github.com/sasa793/montecarlo_final',
      author= 'Sarah Elmasry',
      author_email= 'sme5qyx@virginia.edu',
      license= 'CC0-1.0 Universal',
      description= 'Monte Carlo simulator with Die, Game, and Analyzer classes to assess the outcome of random events', 
      packages = ['montecarlo'],
      install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1', 'pandas'],)