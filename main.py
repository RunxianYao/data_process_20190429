# -*- coding: utf-8 -*-

import sys
import getopt
from util.redisutil import RedisResource


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            RedisResource.set("test1","33333333333333333333333333333333333333333333333333333333333333")
            v1 = RedisResource.get("test1")
            print v1
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())