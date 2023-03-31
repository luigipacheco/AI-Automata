class BlobManager:
    def __init__(self):
        self.blobs = []
        self.command_queues = []
        self.selected_blob_index = 0

    def add_blob(self, blob):
        self.blobs.append(blob)
        self.command_queues.append([])

    def get_selected_blob(self):
        return self.blobs[self.selected_blob_index]

    def get_selected_command_queue(self):
        return self.command_queues[self.selected_blob_index]

    def set_selected_blob(self, index):
        if 0 <= index < len(self.blobs):
            self.selected_blob_index = index
