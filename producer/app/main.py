from dal import pull_batches
from utils import send_batches_to_producer



def main():

    skip = 0
    batch_size = 30

    while True:
        users = pull_batches(skip, batch_size)

        if not users:
            continue
        
        send_batches_to_producer(users)

        skip += len(users)


if __name__ == "__main__":
    main()