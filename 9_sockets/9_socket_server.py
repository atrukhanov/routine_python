import socket


def init_server():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn, addr


def run_server(connection, address):
    try:
        print('server started...')
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.send(data.upper())
    except Exception as ex:
        connection.close()
        raise ex
    finally:
        connection.close()


def main():
    conn, addr = init_server()
    run_server(conn, addr)


if __name__ == '__main__':
    main()
