"""ZŁY KOD:
class NormalFile:
    def read(self):
        # read file implementation
        print('Reading from regular file')

    def write(self, input_text):
        # write file implementation
        print('Writing to regular file')


class ReadonlyFile(NormalFile):
    def read(self):
        # read readonly file implementation
        print('Reading from readonly file')

    def write(self):
        raise Exception('Can\'t write to readonly file')


normal_file = NormalFile()
readonly_file = ReadonlyFile()


def make_file_operations(fil, input_text):
    if not isinstance(fil, ReadonlyFile):
        fil.write(input_text)
    # some processing stuff
    fil.read()

make_file_operations(normal_file, 'tekst')
make_file_operations(readonly_file, 'tekst')

# output:
# Writing to regular file
# Reading from regular file
# Reading from readonly file

Poniżej dobry kod:
"""


class ReadableFile(ABC):
    @abstractmethod
    def read(self) -> str: ...


class WritableFile(ABC):
    @abstractmethod
    def write(self, input_text: str) -> None: ...


class NormalFile(ReadableFile, WritableFile):
    def read(self) -> str:
        # read file implementation
        print('Reading from file')

    def write(self, input_text: str) -> None:
        # write file implementation
        print('Writing to file')


class ReadonlyFile(ReadableFile):
    def read(self) -> str:
        # read readonly file implementation
        print('Reading from readonly file')