FROM ubuntu:latest

RUN apt update && apt install -y vim wget curl git tmux htop mc
RUN apt install -y python3 python3-pip python3-venv

WORKDIR /home/aleksei

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -t robbyrussell \
    -p https://github.com/zsh-users/zsh-autosuggestions
ENV ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#dedede,bg=#9c9c9c,bold,underline"
ENTRYPOINT ["zsh"]
