import pytest

from graeScript.markdown import to_md_list as to_md


class TestList():
    def test2indent(self):
        two_indent = ('This is an example list:\n'
                      '\n'
                      '  This is the first item\n'
                      '  This is a second.\n'
                      '    This should be nested\n'
                      '      This should be double nested.\n')
        correct_output = ['This is an example list:\n',
                          '\n',
                          '- This is the first item\n',
                          '- This is a second.\n',
                          '  - This should be nested\n',
                          '    - This should be double nested.\n']
        assert to_md.bullet_list(two_indent) == correct_output
