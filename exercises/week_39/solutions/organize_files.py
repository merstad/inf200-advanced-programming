"""
Example solution for file renaming task.

Collect metadata in the form

    Date: 2021-09-27
    Location: Ås
    Number: 334

provided at the beginning of files from files in a flat
directory and rename each file placing it into a hierarchical
directory structure

    new_scheme/YYYY-MM/DD/<location>/000nnn.txt
"""

__author__ = 'Hans Ekkehard Plesser and Sanjayan Rengarajan, NMBU'

from pathlib import Path
import re


def _parse_metadata(filename):
    """
    Extract metadata from file.

    :param filename: Name of file to inspect.
    :return: Dictionary with metadata.
    """

    with open(filename, encoding='utf-8') as data_file:
        # Collect metadata by reading one line at a time,
        # matching against a regex collecting field name and value.
        # Loop ends either if three metadata items have been found
        # or a line that does not match the regex is encountered.
        meta_re = re.compile(r'(\w+)\s*:\s*(.+)')
        metadata = {}
        while len(metadata) < 3 and (m := meta_re.match(data_file.readline())):
            field, value = m.groups()
            metadata[field] = value

    return metadata


def move_files_to_hierarchy(source_path, target_path):
    """
    Move files to hierarchical folder structure based on metadata.

    :param source_path: Location of input data (string or Path)
    :param target_path: Top-level destination directory (string or Path)
    """

    # Ensure we have Path objects even if user passes strings
    source_path = Path(source_path)
    target_path = Path(target_path)

    # Parse and move one file at a time
    for source_name in source_path.glob('*.txt'):
        metadata = _parse_metadata(source_name)

        # Split date
        year_month, day = metadata['Date'].rsplit('-', maxsplit=1)

        # Build target directory path
        target_dir = target_path / year_month / day / metadata['Location']

        # Build target file name
        target_name = target_dir / f"{int(metadata['Number']):06d}.txt"

        # Create directory for target
        #   parents=True : intermediate directories will be created if necessary
        #   exist_ok=True: if directory exists already, do nothing
        target_dir.mkdir(parents=True, exist_ok=True)

        # Move file to its new destination
        source_name.rename(target_name)


if __name__ == '__main__':
    move_files_to_hierarchy(Path('./old_scheme'), Path('./new_scheme'))
