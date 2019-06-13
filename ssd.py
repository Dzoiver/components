class Storage:
    def __init__(self):
        self.capacity1 = 'NULL'
        self.capacity2 = 'NULL'

    def set_storage(self, capacity1, capacity2):
        if capacity1.get() == 1:
            self.capacity1 = '500 GB'
        if capacity2.get() == 1:
            self.capacity2 = '1 TB'
