#!/bin/bash
echo "set ssl:verify-certificate no" > /home/lele/.lftp/rc
HOST="ftp.sigcommconfs.hosting.acm.org"
USER="sigcomm-2018@sigcommconfs.hosting.acm.org"
PASS="gSaH}arFoa~T"
FTPURL="ftp://$USER:$PASS@$HOST"
LCD="./_site"
RCD="/"
#DELETE="--delete"
DELETE=""
lftp -c "set ftp:list-options -a;
open '$FTPURL';
lcd $LCD;
cd $RCD;
mirror --reverse \
       $DELETE \
       --verbose \
#       --exclude-glob a-dir-to-exclude/ \
#       --exclude-glob a-file-to-exclude \
#       --exclude-glob a-file-group-to-exclude* \
#       --exclude-glob other-files-to-exclude"
