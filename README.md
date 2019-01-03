# vCenter and ESXi API based simulator

This project bundles [govcsim](https://www.virtuallyghetto.com/2017/04/govcsim-neat-incubation-project-vcenter-server-esxi-api-based-simulator.html) which is a vCenter Server and ESXi API based simulator written using govmomi (vSphere SDK for Go) into an easy to use Docker Container. This is a slight enhancement to the original work by [Brian Burke](https://www.twitter.com/brianbunke) which can be found [here](https://github.com/nimmis/docker-vcsim)

## Building the simulator from source

	docker build -t lamw/govcsim .

## Pulling the simulator from Dockerhub

	docker pull lamw/govcsim

## Running the simulator

The simulator can simulate either a vCenter server or an ESXi server, starting it with default values
assumes vCenter server.

### Start it with default settings as a vCenter server

	docker run --rm -d -p 443:443 lamw/govcsim

### Start it as a vCenter server passing in configuration file `vcenter-vcsim.conf`:

```
type=vcenter
virtualmachine=20
host=30
datacenter=2
cluster=3
folder=5
datastore=6
resourcepool=7
network=8
standalonehost=9
storagecluster=10
vapp=11
```

**Note:** The filename of the VC Sim configuration file can be named anything you want

	docker run --rm -d -p 443:443 --env-file vcenter-vcsim.conf lamw/govcsim

### Run simulator as a ESXi server passing in configuration file `esxi-vcsim.conf`:

```
type=esxi
virtualmachine=20
datastore=6
resourcepool=7
network=8
```

Start it as a ESXi server passing in configuration file `esxi-vcsim.conf`:

	docker run --rm -d -p 443:443 --env-file esxi-vcsim.conf lamw/govcsim

## Stoping the simulator

### Search for Docker Container ID:
	docker ps

### stopping the Docker Container:

	docker stop [PID]