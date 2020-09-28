# WEBCMS3 iCal

## UNSW WebCMS3 Due date iCal Generator

### Usage

- ... GET parameter ``webcms_session=YOUR_SESSIONID``

- docker on your own server

  ```shell script
  docker run -p 80:80 --name webcms-due-ical ghcr.io/shawnking07/webcms-due-ical:latest
  ```


### Development

#### description

All info on webcms is server-side rendered, resolving html xpath is the best way to grab info.

Create conda env

```shell script
conda create -f environment.yaml
```
