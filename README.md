# Python API to Store Contact

[![Instagram](https://img.shields.io/badge/Instagram-profile-orange)](https://www.instagram.com/anish.araz/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-profile-blue)](https://www.linkedin.com/in/anish-araz-009b02258/)

## Discription

<hr>

**The Api can store Name,Contact,Address In Database.<br>It comes with build source code of docker Fully customizable <br> It can perform _GET/POST/PUT/DELETE_ Operation<br>I is based on [FastAPI](https://fastapi.tiangolo.com/)<br>Installation is _simple_ It si based on [docker-compose](https://docs.docker.com/compose/) so _OneClick_ Implementation**

#### !! NOTE : Your host network CIDR can Conflict with docker network so accordingly change the <br> - subnet in compose network <br> - ipv4 address of containers <br> <br> For E.g 10.0.0.1/24 (default in this example) , 12.0.0.1/24 , 192.168.10.1/24

## API Request and Responce

<hr>

The request and responce format is straight and consistent

> **# Post Request** <br>
> You can make post request passing 3 Parameters<br><br>The responce body will be json like.<br> > **E.g Request : http://<!---->10.0.0.2:8000/<!---->?name=mike&phone_num=+977985\*\*\*\*\*&addr=nepal**
>
> ```json
> {
>   "success": true,
>   "responce": {
>     "id": 1
>   }
> }
> ```
>
> <br>

> **# Get Request** <br>
> You can make Get request passing ID as Parameter<br><br>The responce body will be json like.<br> > **E.g Request : http://<!---->10.0.0.2:8000/<!---->?id=user_id**
>
> ```json
> {
>   "success": true,
>   "responce": {
>     "name": "mike",
>     "contact": "+977985******",
>     "addr": "nepal"
>   }
> }
> ```
>
> <br>

> **# PUT Request** <br>
> You can make PUT request passing parameter name and value to Update along with ID of user<br><br>The responce body will be json like.<br>**E.g Request : http://<!---->10.0.0.2:8000/<!---->?id=id_of_username=name_to_update&phone_num=num_to_update&addr=address_to_update**
>
> ```json
> {
>   "success": true,
>   "responce": "Updated ID 1"
> }
> ```
>
> Again GET request gives
>
> ```json
> {
>   "success": true,
>   "responce": {
>     "name": "updated_name",
>     "contact": "updated_number",
>     "addr": "updated_address"
>   }
> }
> ```
>
> <br>

> **# Delete Request** <br>
> You can make Delete request passing ID as Parameter which will delete the record with given ID<br><br>The responce body will be json like.<br> > **E.g Request : http://<!---->10.0.0.2:8000/<!---->?id=user_id_to_delete**
>
> ```json
> {
>   "success": true,
>   "responce": "Removed ID 1"
> }
> ```
>
> Again Get Request for deleted id
>
> ```json
> {
>   "success": false,
>   "reason": "User Not found"
> }
> ```

## Installation

<hr>

It is based on [Docker](https://www.docker.com/) and [Docker-compose](https://docs.docker.com/compose/) Which comes with Persistent Volume No Data Loss<br><br>
**Check Installation**

```bash
# Shell Commands
> docker -v
> docker-compose -v
```

**Api Installation**

```bash
> git clone url_
> cd dir
> docker-compose up -d
```

**The default CIDR in Docker-compose Network is 10.0.0.1/24 db is on 10.0.0.3 and app is on _10.0.0.2_ So You can access your api now on http://10.0.0.3/ using any api client eg. Browser, [Insomnia](https://insomnia.rest/)**
