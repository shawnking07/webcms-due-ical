# WEBCMS3 iCal

## UNSW WebCMS3 Due date iCal Generator

### Usage

... GET parameter ``webcms_session=YOUR_SESSIONID``

### Develop

#### description

All info on webcms is server-side rendered, resolving html xpath is the best way to grab info.

Create conda env

```shell script
conda create -f environment.yaml
```

#### Use docker

```shell script
docker build -t webcms-due-ical .
docker run -p 8080:80 --name webcms-due-ical webcms-due-ical
```

Just a simple example here.
