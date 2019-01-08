import socket
import subprocess

# Start a socket listening for connections on 0.0.0.0:8000
# (0.0.0.0 means all interfaces)

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connect = server_socket.accept()[0].makefile('rb')


try:
    # Run a viewer with an appropriate command line.
    cmdline = ['vlc', '--demux', 'h264', '-']
    player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

    while true:
        ''' Repeatedly read 1k of data from the connection and
        write to the media player's stdin'''
        data = connection.read(1024)

        if not data:
            break
        player.stdin.write(data)
finally:
    connection.close()
    server_socket.close()
    payer.terminate()

            
