FROM nimmis/golang

MAINTAINER nimmis <kjell.havneskold@gmail.com>

# copy startscript
COPY docker-entrypoint.py /

# download and compile vcsim
RUN go get -u github.com/vmware/govmomi/vcsim

# default exposed port is 443
EXPOSE 443

# run start command
ENTRYPOINT ["/docker-entrypoint.py"]
