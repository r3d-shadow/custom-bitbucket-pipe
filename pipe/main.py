from bitbucket_pipes_toolkit import Pipe, get_logger
import os

logger = get_logger()
PIPE_METADATA_FILE=f'{os.environ["WORKDIR"]}/pipe.yml'

schema = {
    'NAME': {'type': 'string', 'required': True},
    'MESSAGE': {'type': 'string', 'required': True},
}

class Greet(Pipe):
    def run(self):
        super().run()
        logger.info('Starting Greet...')

        name = self.get_variable('NAME').strip('"')
        message = self.get_variable('MESSAGE').strip('"')
        print(f"Hello, {name}! {message}")

if __name__ == '__main__':
    pipe = Greet(pipe_metadata=PIPE_METADATA_FILE, schema=schema)
    pipe.run()