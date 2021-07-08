FROM gitpod/workspace-postgres

USER gitpod

# Update packages
RUN sudo apt-get update -y
