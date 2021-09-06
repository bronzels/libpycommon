#!/bin/bash
repo_name='libpycommon'
echo repo_name:${repo_name}
rev=`cat _version.py |awk -F \' '{print \$2}'`
echo rev:${rev}
files="/x/${repo_name}-${rev}*"
echo files:${files}
if ls ${files}  1> /dev/null 2>&1; then
rm -f ${files}
fi

python setup.py sdist bdist_wheel
twine upload --repository-url http://pypi-dev.my.org:18180 --username pypiadmin --password pypiadmin123 dist/*

rm -rf build
rm -rf dist

#windows
#参考https://blog.51cto.com/ixdba/920290，安装nfs支持包
#cmd
#showmount -e 192.168.0.62
#mount \\192.168.0.62\data\cdhdata1\bigopera\pypi\codekoala-dev x:\