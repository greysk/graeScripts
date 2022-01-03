from pathlib import Path

import pytest

from graeScript.FileExplorer.delete_move_dirs import (_validate_args,
                                                      _validate_dir,
                                                      _validate_dirs)


class TestValidateArgs:
    def test_one(self):
        user_input = 'replace', 'cancel', 'delete'
        num_allowed = 1
        with pytest.raises(SystemExit):
            assert _validate_args(user_input, num_allowed, 'replace',
                                  'compare', 'delete')

    def test_two(self):
        user_input = 'make', 'withdraw', 'plan'
        num_allowed = 5
        assert _validate_args(user_input, num_allowed,
                              'make', 'withdraw', 'plan', 'deposit',
                              'draw', 'sample', 'save'
                              ) == ['make', 'withdraw', 'plan']

    def test_three(self):
        user_input = 'replace', 'cancel'
        num_allowed = 1
        assert _validate_args(user_input, num_allowed, 'replace',
                              'compare', 'delete'
                              ) == ['replace']


class TestValidateDir:
    home = Path().home()

    def test_one(self):
        with pytest.raises(SystemExit):
            assert _validate_dir('/src/graeScript/data')

    def test_two(self):
        with pytest.raises(SystemExit):
            assert _validate_dir(self.home / 'bananaPaperSmallFakeFolder')

    def test_three(self):
        assert _validate_dir(str(self.home)) == self.home


class TestValidateDirs:
    home = Path().home()
    fake_folder = home / 'bananaPaperSmallFakeFolder'

    def test_one(self):
        assert _validate_dirs('/src/graeScript/data',
                              str(self.home),
                              self.fake_folder) == [self.home]

    def test_two(self):
        with pytest.raises(SystemExit):
            assert _validate_dirs('/src/graeScript/data', self.fake_folder)
