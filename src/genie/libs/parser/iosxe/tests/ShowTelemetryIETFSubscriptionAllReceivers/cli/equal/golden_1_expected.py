expected_output = {
    101: {
        'grpc-tcp': {
            'connection': 0,
            'explanation': 'Resolution request in progress',
            'state': 'Resolving'
        },
        'grpc-tls': {
            'connection': 0,
            'explanation': 'Receiver invalid',
            'state': 'Disconnected'
        }
    },
    102: {
        'grpc-tcp://5.34.15.224:57846': {
            'connection': 0,
            'explanation': 'Receiver does not exist',
            'state': 'Disconnected'
        }
    }
}