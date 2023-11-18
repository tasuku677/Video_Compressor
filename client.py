import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '0.0.0.0'
server_port = 9001

command = input("input a command")
if command == "ffmpeg -i video.mp4":
    pass
elif command == "ffmpeg -i video.mp4 video.avi":
    pass
elif command == "ffmpeg -i video.flv video.mpeg":
    pass
elif command == "ffmpeg -i input.mp4 -vn output.mp3":
    pass
elif 

exec(command)
