# encoding: utf-8
""" 
main.py
Created by Christopher Bess
Copyright 2011
"""
script_description = 'Runs the main application.'
try:
    # optparse is deprecated, but I wanted broader compatibility
    from optparse import OptionParser
    parser = OptionParser(description=script_description)
    add_argument = parser.add_option
except ImportError:
    # this is here to help any future upgrades
    from argparse import ArgumentParser
    parser = ArgumentParser(description=script_description)
    add_argument = parser.add_argument
    pass

from webapp import server

def run():
    server.run()
    
if __name__ == '__main__':
    print 'app started'
    run()
    print 'app done.'