#!/bin/bash

ANKI_ADDONS_FOLDER="$HOME/.local/share/Anki2/addons21"
ADDON_FOLDER_NAME="anki-github-markdown-development"

display_help_message () {
    cat << EOM

NAME
    development.sh - Set a development environment for anki-github-markdown

DESCRIPTION
    -h, --help      Display help message
    -d, --delete    Delete addon development folder from the anki app

EOM
}

delete_addon_folder () {
    printf "Deleting addon folder...\n"
    rm -rf "$ANKI_ADDONS_FOLDER/$ADDON_FOLDER_NAME"
}

create_symlink () {
    printf "Creating symlink to anki folder...\n"
    ln -s "$PWD/src/" "$ANKI_ADDONS_FOLDER/$ADDON_FOLDER_NAME"
}

main () {
    case "$1" in
        -h|--help)
            display_help_message
            exit 0
            ;;
        -d|--delete)
            delete_addon_folder
            exit 0
            ;;
        *)
            if [ -z "$1" ]; then
                create_symlink
                exit 0
            fi

            printf "Invalid argument: $1"
            exit 1
            ;;
    esac
}

main "$@"
