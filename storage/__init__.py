from storage.base import session_factory

if __name__ == '__main__':
    with session_factory() as session:
        print(1)
