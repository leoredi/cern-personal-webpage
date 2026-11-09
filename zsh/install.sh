#!/bin/sh
# One-shot install for macOS or Ubuntu. Backs up anything it overwrites.
# Run with plain sh: on a fresh Ubuntu zsh is not there yet.
set -e
cd "$(dirname "$0")"
case "$(uname)" in
  Darwin)
    # zsh and vim ship with macOS; plugins are optional eye candy
    if command -v brew >/dev/null; then
      brew install zsh-autosuggestions zsh-syntax-highlighting
      # make Homebrew visible to agents that use bash (Claude Code often does)
      grep -q 'brew shellenv' "$HOME/.bash_profile" 2>/dev/null ||
        echo "eval \"\$($(command -v brew) shellenv)\"" >> "$HOME/.bash_profile"
    fi ;;
  Linux)
    sudo apt-get install -y zsh vim zsh-autosuggestions zsh-syntax-highlighting
    [ "$(getent passwd "$USER" | cut -d: -f7)" = /usr/bin/zsh ] ||
      chsh -s /usr/bin/zsh ;;
esac
for f in zshenv zprofile zshrc; do
  [ -e "$HOME/.$f" ] && mv "$HOME/.$f" "$HOME/.$f.bak.$(date +%Y%m%d%H%M%S)"
  cp "$f" "$HOME/.$f"
done
# refresh completion cache
rm -f "$HOME/.zcompdump"*
echo "Done. Log out and in (Linux) or open a new terminal, or: exec zsh"
