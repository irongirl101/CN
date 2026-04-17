# Computer Networks - Socket Programming Project

## Online Music Streaming Service 
The client sends a request to the server to play music from various categories. The server then streams audio data over a TCP connection, allowing the client to receive and play the music in real time.

### Project Expectations 
- Multiclient Setup
- Adaptive Bitrate Streaming
- Categorization
- Buffer Management

## Requirements 
- Client and Sever set up, both on the same network (local network).
- Python 3.12.x
- songs on the server that can be accessed (note that this is very much system specific. File location changes depending on system). (songs are too massive to be uploaded onto github.)


### Modules 
- socket (built-in)
- subprocess (built-in)
- queue (built-in)
- threading (built-in)
- time (built-in)
- os (built-in)
- ffplay (client only)
  ```
  # For Windows 
  https://github.com/oop7/ffmpeg-install-guide
  ```
  ```
  # For MacOS
  brew install ffmpeg
  ```
  ```
  # For Linux - use your package manager
  sudo apt install ffmpeg
  ```
  ```
  # download ffplay
  pip install ffmpeg-python
  ```

## Setup 
- Use main_client.py and main_server.py 
- Get ip of server using and add it to client.py
  ```
  #Windows
  ipconfig 
  ```
  ```
  # MacOS
  ipconfig getifaddr en0
  ```
  ```
  #Linux
  ip addr
  ```
- Run on server machine first 
  ```
  python main_server.py
  ```
- Run on client machine
  ```
  python main_client.py
  ```
- Client uses interface to play songs. 

## Images of Execution 


## Project handeled by 
### Aditi Vignesh - PES1UG24CS023
### Piya Banerjee - PES1UG25CS830

