#!/usr/bin/env python

import os
from pprint import pprint

vc_httptest = "0.0.0.0:443"
vc_opt = "vcsim"

if os.environ.get('type') is not None:
    if os.environ['type'] == "esxi":
        vc_opt += ' -esx'

if os.environ.get('virtualmachine') is not None:
    vc_opt += " -vm " + os.environ['virtualmachine']

if os.environ.get('host') is not None:
    vc_opt += " -vm " + os.environ['host']

if os.environ.get('datacenter') is not None:
    vc_opt += " -host " + os.environ['datacenter']

if os.environ.get('cluster') is not None:
    vc_opt += " -cluster " + os.environ['cluster']

if os.environ.get('folder') is not None:
    vc_opt += " -folder " + os.environ['folder']

if os.environ.get('datastore') is not None:
    vc_opt += " -ds " + os.environ['datastore']

if os.environ.get('resourcepool') is not None:
    vc_opt += " -pool " + os.environ['resourcepool']

if os.environ.get('network') is not None:
    vc_opt += " -pg " + os.environ['network']

if os.environ.get('standalonehost') is not None:
    vc_opt += " -standalone-host " + os.environ['standalonehost']

if os.environ.get('storagecluster') is not None:
    vc_opt += " -pod " + os.environ['storagecluster']

if os.environ.get('vapp') is not None:
    vc_opt += " -app " + os.environ['vapp']

vc_opt = vc_opt + " -httptest.serve " + vc_httptest

pprint(vc_opt)

os.system(vc_opt)