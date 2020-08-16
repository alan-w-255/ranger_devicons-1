#!/usr/bin/python
# coding=UTF-8
# These glyphs, and the mapping of file extensions to glyphs
# has been copied from the vimscript code that is present in
# https://github.com/ryanoasis/vim-devicons
import re;
import os;

# all those glyphs will show as weird squares if you don't have the correct patched font
# My advice is to use NerdFonts which can be found here:
# https://github.com/ryanoasis/nerd-fonts
file_node_extensions = {
    '7z'       : '',
    'a'        : '',
    'ai'       : '',
    'apk'      : '',
    'asm'      : '',
    'asp'      : '',
    'aup'      : '',
    'avi'      : '',
    'bat'      : '',
    'bmp'      : '',
    'bz2'      : '',
    'c'        : '',
    'c++'      : '',
    'cab'      : '',
    'cbr'      : '',
    'cbz'      : '',
    'cc'       : '',
    'class'    : '',
    'clj'      : '',
    'cljc'     : '',
    'cljs'     : '',
    'cmake'    : '',
    'coffee'   : '',
    'conf'     : '',
    'cfg'      : '',
    'cp'       : '',
    'cpio'     : '',
    'cpp'      : '',
    'cs'       : '',
    'css'      : '',
    'cue'      : '',
    'cvs'      : '',
    'cxx'      : '',
    'd'        : '',
    'dart'     : '',
    'db'       : '',
    'deb'      : '',
    'diff'     : '',
    'dll'      : '',
    'doc'      : '',
    'docx'     : '',
    'dump'     : '',
    'edn'      : '',
    'efi'      : '',
    'ejs'      : '',
    'elf'      : '',
    'elm'      : '',
    'epub'     : '',
    'erl'      : '',
    'ex'       : '',
    'exe'      : '',
    'exs'      : '',
    'eex'      : '',
    'f#'       : '',
    'fifo'     : '|',
    'fish'     : '',
    'flac'     : '',
    'flv'      : '',
    'fs'       : '',
    'fsi'      : '',
    'fsscript' : '',
    'fsx'      : '',
    'gem'      : '',
    'gif'      : '',
    'go'       : '',
    'gz'       : '',
    'gzip'     : '',
    'h'        : '',
    'hbs'      : '',
    'hpp'      : '',
    'hrl'      : '',
    'hs'       : '',
    'htaccess' : '',
    'htpasswd' : '',
    'htm'      : '',
    'html'     : '',
    'ico'      : '',
    'img'      : '',
    'ini'      : '',
    'iso'      : '',
    'jar'      : '',
    'java'     : '',
    'jl'       : '',
    'jpeg'     : '',
    'jpg'      : '',
    'js'       : '',
    'json'     : '',
    'jsx'      : '',
    'key'      : '',
    'less'     : '',
    'lha'      : '',
    'lhs'      : '',
    'log'      : '',
    'lua'      : '',
    'lzh'      : '',
    'lzma'     : '',
    'm4a'      : '',
    'm4v'      : '',
    'markdown' : '',
    'md'       : '',
    'mkv'      : '',
    'ml'       : 'λ',
    'mli'      : 'λ',
    'mov'      : '',
    'mp3'      : '',
    'mp4'      : '',
    'mpeg'     : '',
    'mpg'      : '',
    'msi'      : '',
    'mustache' : '',
    'o'        : '',
    'ogg'      : '',
    'pdf'      : '',
    'php'      : '',
    'pl'       : '',
    'pm'       : '',
    'png'      : '',
    'pub'      : '',
    'ppt'      : '',
    'pptx'     : '',
    'psb'      : '',
    'psd'      : '',
    'py'       : '',
    'pyc'      : '',
    'pyd'      : '',
    'pyo'      : '',
    'rar'      : '',
    'rb'       : '',
    'rc'       : '',
    'rlib'     : '',
    'rom'      : '',
    'rpm'      : '',
    'rs'       : '',
    'rss'      : '',
    'rtf'      : '',
    's'        : '',
    'so'       : '',
    'scala'    : '',
    'scss'     : '',
    'sh'       : '',
    'slim'     : '',
    'sln'      : '',
    'sql'      : '',
    'styl'     : '',
    'suo'      : '',
    't'        : '',
    'tar'      : '',
    'tgz'      : '',
    'ts'       : '',
    'twig'     : '',
    'vim'      : '',
    'vimrc'    : '',
    'wav'      : '',
    'webm'     : '',
    'xbps'     : '',
    'xhtml'    : '',
    'xls'      : '',
    'xlsx'     : '',
    'xml'      : '',
    'xul'      : '',
    'xz'       : '',
    'yaml'     : '',
    'yml'      : '',
    'zip'      : '',
    'tscn'     : '',
    'gd'       : '',
}

dir_node_exact_matches = {
# English
    '.git'                             : '',
    'Desktop'                          : '',
    'Documents'                        : '',
    'Downloads'                        : '',
    'Dotfiles'                         : '',
    'Dropbox'                          : '',
    'Music'                            : '',
    'Pictures'                         : '',
    'Public'                           : '',
    'Templates'                        : '',
    'Videos'                           : '',
# Spanish
    'Escritorio'                       : '',
    'Documentos'                       : '',
    'Descargas'                        : '',
    'Música'                           : '',
    'Imágenes'                         : '',
    'Público'                          : '',
    'Plantillas'                       : '',
    'Vídeos'                           : '',
# French
    'Bureau'                           : '',
    'Documents'                        : '',
    'Images'                           : '',
    'Musique'                          : '',
    'Publique'                         : '',
    'Téléchargements'                  : '',
    'Vidéos'                           : '',
# Portuguese
    'Documentos'                       : '',
    'Imagens'                          : '',
    'Modelos'                          : '',
    'Música'                           : '',
    'Público'                          : '',
    'Vídeos'                           : '',
    'Área de trabalho'                 : '',
# Italian
    'Documenti'                        : '',
    'Immagini'                         : '',
    'Modelli'                          : '',
    'Musica'                           : '',
    'Pubblici'                         : '',
    'Scaricati'                        : '',
    'Scrivania'                        : '',
    'Video'                            : '',
# German
    'Bilder'                           : '',
    'Dokumente'                        : '',
    'Musik'                            : '',
    'Schreibtisch'                     : '',
    'Vorlagen'                         : '',
    'Öffentlich'                       : '',
# Hungarian
    'Dokumentumok'                     : '',
    'Képek'                            : '',
    'Modelli'                          : '',
    'Zene'                             : '',
    'Letöltések'                       : '',
    'Számítógép'                       : '',
    'Videók'                           : '',
}

file_node_exact_matches = {
    '.Xauthority'                      : '',
    '.Xdefaults'                       : '',
    '.Xresources'                      : '',
    '.bash_aliases'                    : '',
    '.bashprofile'                     : '',
    '.bash_profile'                    : '',
    '.bash_logout'                     : '',
    '.bash_history'                    : '',
    '.bashrc'                          : '',
    '.dmrc'                            : '',
    '.DS_Store'                        : '',
    '.fasd'                            : '',
    '.fehbg'                           : '',
    '.gitconfig'                       : '',
    '.gitattributes'                   : '',
    '.gitignore'                       : '',
    '.inputrc'                         : '',
    '.jack-settings'                   : '',
    '.mime.types'                      : '',
    '.nvidia-settings-rc'              : '',
    '.pam_environment'                 : '',
    '.profile'                         : '',
    '.recently-used'                   : '',
    '.selected_editor'                 : '',
    '.vim'                             : '',
    '.vimrc'                           : '',
    '.viminfo'                         : '',
    '.xinitrc'                         : '',
    '.xinputrc'                        : '',
    'config'                           : '',
    'Dockerfile'                       : '',
    'docker-compose.yml'               : '',
    'dropbox'                          : '',
    'exact-match-case-sensitive-1.txt' : 'X1',
    'exact-match-case-sensitive-2'     : 'X2',
    'favicon.ico'                      : '',
    'a.out'                            : '',
    'bspwmrc'                          : '',
    'sxhkdrc'                          : '',
    'Makefile'                         : '',
    'Makefile.in'                      : '',
    'Makefile.ac'                      : '',
    'config.mk'                        : '',
    'config.m4'                        : '',
    'config.ac'                        : '',
    'configure'                        : '',
    'Rakefile'                         : '',
    'gruntfile.coffee'                 : '',
    'gruntfile.js'                     : '',
    'gruntfile.ls'                     : '',
    'gulpfile.coffee'                  : '',
    'gulpfile.js'                      : '',
    'gulpfile.ls'                      : '',
    'ini'                              : '',
    'ledger'                           : '',
    'package.json'                     : '',
    'package-lock.json'                : '',
    '.ncmpcpp'                         : '',
    'playlists'                        : '',
    'known_hosts'                      : '',
    'authorized_keys'                  : '',
    'license'                          : '',
    'LICENSE.md'                       : '',
    'LICENSE'                          : '',
    'LICENSE.txt'                      : '',
    'mimeapps.list'                    : '',
    'node_modules'                     : '',
    'procfile'                         : '',
    'react.jsx'                        : '',
    'README.rst'                       : '',
    'README.md'                        : '',
    'README.markdown'                  : '',
    'README'                           : '',
    'README.txt'                       : '',
    'user-dirs.dirs'                   : '',
    'webpack.config.js'                : '',
}

def devicon(file):
  if file.is_directory: return dir_node_exact_matches.get(file.relative_path, '')
  return file_node_exact_matches.get(os.path.basename(file.relative_path), file_node_extensions.get(file.extension, ''))
