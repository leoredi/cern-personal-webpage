How to `ssh` into `lxplus` without typing your password
===

You need to follow a mixture of [MIT](https://kb.mit.edu/confluence/pages/viewpage.action?pageId=4981397), [this](https://computing.help.inf.ed.ac.uk/using-ssh-macos), and the official [CERN documentation](https://linux.web.cern.ch/docs/kerberos-access/#sshopts). Basically:

Modify your `~/.ssh/config` making sure it will try kerberos as well by addying instances on 
* `GSSAPIAuthentication`: try Kerberos5 authentication
* `GSSAPIDelegateCredentials`: tell the client to forward the Kerberos5 credentials to the remote side


Mine for example looks like this:
```sh
GSSAPIAuthentication yes
GSSAPIDelegateCredentials yes
UseKeychain yes
Host lphelc1a.epfl.ch
IdentityFile ~/.ssh/id_rsa_EPFL
```


Once that is done you need to configure your client, in my case a `macOS`. So I do:
```sh
kinit -f fredi@CERN.CH
```
And check with `klist -f` that I have `F` under my `FLAGS`. Check also by running
```sh
ssh -v fredi@lxplus.cern.ch klist -f\; tokens\; touch .sshtest
```
If everything worked you can now `ssh` into lxplus without typing the password everytime.

You should not use sshpass e.g. tapping like `brew install esolitos/ipa/sshpass`

Apply patches to your repo
===

This is very useful if working with old or unmerged MRs. Simply run
```sh
wget -q -O - <gitlab url>.patch | git apply -v
```

E.g.
```sh
wget https://gitlab.cern.ch/lhcb/Phys/-/merge_requests/924.patch | git apply -v
```

Set up vim on new macOs machine (relevant in 2023)
===

You will need `brew` and `iTerm2` installed.

* Install `oh-my-zsh`:
```sh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

* Install `Vim-Plug`:
```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

* Install powerline fonts using:
```sh
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts && ./install.sh
```
remove the fonts folder. Remember to change the fonts also in the settings of iTerm2.

* Modify your `.vimrc` to include:
```
call plug#begin('~/.vim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'joshdick/onedark.vim'
call plug#end()
let g:airline_powerline_fonts = 1
colorscheme onedark
syntax on
set number
highlight Normal ctermbg=None
highlight LineNr ctermfg=DarkGrey
```
Close, open and type: `:PlugInstall`

