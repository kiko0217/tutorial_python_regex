#!/bin/bash

check_os(){
    case "$OSTYPE" in
        solaris*) echo "SOLARIS" ;;
        darwin*) echo "OSX" ;;
        linux*) echo "LINUX" ;;
        bsd*) echo "BSD" ;;
        msys*) echo "WINDOWS" ;;
        cygwin*) echo "WINDOWS" ;;
        *) echo "unknown: $OSTYPE" ;;
    esac
}

os_type=$(check_os)
create_venv(){
    echo create env
    if [ os_type == "WINDOWS" ]; then
        conda.bat activate base
    elif [ os_type == "LINUX" ]; then
        conda activate base
    else
        conda activate base
    fi
    python -m venv env
}
activate_env() {
    echo activate env
    source env/bin/activate
}
[[ $os_type != "WINDOWS" && $os_type != "LUNUX" ]] && exit 1;
[[ "$VIRTUAL_ENV" == "" ]]; INVENV=$?
[[ $INVENV == 0 && ! -d env ]] && create_venv
[[ $INVENV == 0 ]] && activate_env
pip install -r requirements.txt