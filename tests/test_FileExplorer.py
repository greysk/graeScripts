from pathlib import Path

import pytest

from graeScript.FileExplorer.delete_move_dirs import (validate_args,
                                                      validate_dir,
                                                      validate_dirs,
                                                      block_protected)


class TestValidateArgs:
    def test_one(self):
        user_input = 'replace', 'cancel', 'delete'
        num_allowed = 1
        with pytest.raises(SystemExit):
            assert validate_args(
                user_input, num_allowed, 'replace', 'compare', 'delete')

    def test_two(self):
        user_input = 'make', 'withdraw', 'plan'
        num_allowed = 5
        assert validate_args(
            user_input, num_allowed, 'make', 'withdraw', 'plan',
            'deposit', 'draw', 'sample', 'save') == ['make',
                                                     'withdraw',
                                                     'plan']

    def test_three(self):
        user_input = 'replace', 'cancel'
        num_allowed = 1
        assert validate_args(
            user_input, num_allowed, 'replace', 'compare', 'delete') == [
                'replace']


class TestValidateDir:
    home = Path().home()

    def test_one(self):
        with pytest.raises(SystemExit):
            assert validate_dir('/src/graeScript/data')

    def test_two(self):
        with pytest.raises(SystemExit):
            assert validate_dir(self.home / 'bananaPaperSmallFakeFolder')

    def test_three(self):
        assert validate_dir(str(self.home)) == self.home


class TestValidateDirs:
    home = Path().home()
    fake_folder = home / 'bananaPaperSmallFakeFolder'

    def test_one(self):
        assert validate_dirs('/src/graeScript/data',
                             str(self.home),
                             self.fake_folder) == [self.home]

    def test_two(self):
        with pytest.raises(SystemExit):
            assert validate_dirs('/src/graeScript/data', self.fake_folder)

