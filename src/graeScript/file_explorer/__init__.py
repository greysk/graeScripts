__all__ = (
    'compare_files',
    'delete_move_dirs',
    'find_files',
    'find_photo_folder',
    '_block_protected'
    )

import re
import sqlite3
from pathlib import Path

from graeScript import db_blockprotected_path


class _WindowsRules:
    def __init__(self) -> None:
        """Provides access to file- and directory-protecting rules.
        """
        pass

    __db = db_blockprotected_path('win')

    def check_against(self, path: Path,
                      rule_group: str = 'all') -> Path | None:
        """
        Checks input path against rules which block paths.

        rule_group can be one of the following:
            - 'path_to': blocks paths which end in part matching regex rule.
            - 'in_tree': blocks paths for which any part matches regex rule.
            - 'all': checks paths against both 'path_to' and 'in_tree' rules.

        Args:
            rule_group (str, optional): Which rules to check. Default is 'all'.
            path (Path): The path to check to see if blocked.

        Raises:
            TypeError: Raised if rule_group is not one of the accepted groups.

        Returns:
            Path: Returned if path was not blocked.
            None: Returned if path was blocked.
        """
        GROUPS = ('path_to', 'in_tree', 'all')
        rules_failed = 0
        if rule_group not in GROUPS:
            raise TypeError(f'Expected {rule_group} to be one of {GROUPS}')
        elif rule_group == 'all':
            rules = self.get
        elif rule_group == 'path_to':
            rules = self.get_path_to
        else:
            rules = self.get_in_tree
        for rule in rules:
            pattern = re.compile(rule)
            if pattern.search(str(path)):
                rules_failed += 1
            else:
                continue
        if not rules_failed:
            return path
        else:
            return None

    @property
    def get(self) -> frozenset[str]:
        """
        Returns:
            frozenset[str]: All Windows regex rules from database.
        """
        tables = self.TABLES
        rules = []
        with sqlite3.connect(self.__db) as conn:
            cur = conn.cursor()
            for table in tables:
                cur.execute(f'SELECT pattern FROM {table!r};')
                rules.extend(cur.fetchall())
            return frozenset([item[0] for item in rules])

    @property
    def get_in_tree(self) -> frozenset[str]:
        """
        Returns:
            frozenset[str]: All Windows in_tree regex rules from database.
        """
        with sqlite3.connect(self.__db) as conn:
            cur = conn.cursor()
            cur.execute('SELECT pattern FROM in_tree_win;')
            return frozenset([item[0] for item in cur.fetchall()])

    @property
    def get_path_to(self) -> frozenset[str]:
        """
        Returns:
            frozenset[str]: All Windows path_to regex rules from database.
        """
        with sqlite3.connect(self.__db) as conn:
            cur = conn.cursor()
            cur.execute('SELECT pattern FROM path_to_win;')
            return frozenset([item[0] for item in cur.fetchall()])

    @property
    def TABLES(self) -> tuple[str]:
        """
        Returns:
            tuple[str]: Accessible tables in database
        """
        return ('in_tree_win', 'path_to_win')


class _LinuxRules:
    def __init__(self) -> None:
        """
        Provides access to file- and directory-protecting rules.
        """
        pass

    __db = db_blockprotected_path('linux')

    def check_against(self, path: Path,
                      rule_group: str = 'all') -> Path | None:
        """
        Checks input path against rules which block paths.

        rule_group can be one of the following:
            - 'path_to': blocks paths which end in part matching regex rule.
            - 'in_tree': blocks paths for which any part matches regex rule.
            - 'all': checks paths against both 'path_to' and 'in_tree' rules.

        Args:
            rule_group (str, optional): Which rules to check. Default is 'all'.
            path (Path): The path to check to see if blocked.

        Raises:
            TypeError: Raised if rule_group is not one of the accepted groups.

        Returns:
            Path: Returned if path was not blocked.
            None: Returned if path was blocked.
        """
        GROUPS = ('path_to', 'in_tree', 'all')
        rules_passed = 0
        if rule_group not in GROUPS:
            raise TypeError(f'Expected {rule_group} to be one of {GROUPS}')
        elif rule_group == 'all':
            rules = self.get
        elif rule_group == 'path_to':
            rules = self.get_path_to
        else:
            rules = self.get_in_tree
        for rule in rules:
            pattern = re.compile(rule)
            if pattern.search(path):
                rules_passed += 1
            else:
                continue
        if rules_passed:
            return path
        else:
            return None

    @property
    def get(self) -> frozenset[str]:
        """
        Returns:
            frozenset[str]: All Linux regex rules from database.
        """
        tables = self._TABLES
        rules = []
        with sqlite3.connect(self.__db) as conn:
            cur = conn.cursor()
            for table in tables:
                cur.execute(
                    f'SELECT pattern FROM {table!r};')
                rules.extend(cur.fetchall())
            return frozenset([item[0] for item in rules])

    @property
    def get_in_tree(self) -> frozenset[str]:
        """
        Returns:
            frozenset[str]: All Linux in_tree regex rules from database.
        """
        with sqlite3.connect(self.__db) as conn:
            cur = conn.cursor()
            cur.execute('SELECT pattern FROM in_tree_win;')
            return frozenset([item[0] for item in cur.fetchall()])

    @property
    def get_path_to(self) -> frozenset[str]:
        """
        Returns:
            frozenset[str]: All Linux path_to regex rules from database.
        """
        with sqlite3.connect(self.__db) as conn:
            cur = conn.cursor()
            cur.execute('SELECT pattern FROM path_to_win;')
            return frozenset([item[0] for item in cur.fetchall()])

    @property
    def _TABLES(self) -> tuple[str]:
        """
        Returns:
            tuple[str]: Accessible tables in database
        """
        return ('in_tree_linux', 'path_to_linux')
