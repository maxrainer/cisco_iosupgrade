# (c) 2019, Markus Rainer <markus.rainer@nts.eu>
#
# Filter 
# this plugin takes 2 parameters: ignorelist and platform
#
# do not delete these two files:
# grz-dev-sw1# show boot | include BOOT path-list
# BOOT path-list      : flash:/c3560c405ex-universalk9-mz.152-2.E9/c3560c405ex-universalk9-mz.152-2.E9.bin
# grz-dev-sw1#sh ver | inc System image          
# System image file is "flash:c3560c405ex-universalk9-mz.152-2.E6.bin"
# grz-dev-sw1#
#
import re
from ansible.errors import AnsibleError, AnsibleFilterError

def _platform_check(file, platform):
    if re.match("^" + platform + ".*", file):
        return True
    return False

# cut flash[zahl]: and subdirectories
def _cut_ignorelist_directory(ignorelist):
    res = []
    for ignore in ignorelist:
        r1 = re.split(".*flash.?:/?",ignore)
        if not isinstance(r1, list) or len(r1) < 2:
            raise AnsibleFilterError("Unexpected IgnoreList match. Check show version and show boot output.")
        r2 = re.split("/",r1[1])
        res.append(r2[0])
    return res

# is file matching to ignorenlist 
# only the beginning must match 
# so we include ending .bin and subdirectories
def _ignorelist_check(file, ignorelist):
    for ignore_entry in ignorelist: 
        if re.match("^" + ignore_entry + ".*", file):
            return False
    return True

def cleanfile(filelist, ignorelist, platform):
    if not filelist or not ignorelist or not platform:
        raise AnsibleFilterError('FileList, IgnoreList, Platform must not be empty.')
    if not isinstance(filelist, list):
        raise AnsibleFilterError('FileList must be an array')
    if not isinstance(ignorelist, list):
        raise AnsibleFilterError('IgnoreList must be an array')

    result = []
    ignorelist_cutted = _cut_ignorelist_directory(ignorelist)

    for line in filelist:
        regex = r"[^ ]*$"
        matches = re.search(regex, line)
        filematch = matches.group()
        if _platform_check(filematch, platform):
            if _ignorelist_check(filematch, ignorelist_cutted):
               result.append(filematch)
    return result

class FilterModule(object):
    ''' Clean File filters '''

    def filters(self):
        return {
            'cleanfile': cleanfile,
        }