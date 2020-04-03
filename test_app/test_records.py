import os

from app.records import add_new_record, get_records


class TestAdd():
    def test_add(self):
        add_new_record('record')

    def test_add_after_del(self):
        os.remove('records.txt')
        add_new_record('record')
        assert (get_records() == ['record 1'])

    def test_many_adds(self):
        os.remove('records.txt')
        add_new_record('a')
        add_new_record('b')
        add_new_record('c')
        add_new_record('d')
        assert (get_records() == ['a 1', 'b 1', 'c 1', 'd 1'])

    def test_many_dif_adds(self):
        os.remove('records.txt')
        add_new_record('a')
        add_new_record('a')
        add_new_record('a')
        assert (get_records() == ['a 3'])
