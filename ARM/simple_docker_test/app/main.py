import logging
import subprocess
import shlex
import sys

log = "/app/logs/docker.log"

logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('testing arm docker image deployment')

#az_resource_grp = sys.argv[1]
#az_vm_name = sys.argv[2]

#print(az_resource_grp)
#print(az_vm_name)

subprocess.call(shlex.split('bash deallocate_vm.sh'))
