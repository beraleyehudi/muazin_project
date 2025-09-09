class SSTHelper:
    def __init__(self):
        self._temp_file_path = r'temp\audio_file number 0'
        self._serial_number = 0


    def write_bytes_to_wav(self,data_bytes):
        self._temp_file_path = self._temp_file_path.replace(str(self._serial_number), str(self._serial_number + 1))
        with open(self._temp_file_path, 'wb') as f:
            f.write(data_bytes)
        self._serial_number += 1
        pass

    def text_from_speach(self, data_bytes) -> str:
        self.write_bytes_to_wav(data_bytes)
        pass
