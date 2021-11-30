#! python3
# Test regex against list of str to match and list of str that should not.
import re
import sys


def regex_test(
        pattern, to_pass_match, to_fail_match):
    """
    Tests success/failure of regular expression pattern.

    Args:
        pattern (raw string): regex pattern string
        to_pass_match (list): list of strings that should return match object.
        to_fail_match (list): list of strings that should return None.

    Example:
    >>> regex_pattern = (r'^([0-3]\d)/([01]\d)/([0-2](\d){3})$')
    >>> passing_strings = ['20/01/2020', '31/09/1000', '01/12/1943']
    >>> failing_strings = ['41/10/2999', '01/2021', '12/11/190']
    >>> regex_test(regex_pattern, passing_strings, failing_strings)
    Regex worked. Matched "20/01/2020"
    Regex worked. Matched "31/09/1000"
    Regex worked. Matched "01/12/1943"
    Regex worked. Did not match "41/10/2999"
    Regex worked. Did not match "01/2021"
    Regex worked. Did not match "12/11/190"
    """
    pattern = re.compile(pattern)
    for i in to_pass_match:
        try:
            pass_match = pattern.search(i).group()
        except AttributeError:
            print(f'Regex failed. Did not match "{i}"')
        else:
            print(f'Regex worked. Matched "{pass_match}"')
        finally:
            continue

    for i in to_fail_match:
        try:
            fail_match = pattern.search(i).group()
        except AttributeError:
            print(f'Regex worked. Did not match "{i}"')
        else:
            print(f'Regex failed. Matched "{fail_match}"')
        finally:
            continue


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print('Usage: regex_test "regex_pattern", "list_of_passing_strings"',
              '"list_of_failing_strings"')
        raise SystemExit
    regex_pattern = rf'{sys.argv[1]}'
    passing_strings = sys.argv[2]
    failing_strings = sys.argv[3]
    regex_test(regex_pattern, passing_strings, failing_strings,)
